from django.db import models
class IOT(models.Model):
    uid=models.IntegerField()
    name=models.CharField(max_length=25,blank=False,null=False)

    def __str__(self):
        return self.name




# Create your models here.
