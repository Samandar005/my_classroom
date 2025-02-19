from django.urls import path
from . import views


app_name='assignments'

urlpatterns=[
    path('list/', views.AssignmentListView.as_view(), name='list'),
    path('create/', views.AssignmentCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AssignmentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AssignmentDeleteView.as_view(), name='delete'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.AssignmentDetailView.as_view(), name='detail'),

]