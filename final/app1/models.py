from django.db import models

# Create your models here.

class voice(models.Model):
    num = models.IntegerField(auto_created=True)
    text = models.CharField(max_length=30000)
    message = models.FileField(upload_to='musics/')

    def file(self):
      return self.message
