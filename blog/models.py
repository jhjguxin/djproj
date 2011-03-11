from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    categories  = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    pub_date = models.DateField()
    
    def get_absolute_url(self):
        return "/blog/%i/" % self.id    
  