from searching.models import Alarmtypes, Keywords,Basins, Countries, Xmldata
from django.contrib import admin

''' AlarmTypes '''
class AlarmTypesAdmin(admin.ModelAdmin):
    list_display = ('id_alarm_type', 'nm_alarm_type', 'description')
     
admin.site.register(Alarmtypes,AlarmTypesAdmin)

''' Keywords'''
class KeywordsAdmin(admin.ModelAdmin):
    list_display = ('id_keyword','nm_keyword','description')

admin.site.register(Keywords, KeywordsAdmin)

'''Basins '''
class BasinsAdmin(admin.ModelAdmin):
    list_display = ('gid','nm_basin','situation','geom')

admin.site.register(Basins, BasinsAdmin)

''' Countries '''
class CountriesAdmin(admin.ModelAdmin):
    list_display = ('gid','nm_country','the_geom')

admin.site.register(Countries,CountriesAdmin)

''' xmldata'''
class XmlDataAdmin(admin.ModelAdmin):
    list_display = ('xmlinformation',)

admin.site.register(Xmldata,XmlDataAdmin)
    

