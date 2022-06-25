from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from django.conf.urls import handler404, handler500, handler403

from django.conf import settings
from django.conf.urls.static import static

handler403 = 'app_d.views.custom_error_403'
handler404 = 'app_d.views.custom_error_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('accounts/login/', auth_views.LoginView.as_view(template_name="app_d/login.html", extra_context={'next':'/app_d/alpha/'}), name='login'),

    path('', include('app_a.urls')),
    # path('app_b/', include('app_b.urls')),
    path('app_c/', include('app_c.urls')),
    path('app_d/', include('app_d.urls')),
    path('app_e/', include('app_e.urls')),
    path('photos/', include('photos.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
