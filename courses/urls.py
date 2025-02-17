from django.urls import path
from . import views


app_name='courses'
urlpatterns=[
    path('list/', views.CourseListView.as_view(), name='list'),
    path('create/', views.CreateCourseView.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateCourseView.as_view(), name='update'),
    path('delete/<int:pk>/', views.CourseDeleteView.as_view(), name='delete'),
]