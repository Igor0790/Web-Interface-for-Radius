
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include  # add this


urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register'
    #path("", include("apps.home.urls")),
    path('acl/', include('apps.app_acl.urls')),
    path('users/', include('apps.app_users.urls')),
    path('front/', include('apps.app_front.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
