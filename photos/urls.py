from django.urls import path

from . import views
app_name = 'photos'
urlpatterns = [
    path('clear/', views.clear_database, name='clear_database'),
    path('', views.BasicUploadView.as_view(), name='basic_upload'),
    path('progress-bar-upload/', views.ProgressBarUploadView.as_view(), name='progress_bar_upload'),
    path('drag-and-drop-upload/', views.DragAndDropUploadView.as_view(), name='drag_and_drop_upload'),
    path('delete_file/<int:pk>/', views.delete_file, name='delete_file'),
]
