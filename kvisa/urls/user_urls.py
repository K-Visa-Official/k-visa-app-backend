from django.urls import path
from ..views.user_views import (
    PostCommentsView,
    PostDetailView,
    PostListView,
    UserProfileView
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('profile', UserProfileViewSet, basename='user-profile')
# router.register('applications', VisaApplicationViewSet, basename='visa-applications')

user_urlpatterns = [
    # 비자 상태 확인
    path('me/', UserProfileView.as_view(), name='user-profile'),
    path('posts/', PostListView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
    path('posts/<int:post_id>/comments/', PostCommentsView.as_view()),
]

user_urlpatterns += router.urls
