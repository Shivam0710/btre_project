from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('', include('pages.urls')),
    url('listings/', include('listings.urls')),
    url(r'^admin/', admin.site.urls),
]
