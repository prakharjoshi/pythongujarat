from django.conf.urls import patterns, url
from py_guj import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *


urlpatterns = patterns('',
	url(r'^$',views.home, name = 'home'),
	url(r'/meetings^$',views.meetings, name = 'home'),
	url(r'/blog^$',views.blog, name = 'home'),
	url(r'/members^$',views.members, name = 'home'),
	url(r'/resources^$',views.resources, name = 'home'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
