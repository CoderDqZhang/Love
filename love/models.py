from django.db import models

# Create your models here.
# Create your models here.
class Love(models.Model):
    girl_name = models.CharField(max_length=255, null=True, blank=True)
    boy_name= models.CharField(max_length=255, null=True, blank=True)
    girl_age = models.IntegerField(default=0)
    boy_age = models.IntegerField(default=0)
    love_startTime = models.DateTimeField()