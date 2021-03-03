from django.db import models

# Create your models here.


class movies(models.Model):
    name = models.TextField()
    link = models.TextField()
    source = models.TextField()
    img = models.TextField()
	
     