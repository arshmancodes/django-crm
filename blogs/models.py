from django.db import models

class Blogs(models.Model):
    title       = models.TextField()
    description = models.TextField()
    image_url   = models.TextField()
