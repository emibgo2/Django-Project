from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')
    body  = models.TextField()

    def __str__(self):
        return  self.title

    def summery(self):
        return self.body[:100]