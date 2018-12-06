#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Short sammary of the descriptino of my project.

This is the long descriptiion of my project.
"""

from xml.dom import minidom 
import urllib2

__author__ = "Victor Guérin, Stéphane Guérin"
__copyright__ = "Copyright 2018, Skillkav inc."
__credits__ = ["Patrice Boudreaul", "Mathieu Auclair"]
__version__ = "0.0.2"
__maintainer__ = "Victor Guérin"
__email__ = "victorguerin19@gmail.com"
__status__ = "Developpement"


ID_VIDEOTRON = 'vlxckshl'
forfaitVideotron = 130
url = 'http://dataproxy.pommepause.com/videotron_usage-12.php?'+ ID_VIDEOTRON

class Data:
    def __init__(self, forfaitVideotron):
        self.download = 0
        self.upload = 0
        self.dateFrom = ''
        self.dateTo = ''
        self.forfaitMB = 0
        self.utilisationTot = 0
        self.pourcentageActuel = 0
        self.deltaDay = 0
        self.moyenneJour = 0
        self.forfaitTot = forfaitVideotron

    def get(self, dom):
        usage = dom.getElementsByTagName('usage')[0]
        if usage.getElementsByTagName('download').length == 0:
            erreur = usage.getElementsByTagName('error')[0].childNodes[0].nodeValue
            print("***ERREUR*** \n" + erreur)
        else :
            print("***Connection \xe9tablie*** \n")
            self.download = float(usage.getElementsByTagName('download')[0].childNodes[0].nodeValue)
            self.upload = float(usage.getElementsByTagName('upload')[0].childNodes[0].nodeValue) 
            self.dateFrom = usage.getElementsByTagName('from')[0].childNodes[0].nodeValue        
            self.dateTo = usage.getElementsByTagName('to')[0].childNodes[0].nodeValue
            self.forfaitMB = self.forfaitTot * 1000
            self.utilisationTot = self.download + self.upload
            self.pourcentageActuel = float((self.download + self.upload)/self.forfaitMB *100)
            dayFrom = int(self.dateFrom.split(" ")[1])
            dayTo = int(self.dateTo.split(" ")[1])
            
            if(dayFrom < dayTo or dayFrom == dayTo):
                self.deltaDay = int(dayTo - dayFrom)
            else:    
                self.deltaDay = int(dayTo - dayFrom + 30)
                
            if(self.deltaDay == 0):
                self.moyenneJour = self.utilisationTot
            else:
                self.moyenneJour = float(self.utilisationTot/self.deltaDay)    
            
            
    def printData(self):
        print(u'Donn\xe9es:')
        print(u'T\xe9l\xe9chargement: %s MB' % self.download)
        print(u'T\xe9l\xe9versement:  %s MB' % self.upload)
        print(u'Capacit\xe9 totale : %s MB' % self.forfaitMB)
        print(u"%.2f%% de la consommation totale utilis\xe9es" % self.pourcentageActuel)
        print(u'Diff\xe9rence de jours : %s' % self.deltaDay)
        print('Utilisation en moyenne : %.2f MB par jour' % self.moyenneJour) 

### MAIN ###
dom = minidom.parse(urllib2.urlopen(url))

data = Data(forfaitVideotron)
data.get(dom)
data.printData()






    
