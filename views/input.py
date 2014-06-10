from django.template.loader import render_to_string
from django.http import HttpResponse
import importlib
import linksLeft

def inputPage(request, model='none', header='none'):
    viewmodule = importlib.import_module('.views', 'models.'+model)
    inputmodule = importlib.import_module('.'+model+'_input', 'models.'+model)
    header = viewmodule.header

    html = render_to_string('01uberheader.html', {'title': header+' Inputs'})
    html = html + render_to_string('02uberintroblock_wmodellinks.html', {'model':model,'page':'input'})
    html = html + linksLeft.linksLeft()

    inputPageFunc = getattr(inputmodule, model+'InputPage')  # function name = 'model'InputPage  (e.g. 'sipInputPage')
    html = html + inputPageFunc(request, model, header)

    html = html + render_to_string('06uberfooter.html', {'links': ''})
    
    response = HttpResponse()
    response.write(html)
    return response