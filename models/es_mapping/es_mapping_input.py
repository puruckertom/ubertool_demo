from django.template.loader import render_to_string
 
 
def es_mappingInputPage(request, model='', header=''):
    import es_mapping_parameters
 
    html = render_to_string('04uberinput_jquery.html', { 'model': model })
    html = html + render_to_string('04uberinput_start.html', {
            'model':model,
            'model_attributes': header+' Inputs'})
    html = html + str(es_mapping_parameters.esInp())
    html = html + render_to_string('04uberinput_end.html', {'sub_title': 'Submit'})
    # Check if tooltips dictionary exists
    try:
        import agdrift_trex_tooltips
        hasattr(agdrift_trex_tooltips, 'tooltips')
        tooltips = agdrift_trex_tooltips.tooltips
    except:
        tooltips = {}
    html = html + render_to_string('05ubertext_tooltips_right.html', {'tooltips':tooltips})

    return html