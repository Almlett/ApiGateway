from django.db import models

class Status(models.Model):
    name = models.CharField(max_length=32)
    

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name