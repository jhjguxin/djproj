from django.conf.urls.defaults import *
from django.contrib.syndication.feeds import Feed
from djproj.blog.models import Entry

class LatestEntries(Feed):
    title = "My Blog"
    link = "/archive/"
    description = "The latest news about stuff."

    def items(self):
        return Entry.objects.order_by('-pub_date')[:5]

     
feeds = {
    'latest': LatestEntries,
    # 'categories': LatestEntriesByCategory,
}

urlpatterns = patterns('',
    (r'feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)