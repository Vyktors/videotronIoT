# -*- coding: utf-8 -*-
#IMPORT
from xml.dom import minidom 
import urllib2

#
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
            print("Connection etablie")
            self.download = float(usage.getElementsByTagName('download')[0].childNodes[0].nodeValue)
            self.upload = float(usage.getElementsByTagName('upload')[0].childNodes[0].nodeValue) 
            self.dateFrom = usage.getElementsByTagName('from')[0].childNodes[0].nodeValue        
            self.dateTo = usage.getElementsByTagName('to')[0].childNodes[0].nodeValue
            self.forfaitMB = self.forfaitTot * 1000
            self.utilisationTot = self.download + self.upload
            self.pourcentageActuel = float((self.download + self.upload)/self.forfaitMB *100)
            dayFrom = int(self.dateFrom.split(" ")[1])
            dayTo = int(self.dateTo.split(" ")[1]) 
            if(dayFrom < dayTo):
                self.deltaDay = int(dayTo - dayFrom)
            else:    
                self.deltaDay = int(dayTo - dayFrom + 30)

            self.moyenneJour = float(self.utilisationTot/self.deltaDay)
            
    def printData(self):
        print('Donnees:')
        print('Telechargement: %s MB' % self.download)
        print('Televersement:  %s MB' % self.upload)
        print('Capacite totale : %s MB' % self.forfaitMB)
        print("%.2f%% de la consommation totale utilisees" % self.pourcentageActuel)
        print('Difference de jours : %s' % self.deltaDay)
        print('Utilisation en moyenne : %.2f MB par jour' % self.moyenneJour) 

### MAIN ###
dom = minidom.parse(urllib2.urlopen(url))

data = Data(forfaitVideotron)
data.get(dom)
data.printData()






    
