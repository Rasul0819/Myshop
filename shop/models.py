from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class Brand(models.Model):
    brandname = models.CharField(max_length=125,
                                 verbose_name='Brand:')
    def __str__(self):
        return self.brandname
    
class Category(models.Model):
    category = models.CharField(max_length=125,
                                verbose_name='Category:')

    def __str__(self):
        return self.category
    
    

    



class Product(models.Model):
    product = models.CharField(max_length=125,
                               verbose_name='Product:')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Description:')
    price = models.DecimalField(max_digits=10,
                                decimal_places=2,
                                verbose_name='Price:')
    characteristcs = models.TextField(verbose_name="Characteristircs:",
                                      blank=True,null=True)
    available = models.BooleanField(verbose_name='Available:',
                                    default=True
                                    )
    
    main_image = models.ImageField(upload_to='static/images/products/',
                                   help_text='En glavni suwret qoyin tovarga:'
                                   )
    image2 = models.ImageField(upload_to='static/images/products/',
                               help_text='Bul ekinshi suwret:',
                               blank=True,null=True)
    image3 = models.ImageField(upload_to='static/images/products/',
                               help_text='Bul ushinshi suwret:',
                               blank=True,null=True
                               )
    image4 = models.ImageField(upload_to='static/images/products/',
                               help_text='Bul tortinshi suwret:',
                               blank=True,null=True
                               )
class Reviews(models.Model):
    comment = models.TextField(verbose_name='Comment:',blank=True,null=True)
    photo = models.ImageField(upload_to='media/images/reviews/',blank=True,null=True)
    photo2 = models.ImageField(upload_to='media/images/reviews/',blank=True,null=True)
    photo3 = models.ImageField(upload_to='media/images/reviews/',blank=True,null=True)
    starts = models.PositiveSmallIntegerField(
        verbose_name='Rating (Stars):',
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1,blank=True,null=True
    )
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'review for {self.product} - {self.starts} stars'
    
# class Saleoff(models.Model):
#     sale = models.PositiveIntegerField(verbose_name='Saleoff:')
#     products_price = models.ForeignKey(Product,on_delete=models.CASCADE)

#     def __str__(self):
#         return self.sale
