from haystack import indexes
from .models import CarAnnouncement


class CarAnnouncementIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return CarAnnouncement

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
