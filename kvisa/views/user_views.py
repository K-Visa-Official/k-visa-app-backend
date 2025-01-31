from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework import status

from django.db.models import F, Avg, Count
from kvisa.models.comment import Comment
from kvisa.models.post import Post
from kvisa.serializers.user_serializers import CommentSerializer, PostSerializer, UserSerializer
from drf_spectacular.utils import extend_schema
from kvisa.models.users import CustomUser
from django.http import JsonResponse

class UserCertifyView(APIView):
    
    # permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: UserSerializer}
    )
    def put(self, request):
        phone = phone = request.data.get("phone")  # 🔹 변경됨
        email = request.data.get("email") 

        if not phone:
            return Response({"error": "phone is required"}, status=400)
        
        certify = CustomUser.objects.get(email = email)  
        certify.phone_number = phone
        certify.save()
    
        # serializer = UserSerializer(request.user)
        return JsonResponse({"result": "success"})

   
class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        responses={200: UserSerializer}
    )
    def get(self, request):
        # 현재 로그인한 유저의 데이터만 가져옴
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    @extend_schema(
        request=UserSerializer,
        responses={200: UserSerializer}
    )
    def put(self, request):
        # 현재 로그인한 유저의 데이터만 수정
        serializer = UserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        responses={204: None}
    )
    def delete(self, request):
        user = request.user

        try:
            # 실제 삭제 대신 is_active를 False로 설정하는 방법 (소프트 삭제)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except Exception as e:
            return Response(
                {"error": "회원탈퇴 처리 중 오류가 발생했습니다."},
                status=status.HTTP_400_BAD_REQUEST
            )


class PostListView(APIView):

    @extend_schema(
        responses={200: PostSerializer(many=True)},
        operation_id="getPosts"
    )
    def get(self, request):
        post_type = request.query_params.get('post_type')

        # 기본 쿼리셋에 annotate 추가
        posts = Post.objects.annotate(
            avg_rating=Avg('comments__rating'),
            comment_count=Count('comments')
        ).order_by('-created_at')

        # post_type 필터링
        if post_type:
            posts = posts.filter(post_type=post_type)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):

    @extend_schema(
        responses={200: PostSerializer},
        operation_id="getPost"
    )
    def get(self, request, pk):
        try:
            post = Post.objects.annotate(
                avg_rating=Avg('comments__rating'),
                comment_count=Count('comments')
            ).get(pk=pk)
            # view_count 증가
            post.view_count = F('view_count') + 1
            post.save()

            # 업데이트된 데이터를 다시 가져옴
            post.refresh_from_db()

            serializer = PostSerializer(post)
            return Response(serializer.data)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostCommentsView(APIView):
    @extend_schema(
        responses={200: CommentSerializer(many=True)}
    )
    def get(self, request, post_id):
        try:
            comments = Comment.objects.filter(
                post_id=post_id).select_related('user')
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        request=CommentSerializer,
        responses={201: CommentSerializer}
    )
    @permission_classes([IsAuthenticated])
    def post(self, request, post_id):
        try:
            # post_id로 Post 존재 여부 확인
            post = Post.objects.get(id=post_id)

            # request.data에 post와 user 정보 추가
            data = request.data.copy()
            data['post'] = post_id

            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
