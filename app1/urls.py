from django.urls import path
from .views import UserListCreateAPIView

urlpatterns = [
    path('', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('<int:user_id>/', UserListCreateAPIView.as_view(), name='user-details'),
    path('<int:user_id>/delete/', UserListCreateAPIView.as_view(), name='delete-user'),
]
