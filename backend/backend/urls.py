from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from allauth.account.views import confirm_email as allauthemailconfirmation

# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_url_patterns = [path('', include('backend.urls')), ]
schema_view = get_schema_view(openapi.Info(title="Django API", default_version='v1',
                                           terms_of_service="https://www.google.com/policies/terms/", ), public=True, patterns=schema_url_patterns, )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('rest_auth.urls')),
    path('users/signup/', include('rest_auth.registration.urls')),
    path('all-auth/accounts/', include('allauth.urls')),
    path('accounts/',include('accounts.urls')),
    path('supplements/', include('supplements.urls')),
    path('reviews/', include('reviews.urls')),
    # swagger
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('recommends/', include('recommends.urls')),
    
]
