from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Theme(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField(blank=True)
    link = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey(to=Category, on_delete=models.PROTECT, default=1)

    def __str__(self):
        return self.title
