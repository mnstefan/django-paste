from django.conf.urls.defaults import patterns, url
from django.conf import settings

urlpatterns = patterns('',
    url(r'^$', 'dpaste.views.snippet_new', name='snippet_new'),
    url(r'^guess/$', 'dpaste.views.guess_lexer', name='snippet_guess_lexer'),
    url(r'^diff/$', 'dpaste.views.snippet_diff', name='snippet_diff'),
    url(r'^your-latest/$', 'dpaste.views.snippet_userlist', name='snippet_userlist'),
    url(r'^your-settings/$', 'dpaste.views.userprefs', name='snippet_userprefs'),
    
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/$', 'dpaste.views.snippet_details', name='snippet_details'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/delete/$', 'dpaste.views.snippet_delete', name='snippet_delete'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/freedelete/$', 'dpaste.views.snippet_free_delete', name='snippet_free_delete'),
    url(r'^(?P<snippet_id>[a-zA-Z0-9]{4})/raw/$', 'dpaste.views.snippet_details', {'template_name': 'dpaste/snippet_details_raw.html', 'is_raw': True}, name='snippet_details_raw'),
)

#Added urls
urlpatterns += patterns('',
    url(r'^browse/$', 'dpaste.views.browse', name='snippet_browse'),
    url(r'^browse/language/(?P<language>\w+)/$', 'dpaste.views.browse_language', name='snippet_browse_language'),
    url(r'^languages/$', 'dpaste.views.language_list', name='language_list'),
    url(r'^authors/$', 'dpaste.views.author_list', name='author_list'),
)