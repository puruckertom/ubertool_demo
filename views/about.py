# -*- coding: utf-8 -*-
"""
Created on Tue Jan 03 13:30:41 2012
@author: jharston
"""
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class aboutPage(webapp.RequestHandler):
    def get(self):
        text_file2 = open('about_text.txt','r')
        xx = text_file2.read()
        templatepath = os.path.dirname(__file__) + '/templates/'                     
        html = template.render(templatepath+'01uberheader.html', {'title':'Ubertool'})
        html = html + template.render(templatepath+'02uberintroblock_nomodellinks.html', {'title2':'Ecological Risk Web Applications','title3':''})
        html = html + template.render (templatepath + '03ubertext_links_left.html', {})                        
        html = html + template.render(templatepath + '04ubertext_start.html', {
            'model_page':'',
            'model_attributes':'Developer Profiles','text_paragraph':''})
        html = html + template.render (templatepath+'04ubertext_end.html',{})
        html = html + template.render (templatepath+'05ubertext_links_right.html', {})
        html = html + template.render(templatepath+'06uberfooter.html', {'links': ''})
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', aboutPage)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == '__main__':
    main()  