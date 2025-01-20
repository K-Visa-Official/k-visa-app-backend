from django.urls import path
from ..views.admin_views import (
    PostAdminViewSet,
    UserAdminViewSet,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users', UserAdminViewSet, basename='admin-users')
router.register('posts', PostAdminViewSet, basename='admin-posts')
# router.register('visas', AdminVisaViewSet, basename='admin-visas')

# admin_urlpatterns = [
#     # 관리자 대시보드
#     path('dashboard/', AdminDashboardView.as_view(), name='admin-dashboard'),
#     path('statistics/', AdminStatisticsView.as_view(), name='admin-statistics'),
# ]

admin_urlpatterns = []
admin_urlpatterns += router.urls
