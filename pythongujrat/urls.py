from django.conf.urls import patterns, include, url
from py_guj import views
from django.contrib import admin 
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'',include('py_guj.urls')),
)+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
