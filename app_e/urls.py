from django.urls import path
from . import views
app_name = 'app_e'

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>/', views.update, name='update')
]
