from django.db import models


class PortfolioGroup(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class PortfolioItem(models.Model):
    slug = models.SlugField()
    group = models.ForeignKey(PortfolioGroup, on_delete=models.RESTRICT)
    name = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    date = models.DateField()
    description = models.TextField()
    images = models.ManyToManyField('Image')
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    image = models.OneToOneField('Image', on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title


class Image(models.Model):
    path = models.CharField(max_length=200)
    alt_text = models.TextField()

    def __str__(self):
        return self.path


class Tag(models.Model):
    tag = models.CharField(max_length=64)

    def __str__(self):
        return self.tag
