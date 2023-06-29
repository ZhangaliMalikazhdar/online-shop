from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)
    # sub_category = models.ForeignKey(
    #     'self', on_delete=models.CASCADE,
    #     related_name='sub_categories', null=True, blank=True
    # )
    # is_sub = models.BooleanField(default=False)
    # slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:list-category')

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    description = models.TextField()
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    # slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager:list-product')

    def get_buy_url(self):
        return reverse('shop:product_detail', kwargs={'pk': self.pk})

    # def save(self, *args, **kwargs):
    #     self.pk = slugify(self.name)
    #     return super().save(*args, **kwargs)
