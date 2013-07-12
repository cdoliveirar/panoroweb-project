'''
Created on 22/01/2013

@author: realize
'''
from django.contrib.auth.models import User
#from treefiles.models import Documents, Folders
from django.http import HttpResponse
from django.shortcuts import render_to_response
import logging
from django.template import RequestContext

#from treefiles.views import minidomoperations as xxx
from treefiles.views.minidomoperations import showMinidom
#from test.test_contains import seq
import textwrap
#sessoin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger =logging.getLogger()


'''
def folderList(request):
    folder_list = Folders.objects.all()
    logger.info("documento size >>>> %s"% folder_list.count())
    
    return render_to_response("panorotreefiles.html",{"folder_list":folder_list})



@login_required(login_url='/login/')
def treeTest(request,id):
    logger.info(id+'<<<<<<< id')
    document_filter_list = Documents.objects.filter(cd_folder = id)
    
    listxmls = showMinidom()
    finalMenuString = ''
    for list in listxmls:
        finalMenuString +=''.join(list)
        print finalMenuString
    
    paginator = Paginator(document_filter_list, 12)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)
       
    
    return render_to_response("treefiles.html",{ "listxmls":finalMenuString, "documents":documents},context_instance=RequestContext(request))

'''
