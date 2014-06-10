#  https://docs.djangoproject.com/en/1.6/intro/tutorial03/
from django.conf.urls import patterns, include, url
# from django.contrib import admin
# admin.autodiscover()


# All view functions here must be in '/views/views.py'
urlpatterns = patterns('views',
    (r'^$', 'landing.ecoLandingPage'),
    (r'^eco/?$', 'landing.ecoLandingPage'),
    (r'^eco/(?P<model>.*?)/description/?$', 'description.descriptionPage'),
    (r'^eco/(?P<model>.*?)/input/?$', 'input.inputPage'),
    (r'^eco/(?P<model>.*?)/output/?$', 'output.outputPage'),
    (r'^eco/(?P<model>.*?)/algorithms/?$', 'algorithms.algorithmPage'),
    (r'^eco/(?P<model>.*?)/references/?$', 'references.referencesPage'),
    (r'^eco/(?P<model>.*?)/batchinput/?$', 'batch.batchInputPage'),
    (r'^eco/(?P<model>.*?)/batchoutput/?$', 'batch.batchOutputPage'),
    (r'^eco/(?P<model>.*?)/qaqc/?$', 'qaqc.qaqcPage'),
    (r'^eco/(?P<model>.*?)/history/?$', 'history.historyPage'),
    (r'^eco/.*?/history_revisit\.html$', 'history.historyPageRevist'),
    (r'^eco/(?P<model>.*?)/?$', 'description.descriptionPage'),
    # url(r'^admin/', include(admin.site.urls)),
)

# 404 Error view (file not found)
handler404 = 'views.misc.fileNotFound'
# 500 Error view (server error)
handler500 = 'views.misc.fileNotFound'
# 403 Error view (forbidden)
handler403 = 'views.misc.fileNotFound'

