'''
Created on 17/01/2013

@author: carlos oliveira
'''
from django.shortcuts import render_to_response
from django.template import RequestContext


def panoroIndex(request):
    return render_to_response('index.html',"",context_instance=RequestContext(request))
    