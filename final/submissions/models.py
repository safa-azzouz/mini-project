from django.db import models

# Create your models here.

class submissions(models.Model):

    num = models.IntegerField(auto_created=True)
    text = models.CharField(max_length=200)
    message = models.FileField()

    def file(self):
      return self.message
