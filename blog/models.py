from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100]

    def short_time(self):
        return self.pub_date.strftime('%b %e %Y')
