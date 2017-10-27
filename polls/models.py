from django.db import models


# Create your models here.
class Excercise (models.Model):
    application = models.CharField (max_length=255, null=False)

    def __str__(self):
        return "".join(self.application)
