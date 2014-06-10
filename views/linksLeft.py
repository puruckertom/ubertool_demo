from django.template.loader import render_to_string
from collections import OrderedDict


# 03ubertext_links_left:
def linksLeft():
    link_dict = OrderedDict([
        ('Terrestrial Models', OrderedDict([
                ('TerrPlant', 'terrplant'),
                ('Agdrift-T-Rex', 'agdrift_trex'),
            ])
        ),
        ('Aquatic Models', OrderedDict([
                ('GENEEC', 'geneec'),
            ])
        ),
        ('Mapping Tools', OrderedDict([
                ('Endangered Species Mapper', 'es_mapping'),
            ])
        ),
    ])

    html = render_to_string('03ubertext_links_left.html', {'link_dict': link_dict})
    return html