from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

def algorithmPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    header = viewmodule.header

    text_file1 = open('models/'+model+'/'+model+'_algorithm.txt','r')
    x = text_file1.read()
    html = render_to_string('01uberheader.html', {'title': header+' Algorithms'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'algorithm'})
    html = html + linksLeft.linksLeft()
    html = html + render_to_string('04uberalgorithm_start.html', {
            'model_attributes': header+' Algorithms', 
            'text_paragraph':x})
    html = html + render_to_string('04ubertext_end.html', {})
    html = html + render_to_string('05ubertext_links_right.html', {})
    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response