# -*- coding: utf-8 -*-
__author__ = 'Anuj'
from collection import Collection
from bs4 import BeautifulSoup
import requests
import re
import json
import goslate
from textblob import TextBlob


class BerlinFindingAid(Collection):

    def keywordResultsCount(self, inputs):
        self.inputs = inputs

        print self.inputs
        print inputs

        query = inputs.split(' ',1)
        x=len(query)
        print 'berlin'
        print query[0]
        print x
        #print query[1]

        '''
        gs = goslate.Goslate()
        query1=gs.translate(query[2], 'de')
        print query1
        '''

        if (x>1):
         try:
            blob = TextBlob(query[1])

            if (query[0]=='German'):
                try:
                 query_german = blob.translate(to="de")
                 #query_german = unicode( query_german, "utf-8" )
                 self.result_search_term = str(query_german)
                 print 'berlin german : '+str(self.result_search_term)
                 #self.result_search_term = self.result_search_term.encode('utf-8')
                 url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_german)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
                except:
                 query_german = blob.translate(to="de")
                 query_german = unicode( query_german, "utf-8" )
                 self.result_search_term = str(query_german)
                 print 'berlin german : '+str(self.result_search_term)
                 self.result_search_term = self.result_search_term.encode('utf-8')
                 url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_german)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"

            elif (query[0]=='French') :

               try:
                 query_french = blob.translate(to="fr")
                 #query_german = unicode( query_german, "utf-8" )
                 self.result_search_term = str(query_french)
                 print 'berlin german : '+str(self.result_search_term)
                 #self.result_search_term = self.result_search_term.encode('utf-8')
                 url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_french)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
               except:
                 query_french = blob.translate(to="fr")
                 query_french = unicode( query_french, "utf-8" )
                 self.result_search_term = str(query_french)
                 print 'berlin german : '+str(self.result_search_term)
                 self.result_search_term = self.result_search_term.encode('utf-8')
                 url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_french)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"

            else:
                query1 = " "+inputs
                query1 = query1.split(' ',1)
                url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+query1[1]+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
                self.result_search_term = str(query1[1])

         except:
            url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+query[1]+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
            self.result_search_term = str(query[1])
            pass

        else:
            url = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+query[0]+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
            self.result_search_term = str(query[0])

        #query = "+".join(inputs.split())

        #url_g = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_german)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"
        #url_f = "http://www.lostart.de/Webs/DE/Datenbank/SucheMeldungSimpel.html?resourceId=4424&input_=4046&pageLocale=de&simpel="+str(query_french)+"&type=Simpel&type.HASH=a367122406f8d243ac08&suche_typ=MeldungSimpel&suche_typ.HASH=e2ace3636225271222d5&suchen=Suchen"



        html = requests.get(url).text
        soup = BeautifulSoup(html, "lxml")

        #divs = soup.find_all('div')
        #print "BBBBBBBBBBBBBBBBBBBBBBBBBBBBBb"
        #results = soup.find("div", {"id" : "id67734"})
        #results_1 = results.find("table", {"summary" : "suche0"})
        #results_2 = results_1.find("tbody")
        #results_3 = results_2.find_all("tr")
        #count =  results_3.__len__()

        results = soup.find("div", {"id" : "id67734"})
        results_1 = results.find("table", {"summary" : "suche0"})


        if results_1 is not None:
            captionResults = results_1.find("caption")
            #print 'berlin_captionResults : ' + str(captionResults)
            string1 = captionResults.string
            print string1
            x1 = string1.split()[0]
            try:
             self.results_count = int(string1.split()[0])
            except Exception as e:
              self.results_count = 0
              print 'berlin' + str(e)
            #print 'berlin_string1 : ' + str(string1)
            #self.results_count = int(string1.split()[0])


            print self.results_count
        else:
            self.results_count = 0

        self.results_url = url


        return self
