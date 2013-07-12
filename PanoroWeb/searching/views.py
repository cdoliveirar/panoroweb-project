# Create your views here.
import logging

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


from .utilfinder import FindGeoDocumentation
from .utilfinder import FindGeoInformation

from .models import Countries
from .models import Documents
from .models import ProductionFields
from .models import Basins
from .models import ExplorationBlocks


logger =logging.getLogger()

@login_required(login_url='/login/')    
def search(request):
    return render_to_response("searchdocument.html","",context_instance=RequestContext(request))


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




@login_required(login_url='/login/') 
def searching(request):
    countryItems = Countries.objects.all()
    return render_to_response ('filter_searching2.html',{'items':countryItems}, context_instance =  RequestContext(request))

def searchFilterDocuments(request):
    #country = request.POST['country']
    #basin = request.POST['basin']
    #if 'q' in request.GET and request.GET['q']:
    #bloque = request.POST.get('block')
    #print "algo mas" + bloque
    if 'block' in request.GET and request.GET['block']:
        blockId = request.GET['block']
    #if 'block' in request.POST and request.POST.get('block'):
    #    bloque = request.POST.get('block')
    #    print bloque
    #    blockId = request.POST.get('block')
        
        
        blockName = FindGeoDocumentation().getBlockName(blockId)
        filter_documents = Documents.objects.filter(path__contains=blockName)
        logger.info("Number of Documents >> %s" % filter_documents.count())
        docAmount = filter_documents.count()
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
        return render_to_response("document_list.html",{"block": blockId,"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    else:
        return render_to_response('document_list.html', {'error': True},context_instance=RequestContext(request))
    

def documents_detail(request, id):
    document = Documents.objects.filter(id_document = id)
    #print document.nm_document
    return render_to_response("document_detail.html",{"documents": document},context_instance=RequestContext(request))
        

def field_document_list(request, id):
    field = ProductionFields.objects.get(gid = id)
    fieldName = field.nm_field
    #print fieldName
    filter_documents = Documents.objects.filter(path__contains=fieldName)
    logger.info("amount of fields >>>> %s" % filter_documents.count())
    docAmount = filter_documents.count()
    
    paginator = Paginator(filter_documents, 15)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)    
    #
    return render_to_response("field_document.html",{"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))


def basin_document_list(request,id):
    basin = Basins.objects.get(gid = id)
    basinName = basin.nm_basin
    print basinName     
    filter_documents = Documents.objects.filter(path__contains=basinName)
    logger.info("amount of Basins >>>> %s" % filter_documents.count())
    docAmount = filter_documents.count()
    
    paginator = Paginator(filter_documents, 15)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)    
    #
    return render_to_response("basin_document.html",{"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    

def block_document_list(request,id):
    block = ExplorationBlocks.objects.get(gid = id)
    blockName = block.nm_block
    print blockName
    
    filter_documents = Documents.objects.filter(path__contains=blockName)
    logger.info("amount of blocks >>>> %s" % filter_documents.count())
    docAmount = filter_documents.count()
    
    paginator = Paginator(filter_documents, 15)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)    
    #
    return render_to_response("block_document.html",{"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    
        

def findBasinbyCountry(request):
    if request.method == "POST" and request.is_ajax():
        countryId = request.POST.get('ddvalue')
        countryId = int(countryId)
        print countryId
        print request.POST 
        
        message = ""
        
        basinList = FindGeoInformation().getBasinbyCountryId(countryId)
        print basinList
        
        basins = []
        for basin in basinList:
            basins.append("<option value='%s'>%s</option>" % (basin.gid,basin.nm_basin))
        
    else:
        logger.info("No ajax approach")
    
    return HttpResponse(basins)
    
    
    
def findBlockbyBasin(request):
    
    if request.method == "POST" and request.is_ajax():
        basinId = request.POST.get('ddvalue')
        basinId = int(basinId)
        print basinId
        print request.POST 
        
        blockList = FindGeoInformation().getBlockbyBasinId(basinId)
        print blockList
        
        blocks = []
        for block in blockList:
            blocks.append("<option value='%s'>%s</option>" % (block.gid,block.nm_block))
        
    else:
        logger.info("No ajax approach")
        
    return HttpResponse(blocks)
    

