from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    photo = models.ImageField(upload_to='person_portfolio/image_portfolio')
    url = models.URLField(blank=True)
    
    def __str__(self):
        return self.title
    
    