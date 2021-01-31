from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ("name",)
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"

    def __str__(self):
        return f"{self.name}"


class Tag(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Etykieta"
        verbose_name_plural = "Etykiety"

    def __str__(self):
        return f"{self.name}"


class Entry(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)  # editable=False we frontendzie sie tego nie bedzie pokazywac (ale trzeba skasowac w adminie z fields i list_display
    body = models.TextField()
    publication_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-category",)
        verbose_name = "Wpis"
        verbose_name_plural = "Wpisy"

    def __str__(self):
        return f"{self.title}"
