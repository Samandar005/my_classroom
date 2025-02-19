from django.urls import path
from . import views


app_name='assignments'

urlpatterns=[
    path('list/', views.AssignmentListView.as_view()  , name='list')
]