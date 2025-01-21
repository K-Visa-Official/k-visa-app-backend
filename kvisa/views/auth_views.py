from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.apple.views import AppleOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.serializers import JWTSerializer
from drf_spectacular.utils import extend_schema


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
