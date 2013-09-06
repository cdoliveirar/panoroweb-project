from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PanoroWeb.views.home', name='home'),
    # url(r'^PanoroWeb/', include('PanoroWeb.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #declarando Index path
    url(r'^$', 'indexpackage.views.panoroIndex'),
    #url(r'^treemodel/$', 'treefiles.views.ShowTreeFiles'),
    #url(r'^treelist/$', 'treefiles.views.folderview.folderList'),
    
    #url(r'^doclist/(?P<id>\w+)', 'treefiles.views.documentsview.documentList'),
    
    #sin lista de tabla
    #url(r'^treetest/$', 'treefiles.views.folderview.treeTest'),
    #envia la lista de xml a la pagina
    #url(r'^treeview/(?P<id>\w+)', 'treefiles.views.folderview.treeTest'),
    
    #allauth    
    (r'^accounts/', include('allauth.urls')),
    
    #search
    url(r'^search/$', 'searching.views.search'),
    url(r'^searchdoc/$', 'searching.views.searching_documents'),
    
    #session part
    url(r'^login/$', 'authentication.views.login_user'),
    url(r'^logout/$', 'authentication.views.logout_view'),
    
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    #url(r'^accounts/logout/$', 'authentication.views.logout_view'),
    
    url(r'^account/invalid/$', 'authentication.views.invalidAccount'),
    url(r'^account/loggedout/$', 'authentication.views.logout_show'),
    
    #userena
    #url(r'^accounts/', include('userena.urls')),
    #dr
    #(r'^accounts/', include('registration.backends.simple.urls')),
    
    #searching documents
    #url(r'^search2/$', 'searching.views.load_country_combo'),
    
    #search for basin
    url(r'^searchdocumentsbasin/$', 'searching.views.searchdocumentsbasin'),
    url(r'^searchFilterBasins/$', 'searching.views.searchFilterBasins'),
    #search for block
    url(r'^searchdocumentsblock/$', 'searching.views.searchdocumentblock'),
    url(r'^searchfilterblock/$', 'searching.views.searchFilterDocuments'),
        #search for field
    url(r'^searchdocumentsfield/$', 'searching.views.searchdocumentsfield'),
    url(r'^searchFilterFields/$', 'searching.views.searchFilterFields'),
    
    url(r'^documents_detail/(?P<id>\w+)', 'searching.views.documents_detail'),
    
    #searching fields
    url(r'^field/(?P<id>\w+)', 'searching.views.field_document_list'),    
    #searching basin
    url(r'^basin/(?P<id>\w+)', 'searching.views.basin_document_list'),
    #searching block
    url(r'^block/(?P<id>\w+)', 'searching.views.block_document_list'),
    
    #url(regex=r'^documents_detail/(?P<pk>\d+)/$',view=DocumentDetailView.as_view(),name="documents"
    
    #url(r'^ajax_test/$', 'searching.views.ajax_test' ),
    url(r'^findBasinbyCountry/$', 'searching.views.findBasinbyCountry', name='findBasinbyCountry'),
    url(r'^findBlockbyBasin/$', 'searching.views.findBlockbyBasin', name='findBlockbyBasin'),
    url(r'^findFieldbyBasin/$', 'searching.views.findFieldbyBasin', name='findFieldbyBasin'),
    # send document
    url(r'^download/(?P<id>\w+)', 'searching.views.send_document'),
    
    #user requested report
    url(r'^requested/$', 'searching.views.search_user_requested'),
    url(r'^searchrequested/$', 'searching.views.list_user_request'),
    #csv report
    url(r'^downloadcsv/(?P<username>\w+)', 'searching.views.user_message_csv'),
    
)
    
    


