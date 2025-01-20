from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.serializers import JWTSerializer
from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework.exceptions import AuthenticationFailed
from jwt import ExpiredSignatureError, DecodeError
from rest_framework_simplejwt.exceptions import InvalidToken


@extend_schema(
    request=SocialLoginSerializer,
    responses={
        200: JWTSerializer
    }
)
class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'your-redirect-url'


@extend_schema(
    request=SocialLoginSerializer,
    responses={
        200: JWTSerializer
    }
)
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'your-redirect-url'


@extend_schema(
    request=SocialLoginSerializer,
    responses={
        200: JWTSerializer
    }
)
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'your-redirect-url'


@extend_schema(
    request=SocialLoginSerializer,
    responses={
        200: JWTSerializer
    }
)
class AppleLogin(SocialLoginView):
    adapter_class = AppleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = 'your-redirect-url'


class TokenValidationView(APIView):
    """
    JWT 토큰 검증 API
    """
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        token = request.data.get('token', None)
        if not token:
            return Response({"detail": "Token is required"}, status=400)
        try:
            # UntypedToken을 사용하여 토큰 검증
            UntypedToken(token)
            return Response({"detail": "Token is valid"}, status=401)
        except ExpiredSignatureError:
            return Response({"detail": "Token has expired"}, status=401)
        except DecodeError:
            return Response({"detail": "Token is invalid"}, status=401)
        except InvalidToken:
            return Response({"detail": "Token is invalid"}, status=401)