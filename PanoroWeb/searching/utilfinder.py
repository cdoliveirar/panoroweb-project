'''
@author: Carlos Oliveira
'''
from django.contrib.gis.geos import *

import logging

from .models import Basins
from .models import ExplorationBlocks
from .models import Countries

logger =logging.getLogger()


class FindGeoInformation:
    
    def getBasinbyCountryId(self,number):
        #basinList = Basins.objects.filter(gid=number)
       # Countries.objects.filter(the_geom__contains=)
        countryObj = Countries.objects.get(gid= number)
        countryName = countryObj.nm_country
        logger.info('Pais Selected: ' + countryName)
        basinList = Basins.objects.raw('select  ba.* from countries c,basins ba where ST_INTERSECTS(c.the_geom,ba.geom) and c.nm_country = %s', [countryName]) 
        for b in basinList: 
            logger.info("Basin >> " +b.nm_basin)
            
        return basinList
    
    def getBlockbyBasinId(self,number):
        basinObj = Basins.objects.get(gid=number)
        basinName = basinObj.nm_basin
        blockList = ExplorationBlocks.objects.raw('select  eb.* from basins ba, exploration_blocks eb where ST_Contains(ba.geom,eb.geom) and ba.nm_basin =%s', [basinName])
        for block in blockList:
            logger.info("Block >> " +block.nm_block)
            
        return blockList


class FindGeoDocumentation():
    
    def getBlockName(self,number):
        block = ExplorationBlocks.objects.get(gid = number)
        print block.nm_block
        return block.nm_block
        
 
            