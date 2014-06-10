from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
 
@require_POST
def es_mappingOutputPage(request):
    import es_mapping_model,es_mapping_tables

    args={}
    for key in request.POST:
        args[key] = request.POST.get(key)
    es_obj = es_mapping_model.es_mapping(args)
    import logging

    html = es_mapping_tables.table_all(es_obj)

    return html, es_obj