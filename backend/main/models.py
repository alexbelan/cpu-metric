from django.db import models


# Create your models here.
class CPUMetric(models.Model):
    id = models.AutoField(unique=True, primary_key=True)
    data = models.CharField(max_length=10)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.date)