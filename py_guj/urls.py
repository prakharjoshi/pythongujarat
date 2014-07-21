from django.conf.urls import patterns, url
from py_guj import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import *


urlpatterns = patterns('',
	url(r'^$',views.home, name = 'home'),
	url(r'^meetings/$',views.meetings, name = 'meetings'),
	url(r'^blog/$',views.blog, name = 'home'),
	url(r'^members/$',views.members, name = 'home'),
	url(r'^resources/$',views.resources, name = 'home'),
	url(r'^python-resources/$',views.pythonresources, name = 'pythonresources'),
	url(r'^posting-policy/$',views.postingpolicy, name = 'postingpolicy'),
	url(r'^git-and-pull-requests/$',views.gitandpullrequest, name = 'gitandpullrequests'),
	url(r'^welcome/$',views.welcome, name = 'welcome'),
	url(r'^launching-website/$',views.launchingwebsite, name = 'launchingwebsite'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
