'''
Created on 28/01/2013

@author: Carlos Oliveira
'''
from xml.dom import minidom, Node
import StringIO

from searching.models import Xmldata


def consultingXmlData():
    xmlString = ''
    xmlList = Xmldata.objects.filter(id=1)
    for xmlobj in xmlList:
        xmlString = xmlobj.xmlinformation
    return xmlString    

doc = minidom.parseString(consultingXmlData())    
#doc = minidom.parse('C:/REALIZE/Teste.xml')
root = doc.documentElement # el root elementp 

def showParent(nodes):
    listParent = []
    if nodes.length > 0:
        for node in nodes:
            if node.nodeType == 1:
                att = node.attributes
                xx = att.items()
                #print "<li>" + xx[0][1]+" "+ xx[1][1] + "</li>"
                listParent.append("<li><span class='"'folder'"'>" + "<a href='"'/treeview/'+str(xx[0][1])+"'>"+str(xx[0][1])+" "+ str(xx[1][1]) +"</span>")
                #listParent.append("<li>" + str(xx[0][1])+" "+ str(xx[1][1]) +"</li>")
                if node.hasChildNodes:
                    listParent.append("<ul>")
                    listParent.append(showChildren(node.childNodes))
                    listParent.append("</ul>")
                    listParent.append("</li>")
                else:
                    listParent.append("</li>")
                            
    
    return listParent            
                
def showChildren(nodes):
    listChildrem = []
    childs = ''
    #print "<ul>"
    if nodes.length >0:
        for node in nodes:
            if node.nodeType == 1:
                if node.hasChildNodes:
                    att = node.attributes
                    xx = att.items()
                    #print "<li>" + xx[0][1]+" "+ xx[1][1] + "</li>"
                    listChildrem.append("<li><span class='"'folder'"'>"+ "<a href='"'/treeview/'+str(xx[0][1])+"'>"+str(xx[0][1])+" "+ str(xx[1][1]) + "</span>")
                    #listChildrem.append("<li>" + str(xx[0][1])+" "+ str(xx[1][1]) + "</li>")
                    listChildrem.append('<ul>')
                    listChildrem.append(showParent(node.childNodes))
                    listChildrem.append('</ul>')
                    listChildrem.append("</li>")
    #print "</ul>"
    
    for lischd in listChildrem:
        childs +=''.join(lischd)     
    return childs
    
#return cadenaHija
#xxx(doc.childNodes)
#xxx(doc.childNodes)

#if __name__ =="__main__tuhermanaesMain__":
def showMinidom():
    finalList = []
    finalList =  showParent(root.childNodes)
    print ''.join(map(str, finalList))
    return finalList

def main():
    cadenas= showMinidom()
    for cad in cadenas:
        #print cad
        print 'cad'
        
main()