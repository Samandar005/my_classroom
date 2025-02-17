from django.urls import path
from . import  views

app_name='users'

urlpatterns=[
    path('list/', views.UserListView.as_view(), name='list'),
    path('create/', views.UserCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.UserDeleteView.as_view(), name='delete'),
]