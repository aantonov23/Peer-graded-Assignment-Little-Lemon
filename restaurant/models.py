from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    reservation_slot = models.SmallIntegerField(default=10)
    num_of_guests = models.SmallIntegerField(default=2)

    def __str__(self): 
        return self.first_name


# Add code to create Menu model
class Menu(models.Model):
   title = models.CharField(max_length=200) 
   price = models.DecimalField(null=False, max_digits=6, decimal_places=2) 
   menu_item_description = models.TextField(max_length=1000, default='')
   inventory = models.IntegerField(null=True, blank=True) 

   def __str__(self):
      return self.title
   
   def get_item(self):
       return f'{self.title}: {str(self.price)}'