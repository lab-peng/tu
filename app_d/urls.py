from django.urls import path
from . import views

app_name = 'app_d'

urlpatterns = [
    path('', views.SampleModelList.as_view(), name='list'),
    path('create_update/', views.create_update, name='create_update'),
    path('get_update_info/', views.get_update_info, name='get_update_info'),
    path('delete/', views.delete, name='delete')
]
