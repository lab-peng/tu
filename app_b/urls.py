from django.urls import path
from . import views

app_name = 'app_b'
urlpatterns = [
    path('', views.ProductList.as_view(), name='product_list'),
    path('product_update/<int:pk>/', views.ProductUpdate.as_view(), name='product_update'),
]
