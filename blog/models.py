from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Entry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    body = models.TextField()
    publication_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
