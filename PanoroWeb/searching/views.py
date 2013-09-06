# Create your views here.
import logging
import mimetypes
import os
import csv
import datetime
 

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.defaults import page_not_found
from django.core.servers.basehttp import FileWrapper

#from django.contrib.auth import user_logged_in


from .utilfinder import FindGeoDocumentation
from .utilfinder import FindGeoInformation

from .models import Countries
from .models import Documents
from .models import ProductionFields
from .models import Basins
from .models import ExplorationBlocks
from .models import UserMessage
from .models import ServerPath


logger =logging.getLogger()

@login_required(login_url='/login/')    
def search(request):
    filter_documents = Documents.objects.all()[:500]
    
    #document_amount = filter_documents.count()
    paginator = Paginator(filter_documents, 25)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)    
    
    return render_to_response("searchdocument.html",{"documents": documents},context_instance=RequestContext(request))
    

@login_required(login_url='/login/') 
def searching_documents(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        filter_documents = Documents.objects.filter(nm_document__contains=q)
              
        document_amount = filter_documents.count()
        #
        paginator = Paginator(filter_documents, 25)
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
def searchdocumentsbasin(request):
    countryItems = Countries.objects.all()
    return render_to_response ('filter_searching_basin.html',{'items':countryItems}, context_instance =  RequestContext(request))


@login_required(login_url='/login/') 
def searchdocumentblock(request):
    countryItems = Countries.objects.all()
    return render_to_response ('filter_searching_block.html',{'items':countryItems}, context_instance =  RequestContext(request))


@login_required(login_url='/login/')
def searchdocumentsfield(request):
    countryItems = Countries.objects.all()
    return render_to_response ('filter_searching_field.html',{'items':countryItems}, context_instance =  RequestContext(request))


#filters
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
        
        block = "block"
        
        blockName = FindGeoDocumentation().getBlockName(blockId)
        filter_documents = Documents.objects.filter(path__contains=blockName)
        logger.info("Number of Documents >> %s" % filter_documents.count())
        docAmount = filter_documents.count()
        #go csv
        #trato_csv(filter_documents)
        
        
        paginator = Paginator(filter_documents, 25)
        page = request.GET.get('page')
        try:
            documents = paginator.page(page)
        except PageNotAnInteger:
            documents = paginator.page(1)
        except EmptyPage:
            documents = paginator.page(paginator.num_pages)    
        #
        return render_to_response("document_list.html",{"block":block,"id": blockId,"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    else:
        return render_to_response('document_list.html', {'error': True},context_instance=RequestContext(request))


def searchFilterBasins(request):
    #country = request.POST['country']
    #basin = request.POST['basin']
    #if 'q' in request.GET and request.GET['q']:
    #bloque = request.POST.get('block')
    #print "algo mas" + bloque
    if 'basin' in request.GET and request.GET['basin']:
        basinId = request.GET['basin']
    #if 'block' in request.POST and request.POST.get('block'):
    #    bloque = request.POST.get('block')
    #    print bloque
    #    blockId = request.POST.get('block')
        basin = "basin"
        
        basinName = FindGeoDocumentation().getBasinName(basinId)
        logger.info("basin name>>>>>> %s" % basinName)
        filter_basin = Documents.objects.filter(path__contains=basinName)
        logger.info("Number of Documents >> %s" % filter_basin.count())
        docAmount = filter_basin.count()
        #
        paginator = Paginator(filter_basin, 25)
        page = request.GET.get('page')
        try:
            documents = paginator.page(page)
        except PageNotAnInteger:
            documents = paginator.page(1)
        except EmptyPage:
            documents = paginator.page(paginator.num_pages)    
        #
        return render_to_response("document_list.html",{"basin":basin,"id": basinId,"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    else:
        return render_to_response('document_list.html', {'error': True},context_instance=RequestContext(request))




def searchFilterFields(request):
    #country = request.POST['country']
    #basin = request.POST['basin']
    #if 'q' in request.GET and request.GET['q']:
    #bloque = request.POST.get('block')
    #print "algo mas" + bloque
    if 'field' in request.GET and request.GET['field']:
        fieldId = request.GET['field']
    #if 'block' in request.POST and request.POST.get('block'):
    #    bloque = request.POST.get('block')
    #    print bloque
    #    blockId = request.POST.get('block')
        
        field = "field"
        
        fieldName = FindGeoDocumentation().getFieldName(fieldId)
        logger.info("field name>>>>>> %s" % fieldName)
        filter_field = Documents.objects.filter(path__contains=fieldName)
        logger.info("Number of Documents >> %s" % filter_field.count())
        docAmount = filter_field.count()
        #
        paginator = Paginator(filter_field, 25)
        page = request.GET.get('page')
        try:
            documents = paginator.page(page)
        except PageNotAnInteger:
            documents = paginator.page(1)
        except EmptyPage:
            documents = paginator.page(paginator.num_pages)    
        #
        return render_to_response("document_list.html",{"field":field,"id": fieldId,"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    else:
        return render_to_response('document_list.html', {'error': True},context_instance=RequestContext(request))

#detail all Geo types
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
    
    paginator = Paginator(filter_documents, 25)
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
    logger.info("Basin Name >>>> " + basinName)
    filter_documents = Documents.objects.filter(path__contains=basinName)
    logger.info("amount of Basins >>>> %s" % filter_documents.count())
    docAmount = filter_documents.count()
    
    paginator = Paginator(filter_documents, 25)
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
    logger.info("Block Name >>>> " + blockName)
    
    filter_documents = Documents.objects.filter(path__contains=blockName)
    logger.info("amount of blocks >>>> %s" % filter_documents.count())
    docAmount = filter_documents.count()
    
    paginator = Paginator(filter_documents, 25)
    page = request.GET.get('page')
    try:
        documents = paginator.page(page)
    except PageNotAnInteger:
        documents = paginator.page(1)
    except EmptyPage:
        documents = paginator.page(paginator.num_pages)    
    #
    return render_to_response("block_document.html",{"documents": documents,"docAmount":docAmount},context_instance=RequestContext(request))
    
        
#Method Ajax
def findBasinbyCountry(request):
    if request.method == "POST" and request.is_ajax():
        countryId = request.POST.get('ddvalue')
        countryId = int(countryId)
        logger.info("country Id >>>> %s" % countryId)
        print request.POST 
        
        message = ""
        
        basinList = FindGeoInformation().getBasinbyCountryId(countryId)
        print basinList
        
        basinListRes = []
        for basin in basinList:
            basinListRes.append("<option value='%s'>%s</option>" % (basin.gid,basin.nm_basin))
        
    else:
        logger.info("No ajax approach")
    
    return HttpResponse(basinListRes)
    
    
def findBlockbyBasin(request):
    if request.method == "POST" and request.is_ajax():
        basinId = request.POST.get('ddvalue')
        basinId = int(basinId)
        print basinId
        print request.POST 
        
        blockList = FindGeoInformation().getBlockbyBasinId(basinId)
        print blockList
        
        blockListRes = []
        for block in blockList:
            blockListRes.append("<option value='%s'>%s</option>" % (block.gid,block.nm_block))
    else:
        logger.info("No ajax approach")
        
    return HttpResponse(blockListRes)
    

def findFieldbyBasin(request):
    if request.method == "POST" and request.is_ajax():
        basinId = request.POST.get('ddvalue')
        basinId = int(basinId)
        print basinId
        print request.POST 
        
        fieldList = FindGeoInformation().getFieldbyBasinId(basinId)
        print fieldList
        
        fieldListRes = []
        for field in fieldList:
            fieldListRes.append("<option value='%s'>%s</option>" % (field.gid,field.nm_field))
        
    else:
        logger.info("No ajax approach")
        
    return HttpResponse(fieldListRes)

#Allow download one file
def send_document(request,id):
    #serverPathId = 2
    documentObj = Documents.objects.get(id_document = id)
    serverPathObj = ServerPath.objects.get(id_path = 2)
    pathLocal = serverPathObj.nm_path
    print pathLocal
    
    filename = documentObj.nm_document
    
    logger.info("filename>> "+ filename)
    path = documentObj.path
    
    fullname = pathLocal + path + filename
    logger.info("fullname>> "+ fullname)
    
    #username = request.GET['username']
    #print username
    
    try:
        f = open(fullname, "rb")
        
        if request.user.is_authenticated():
            #user_logged_in = request.user
            userName = request.user
            #logger.error("User get document is>> "+ userName)
            print 
            u= UserMessage(user_name = userName, message_string = filename)
            u.save()
        
    except Exception, e:
        return page_not_found(request, template_name='404.html')
    try:
        wrapper = FileWrapper(f)
        response = HttpResponse(wrapper, mimetype=mimetypes.guess_type(filename)[0])
        response['Content-Length'] = os.path.getsize(fullname)
        #response['Content-Disposition'] = 'attachment; filename={0}'.format(filename)
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    except Exception, e:
        return page_not_found(request, template_name='500.html')



@login_required(login_url='/login/')
def search_user_requested(request):
    return render_to_response("user_document_search.html","",context_instance=RequestContext(request))


@login_required(login_url='/login/') 
def list_user_request(request):
    
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        filter_userlogger = UserMessage.objects.filter(user_name__contains=q)
        
        document_amount = filter_userlogger.count()
        #logger.info("document amount >> "+ document_amount)
        #
        paginator = Paginator(filter_userlogger, 25)
        page = request.GET.get('page')
        try:
            messages = paginator.page(page)
        except PageNotAnInteger:
            messages = paginator.page(1)
        except EmptyPage:
            messages = paginator.page(paginator.num_pages)    
        #
        
        return render_to_response("user_document_search.html",{"query":q,"messages": messages,"docAmount": document_amount},context_instance=RequestContext(request))
    else:
        return render_to_response('user_document_search.html', {'error': True},context_instance=RequestContext(request))
    
    
def user_message_csv(request,username):
    userMessage = UserMessage.objects.filter(user_name = username)
    currentDate = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    response = HttpResponse(mimetype='text/csv')
    #response['Content-Disposition'] = 'attachment; filename=userDocuments_'+username+'.csv'
    response['Content-Disposition'] = 'attachment; filename=Documents_'+username+'_'+currentDate+'.csv'
    # Create the CSV writer using the HttpResponse as the "file."
    writer = csv.writer(response,delimiter=";")
    writer.writerow(['User Name', 'Document','Date'])
    for message in userMessage:
        userName = message.user_name
        userDate = message.created_date.strftime("%Y-%m-%d %H:%M")
        userMessage = message.message_string
        writer.writerow([userName,userMessage,userDate])
    
    return response






    