from django.db import models

# Create your models here.
class Born(models.Model):
    def __str__(self):
        return self.name
    id = models.IntegerField(primary_key=True)
    huml = models.FloatField()
    humw = models.FloatField()
    ulnal = models.FloatField()
    ulnaw = models.FloatField()
    feml = models.FloatField()
    femw = models.FloatField()
    tibl = models.FloatField()
    tibw = models.FloatField()
    tarl = models.FloatField()
    tarw = models.FloatField()
    type = models.CharField(max_length = 15)

