from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('', include('pages.urls')),
    url('listings/', include('listings.urls')),
    url('accounts/', include('accounts.urls')),
    url('contacts/', include('contacts.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
