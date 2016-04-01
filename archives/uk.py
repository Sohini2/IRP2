# -*- coding: utf-8 -*-
__author__ = 'anuj'
from collection import Collection
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob

class UKFindingAid(Collection):

    def keywordResultsCount(self, inputs):
        self.inputs = inputs
        #query = "+".join(inputs.split())

        query = inputs.split(' ')
        x=len(query)
        print x

        if (x>1):

         try:

            blob = TextBlob(query[1])
            if (query[0]=='German'):
                query_german = blob.translate(to="de")
                query_german = unicode( query_german, "utf-8" )
                url = "http://discovery.nationalarchives.gov.uk/results/r?_q="+str(query_german)+"&_sd=&_ed=&discoveryCustomSearch=true&_col=200&_dt=LA&_hb=tna"
                self.result_search_term = str(query_german)
                self.result_search_term = self.result_search_term.encode('utf-8')

            elif (query[0]=='French') :
                query_french = blob.translate(to="fr")
                query_french = unicode( query_french, "utf-8" )
                url = "http://discovery.nationalarchives.gov.uk/results/r?_q="+str(query_french)+"&_sd=&_ed=&discoveryCustomSearch=true&_col=200&_dt=LA&_hb=tna"
                self.result_search_term = str(query_french)
                self.result_search_term = self.result_search_term.encode('utf-8')
         except:
            url = "http://discovery.nationalarchives.gov.uk/results/r?_q="+query[1]+"&_sd=&_ed=&discoveryCustomSearch=true&_col=200&_dt=LA&_hb=tna"
            self.result_search_term = str(query[1])
            pass

        else:
             url = "http://discovery.nationalarchives.gov.uk/results/r?_q="+query[0]+"&_sd=&_ed=&discoveryCustomSearch=true&_col=200&_dt=LA&_hb=tna"
             self.result_search_term = str(query[0])


        #url = "http://discovery.nationalarchives.gov.uk/results/r?_q="+query+"&_sd=&_ed=&discoveryCustomSearch=true&_col=200&_dt=LA&_hb=tna"
        try:
         html = requests.get(url).text

        except:
         url = "https://www.google.com/webhp?hl=en"
         html = requests.get(url).text
         print "Timeout error. Please try again later."
         pass
        soup = BeautifulSoup(html, "lxml")

        results = soup.find_all("li", class_="tna-result")
        count = results.__len__()

        self.results_url = url
        self.results_count = count

        return self
