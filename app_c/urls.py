from django.urls import path
from . import views

app_name = 'app_c'
urlpatterns = [
    path('', views.indexView),
    path('create_update_friend/', views.create_update_friend, name = "create_update_friend"),
    path('delete_friend/', views.delete_friend, name = "delete_friend"),
    path('edit_friend/', views.edit_friend, name = "edit_friend"),
    path('get/ajax/validate/nickname/', views.checkNickName, name = "validate_nickname"),

    path("cbv/", views.FriendView.as_view(), name = "friend_cbv")
]
