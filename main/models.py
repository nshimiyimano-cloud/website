from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)  #here means if they delete user this post will be deleted too in database
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + "\n" + self.description

    # about shopping project models

class Category(models.Model):
    name= models.CharField(max_length= 200, db_index= True)
    slug = models.SlugField(max_length= 200, unique= True)

    class Meta:
        ordering= ('name',)
        verbose_name= 'category'
        verbose_name_plural= 'categories'
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            'main:product_list_by_category',
             args=[self.slug])




class Product(models.Model):
        category= models.ForeignKey(Category,related_name='product',
         on_delete= models.CASCADE )
        name= models.CharField( max_length=200,db_index= True)
        slug= models.SlugField( max_length=200,db_index= True)
        image= models.ImageField(upload_to='products/%Y/%m/%d',blank=True)
        description= models.TextField(blank=True)
        price = models.DecimalField(max_digits=10,decimal_places=2)
        available = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(auto_now=True)


        class Meta:
            ordering= ('name',)
            index_together= (('id','slug'),)
            
        
        def __str__(self):
            return self.name
        
        def get_absolute_url(self):
            return reverse(
                'main:product_detail',
                 args=[self.id,self.slug])




