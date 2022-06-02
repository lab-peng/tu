from django.urls import path
from . import views

app_name = 'app_a'
urlpatterns = [
    path('', views.index, name='index'),
    path('project_list/', views.ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('project_update/<int:pk>/', views.ProjectUpdate.as_view(), name='project_update'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),

    path('tianditu/', views.tianditu, name='tianditu')
]

