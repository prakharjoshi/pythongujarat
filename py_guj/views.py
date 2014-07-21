from django.shortcuts import *
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse


def home(request):
	return render_to_response('py_guj/frontpage.html',context_instance=RequestContext(request))

def meetings(request):
	return render_to_response('py_guj/meetings.html',context_instance=RequestContext(request))

