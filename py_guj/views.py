from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse


def home(request):
	return render_to_response('py_guj/frontpage.html/',context_instance=RequestContext(request))

def meetings(request):
	return render_to_response('py_guj/meeting.html/',context_instance=RequestContext(request))

def blog(request):
	return render_to_response('py_guj/blog.html/',context_instance=RequestContext(request))

def members(request):
	
	return render_to_response('py_guj/members.html/',context_instance=RequestContext(request))

def resources(request):
	return render_to_response('py_guj/resources.html/',context_instance=RequestContext(request))

def pythonresources(request):
	return render_to_response('py_guj/python-resources.html/',context_instance=RequestContext(request))

def postingpolicy(request):
	return render_to_response('py_guj/postingpolicy.html/',context_instance=RequestContext(request))

def gitandpullrequest(request):
	return render_to_response('py_guj/gitandpullrequest.html/',context_instance=RequestContext(request))

def welcome(request):
	return render_to_response('py_guj/welcome.html/',context_instance=RequestContext(request))

def launchingwebsite(request):
	return render_to_response('py_guj/launchingwebsite.html/',context_instance=RequestContext(request))
