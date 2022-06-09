from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('publicaciones/', include('app.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path("register", views.register_request, name="register")
] 

urlpatterns += staticfiles_urlpatterns()
