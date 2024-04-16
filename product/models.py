from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self) :
        return self.name
    
    class Meta:
        verbose_name='Kategoriya'
        verbose_name_plural='Kategoriyalar'

class Product(models.Model):
    name=models.CharField(max_length=250)
    price=models.PositiveIntegerField(default=0)
    cat=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    about=models.TextField(default='', null=True, blank=True)
    image=models.ImageField(upload_to='product_images/', null=True ,
                            validators=[FileExtensionValidator(allowed_extensions=['jpeg', 'png', 'jpg'])])

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name='Mahsulot'
        verbose_name_plural='Mahsulotlar'