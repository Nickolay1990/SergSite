from django.conf.urls.static import static
from django.urls import path

from SergSite import settings
from .views import index


urlpatterns = [
    path('', index, name='index'),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)