from django.urls import path, include

from ..views.auth_views import (
    AppleLogin,
    KakaoLogin,
    GoogleLogin,
    FacebookLogin
)

auth_urlpatterns = [
    # dj-rest-auth 기본 URLs (로그인, 로그아웃 등)
    path('', include('dj_rest_auth.urls')),

    # 소셜 로그인 URLs
    path('kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('facebook/', FacebookLogin.as_view(), name='facebook_login'),
    path('apple/', AppleLogin.as_view(), name='apple_login'),
]
