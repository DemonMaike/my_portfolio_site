from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=15)
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title
    