from django.urls import path
from . import views

app_name = 'app_a'
urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:pk>/', views.ProjectDetail.as_view(), name='project_detail'),
    path('delete_file/<int:pk>/<int:doc_pk>/', views.delete_file, name='delete_file'),
]

