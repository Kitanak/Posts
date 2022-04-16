from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Django Shop",
      default_version='v1',
      contact=openapi.Contact(email="danilovhamza@mail.ru"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

api_urlpatterns = [
    path('posts/',include('posts.urls')),
    path('bot/',include('bot_app.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include(api_urlpatterns)),

    path("jet/", include("jet.urls", "jet")),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
