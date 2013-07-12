'''
Created on 30/04/2013

@author: Carlos Oliveira
'''

from dajaxice.decorators import dajaxice_register
from dajax.core import Dajax
from django.core.context_processors import request
from .utilfinder import FindGeoInformation

@dajaxice_register
def updateDropDownBasin(request, option):
    dajax = Dajax()
    print "Option: " + option
    basinList = FindGeoInformation().getBasinbyCountryId(option)
    out = []
    for basin in basinList:
        print basin.gid
        print basin.nm_basin
        out.append("<option value='%s'>%s</option>" % (basin.gid,basin.nm_basin))
        
    dajax.assign('#basin', 'innerHTML', ''.join(out))
    return dajax.json()


@dajaxice_register
def updateDropDownBlock(request, option):
    print option
    dajax = Dajax()
    blocksList = FindGeoInformation().getBlockbyBasinId(option)
    out = []
    for block in blocksList:
        print block.nm_block
        print block.gid
        out.append("<option value='%s'>%s</option>" % (block.gid,block.nm_block))
        
    dajax.assign('#block', 'innerHTML', ''.join(out))
    return dajax.json()