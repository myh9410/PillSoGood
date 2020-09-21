from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('users/signup/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),

    path('supplements/', include('supplements.urls'))
]
