from django.db import models


# Create your models here.
class Location(models.Model):

    '''
    locations model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
       return self.location
       
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):

    '''
    Photo category model
    '''
    
    image_category = models.CharField(max_length=120)

    def __str__(self):
       return self.image_category
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Image(models.Model):

    '''
    Images model
    '''
    
    image_path = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=200, blank=True)
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location, blank=True)

    def __str__(self):
       return self.image_name
    

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    @classmethod
    def get_all(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__image_category__icontains = search_category)
        return images

    @classmethod
    def filter_by_location(cls):
        images = cls.objects.order_by('category')
        return images