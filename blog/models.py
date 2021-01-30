from django.db import models

# Create your models here.
class Category(models.Model):



class Entry(models.Model):
    category= models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    body = models.TextField()
    publication_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


