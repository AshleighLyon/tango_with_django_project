from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# When you define a model, you need to specify the list of fields
# and their types.


class Category(models.Model):
    # Field name is unique (set to true) meaning this field
    # can be used as a primar key.
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    # __str__ generates a string representation of the class
    # similar to a toString() method in java
    def __str__(self):
        return self.title
