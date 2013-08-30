# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models

class Alarms(models.Model):
    id_alarm = models.IntegerField(primary_key=True)
    tp_alarm = models.IntegerField()
    cd_document = models.IntegerField()
    dt_creation = models.DateTimeField(null=True, blank=True)
    dt_limit = models.DateTimeField(null=True, blank=True)
    pt_critical = models.IntegerField(null=True, blank=True)
    pt_attention = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'alarms'

class Alarmtypes(models.Model):
    id_alarm_type = models.IntegerField(primary_key=True)
    nm_alarm_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'alarmtypes'

class Attachments(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_document = models.IntegerField()
    cd_link = models.IntegerField()
    class Meta:
        db_table = 'attachments'


class Basins(models.Model):
    gid = models.IntegerField(primary_key=True)
    nm_basin = models.CharField(max_length=50, blank=True)
    situation = models.IntegerField(null=True, blank=True)
    geom = models.MultiPolygonField(srid=4618, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'basins'

class Countries(models.Model):
    gid = models.IntegerField(primary_key=True)
    nm_country = models.CharField(max_length=26, blank=True)
    the_geom = models.GeometryField(srid=4618, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'countries'


class DocumentKeyword(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_document = models.IntegerField()
    cd_keyword = models.ForeignKey('Keywords', db_column='cd_keyword')
    class Meta:
        db_table = 'document_keyword'

class DocumentSource(models.Model):
    id_doc_source = models.IntegerField(primary_key=True)
    nm_doc_source = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'document_source'

class DocumentState(models.Model):
    id_doc_state = models.IntegerField(primary_key=True)
    nm_doc_state = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'document_state'

class DocumentSuport(models.Model):
    id_doc_suport = models.IntegerField(primary_key=True)
    nm_doc_suport = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'document_suport'

class DocumentTypes(models.Model):
    id_doc_type = models.IntegerField(primary_key=True)
    nm_doc_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'document_types'

class DocumentVia(models.Model):
    id_doc_via = models.IntegerField(primary_key=True)
    nm_doc_via = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'document_via'

class Documents(models.Model):
    id_document = models.IntegerField(primary_key=True)
    nm_document = models.CharField(max_length=200, blank=True)
    tp_document = models.IntegerField(null=True, blank=True)
    dt_modify = models.DateTimeField(null=True, blank=True)
    dt_create = models.DateTimeField(null=True, blank=True)
    dt_insert = models.DateTimeField(null=True, blank=True)
    extension = models.CharField(max_length=20, blank=True)
    nm_author = models.CharField(max_length=100, blank=True)
    protocol = models.CharField(max_length=20, blank=True)
    title = models.CharField(max_length=200, blank=True)
    path = models.CharField(max_length=200, blank=True)
    size = models.IntegerField(null=True, blank=True)
    cd_via = models.IntegerField(null=True, blank=True)
    cd_state = models.IntegerField(null=True, blank=True)
    cd_suport = models.IntegerField(null=True, blank=True)
    cd_source = models.IntegerField(null=True, blank=True)
    cd_folder = models.ForeignKey('Folders', db_column='cd_folder')
    review = models.IntegerField(null=True, blank=True)
    finalized = models.NullBooleanField(null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = 'documents'

class ExplorationBlocks(models.Model):
    gid = models.IntegerField(primary_key=True)
    nm_block = models.CharField(max_length=10, blank=True)
    geom = models.MultiPolygonField(srid=4618, null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        db_table = 'exploration_blocks'

class Folders(models.Model):
    id_folder = models.IntegerField(primary_key=True)
    nm_folder = models.CharField(max_length=200, blank=True)
    tp_folder = models.IntegerField(null=True, blank=True)
    cd_parent = models.IntegerField(null=True, blank=True)
    nm_path = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = 'folders'

class FoldersBasins(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_folder = models.ForeignKey(Folders, null=True, db_column='cd_folder', blank=True)
    cd_basin = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_basins'

class FoldersBlocks(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_folder = models.ForeignKey(Folders, null=True, db_column='cd_folder', blank=True)
    cd_block = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_blocks'

class FoldersCountries(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_folder = models.ForeignKey(Folders, null=True, db_column='cd_folder', blank=True)
    cd_country = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_countries'

class FoldersFields(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_folder = models.ForeignKey(Folders, null=True, db_column='cd_folder', blank=True)
    cd_field = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_fields'

class FoldersTypes(models.Model):
    id_folder_type = models.IntegerField(primary_key=True)
    nm_folder_type = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'folders_types'

class FoldersWells(models.Model):
    id = models.IntegerField(primary_key=True)
    cd_folder = models.ForeignKey(Folders, null=True, db_column='cd_folder', blank=True)
    cd_well = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'folders_wells'

class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True) # This field type is a guess.
    f_table_schema = models.TextField(blank=True) # This field type is a guess.
    f_table_name = models.TextField(blank=True) # This field type is a guess.
    f_geography_column = models.TextField(blank=True) # This field type is a guess.
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.TextField(blank=True)
    class Meta:
        db_table = 'geography_columns'

class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, blank=True)
    f_table_schema = models.CharField(max_length=256, blank=True)
    f_table_name = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension = models.IntegerField(null=True, blank=True)
    srid = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=30, blank=True)
    class Meta:
        db_table = 'geometry_columns'

class Keywords(models.Model):
    id_keyword = models.IntegerField(primary_key=True)
    nm_keyword = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=100, blank=True)
    class Meta:
        db_table = 'keywords'

class ProductionFields(models.Model):
    gid = models.IntegerField(primary_key=True)
    nm_field = models.CharField(max_length=150, blank=True)
    geom = models.MultiPolygonField(srid=4618, null=True, blank=True)
    objects = models.GeoManager()
    
    def __unicode__(self):
        return u'{0}'.format(self.nm_field)
    
    class Meta:
        db_table = u'production_fields'    


class Xmldata(models.Model):
    id = models.IntegerField(primary_key=True)
    xmlinformation = models.TextField(blank=True)
    class Meta:
        db_table = u'xmldata'
        


class UserMessage(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    user_name = models.CharField(max_length=300, blank=True)
    message_string = models.CharField(max_length=300, blank=True)
    
    class Meta:
        db_table = 'user_message' 


class ServerPath(models.Model):
    id_path = models.IntegerField(primary_key=True)
    nm_path = models.CharField(max_length=50, blank=True)
    
    class Meta:
        db_table = 'server_path'
       