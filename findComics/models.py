from django.db import models

class Comic(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=20)
    bookcase = models.CharField(max_length=10)

    def __str__(self):
        return self.title
