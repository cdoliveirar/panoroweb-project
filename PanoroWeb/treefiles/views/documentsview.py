'''
Created on 21/01/2013

@author: Carlos Oliveira
'''
'''
from treefiles.models import Documents, Folders
from django.http import HttpResponse
from django.shortcuts import render_to_response
import logging
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger =logging.getLogger()
'''

'''
def documentList(request,id):
    logger.info(id+'<<<<<<< id')
    document_filter_list = Documents.objects.filter(cd_folder = id)
    
    tamanho = document_filter_list.count()
    logger.info("documento size >>>> %s"% tamanho)
    for document in range(len(document_filter_list)):
        logger.info(document_filter_list[document])
        
    folder_list = Folders.objects.all()    

    return render_to_response("panorotreefiles.html",{"document_list":document_filter_list,
                                                      "folder_list":folder_list})
@login_required(login_url='/login/')    
def search(request):
    return render_to_response("searchdocument.html","",context_instance=RequestContext(request))

'''
'''
def serching_documents(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        filter_documents = Documents.objects.filter(nm_document__contains=q)
        #        
        
        return render_to_response("searchdocument.html",{"filter_documents":filter_documents,"quey":q},context_instance=RequestContext(request))
    else:
        return render_to_response('searchdocument.html', {'error': True},context_instance=RequestContext(request))
'''    
''' 
@login_required(login_url='/login/') 
def searching_documents(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        filter_documents = Documents.objects.filter(nm_document__contains=q)
        document_amount = filter_documents.count()
        #
        paginator = Paginator(filter_documents, 15)
        page = request.GET.get('page')
        try:
            documents = paginator.page(page)
        except PageNotAnInteger:
            documents = paginator.page(1)
        except EmptyPage:
            documents = paginator.page(paginator.num_pages)    
        #
        
        return render_to_response("searchdocument.html",{"query":q,"documents": documents,"docAmount": document_amount},context_instance=RequestContext(request))
    else:
        return render_to_response('searchdocument.html', {'error': True},context_instance=RequestContext(request))
    
'''    
    
    
    
    
    
    
    
    
    
        