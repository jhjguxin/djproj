from django.conf.urls.defaults import *
from django.views.generic import list_detail
from djproj.ttapp.models import Publisher, Book
from mysite.feeds import LatestEntries, LatestEntriesByCategory

feeds = {
    'latest': LatestEntries,
    'categories': LatestEntriesByCategory,
}

def get_books():
    return Book.objects.all()

apress_books = {
    'queryset': Book.objects.filter(publisher__name='apress'),
    'template_name': 'books/apress_list.html',
    'template_object_name': 'book',
}
    
publisher_info = {
    'queryset': Publisher.objects.all(),
    'template_name': 'publisher_list.html',
    'template_object_name': 'publisher',
    'extra_context': {'book_list': get_books},
}

urlpatterns = patterns('',
    (r'publishers/$', list_detail.object_list, publisher_info),
    (r'books/apress/$', list_detail.object_list, apress_books),
    (r'feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

