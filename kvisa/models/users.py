from django.contrib.auth.models import AbstractUser
from django.db import models

from kvisa.constants import VISA_CHOICES


class CustomUser(AbstractUser):
    class OAuthType(models.TextChoices):
        GOOGLE = 'GOOGLE', '구글'
        KAKAO = 'KAKAO', '카카오'
        NAVER = 'NAVER', '네이버'

    # 기본 필드 재정의
    email = models.EmailField('이메일', unique=True)
    username = models.CharField('아이디', max_length=150, unique=True)
    password = models.CharField('비밀번호', max_length=128)

    # 추가 필드
    full_name = models.CharField('이름', max_length=150)
    phone_number = models.CharField('전화번호', max_length=20)
    nationality = models.CharField('국적', max_length=100)
    visa_type = models.CharField(
        '비자 종류',
        max_length=10,
        choices=VISA_CHOICES
    )
    visa_expiry_date = models.DateField('비자 만료일', null=True, blank=True)
    device = models.CharField('디바이스', max_length=200, blank=True)
    terms_agreed = models.BooleanField('약관 동의', default=False)

    # OAuth 연동 정보
    oauth_type = models.CharField(
        '연동 타입', max_length=10, choices=OAuthType.choices, null=True, blank=True)
    oauth_id = models.CharField('연동 ID', max_length=255, null=True, blank=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.email
