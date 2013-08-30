'''
Created on 23/08/2013

@author: Carlos Oliveira
'''

from .models import Documents, UserMessage, Keywords
from django.contrib import admin

''' Documents '''
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nm_document', 'path', 'dt_create','description','nm_author')
     
admin.site.register(Documents,DocumentAdmin)


''' keywords '''
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('nm_keyword','description')
     
admin.site.register(Keywords,KeywordsAdmin)

''' UserMessage '''
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('created_date','user_name','message_string')
     
admin.site.register(UserMessage,UserMessageAdmin)





