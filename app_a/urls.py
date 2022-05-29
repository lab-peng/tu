from django.urls import path
from . import views

app_name = 'app_a'
urlpatterns = [
    path('', views.index, name='index'),
    path('project_list/', views.ProjectList.as_view(), name='project_list'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),
    path('del_file/', views.del_file, name='del_file'),

    path('tianditu/', views.tianditu, name='tianditu')
]

