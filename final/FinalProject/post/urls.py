from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.PostList.as_view(), name='snippet-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='snippet-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserList.as_view(), name='user-detail'),
]

