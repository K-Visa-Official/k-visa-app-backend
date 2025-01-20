from rest_framework import viewsets

from kvisa.models.post import Post
from django.db.models import Avg, Count


from ..serializers.admin_serializers import PostAdminSerializer, UserAdminSerializer
from ..permissions import IsAdminUser
from django.contrib.auth import get_user_model

User = get_user_model()


class UserAdminViewSet(viewsets.ModelViewSet):
    queryset = User.objects.filter(is_admin=False)
    serializer_class = UserAdminSerializer
    permission_classes = [IsAdminUser]


class PostAdminViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostAdminSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Post.objects.annotate(
            avg_rating=Avg('comments__rating'),
            comment_count=Count('comments')
        )
