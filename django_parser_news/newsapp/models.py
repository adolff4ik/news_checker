from django.db import models


class Article(models.Model):
    keyword = models.CharField(max_length=50)
    pubdate = models.DateTimeField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "article"
        verbose_name_plural = "articles"
