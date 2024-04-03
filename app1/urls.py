from django.urls import path
from .views import UserListCreateAPIView
from .views import registration_view, login_view


urlpatterns = [
    
    path('api/post/', UserListCreateAPIView.as_view(),name='post'),
    path('api/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('<str:username>/', UserListCreateAPIView.as_view(), name='user-details'),
    path('<str:username>/delete/',
         UserListCreateAPIView.as_view(), name='delete-user'),
    path('app1/register/', registration_view, name='registration'),
    path('app1/login/', login_view, name='login'),
    path('app1/loginsucces/', login_view),

]
