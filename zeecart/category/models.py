from django.db import models
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name=models.CharField(max_length=50,unique=True,default="")
    slug=models.SlugField(max_length=200,unique=True,default="")
    description=models.TextField(max_length=400,blank=True,default="")
    cat_image=models.ImageField(upload_to='photos/categories',blank=True,default="")

    class Meta:
        verbose_name="Category"
        verbose_name_plural="Categories"

    def get_url(self):
        return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name