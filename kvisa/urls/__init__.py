from django.urls import path, include

from .admin_urls import admin_urlpatterns
from .user_urls import user_urlpatterns
from .auth_urls import auth_urlpatterns

urlpatterns = [
    # 관리자 URLs - /api/admin/...
    path('admin/', include(admin_urlpatterns)),
    # 일반 사용자 URLs - /api/user/...
    path('user/', include(user_urlpatterns)),
    # 인증 URLs - /api/auth/...
    path('auth/', include(auth_urlpatterns)),
]
