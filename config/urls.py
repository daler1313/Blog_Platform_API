from django.contrib import admin
from django.urls import path,include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path("users/", include("users.urls")),
    path("",include("posts.urls")),
    path("", include("comments.urls")),
]
if (settings.DEBUG):
    # swagger
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        # YOUR PATTERNS
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]
 