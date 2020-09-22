from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email as allauthemailconfirmation

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('users/signup/', include('rest_auth.registration.urls')),
    path('accounts/', include('allauth.urls')),
    url(r'accounts/confirmemail/(?P<key>[-:\w]+)/$',allauthemailconfirmation,
       name='account_confirm_email'),
    path('supplements/', include('supplements.urls'))
]
