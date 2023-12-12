from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.utils import timezone
import os



# Define the User model (if not already defined)
# class User(models.Model):
#     # Define user fields

class Category(models.Model):
    category = models.CharField(max_length=20, default="легковые")

    def __str__(self):
        return self.category

def car_image_path(instance, filename):
    # Get the car's name from the instance
    car_name = instance.car_name

    # Split the file extension from the original filename
    _, ext = os.path.splitext(filename)

    # Generate a unique filename based on the car's name and the current timestamp
    unique_filename = f"{car_name}_{timezone.now().strftime('%Y%m%d%H%M%S')}{ext}"

    # Return the final path for the uploaded image
    return os.path.join('car_images', unique_filename)
# Define the Car model
class CarAnnouncement(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign Key to User model
    name_car = models.CharField(max_length=50)
    image = models.ImageField(upload_to='car_images/')  # For storing one or more images
    price_usd = models.DecimalField(max_digits=15, decimal_places=2)  # Price in USD
    price_soms = models.DecimalField(max_digits=15, decimal_places=2)  # Price in SOM
    year = models.PositiveIntegerField()  # Year of manufacture
    mileage = models.PositiveIntegerField()  # Mileage in km
    body_type = models.CharField(max_length=50, )  # Body type тип кузова
    color = models.CharField(max_length=7, )  # Color in HTML color code format
    engine = models.CharField(max_length=20)  # Engine description
    transmission = models.CharField(max_length=20)  # Transmission type
    drive = models.CharField(max_length=20)  # Drive type привод
    steering_left = models.BooleanField(default="слева")  # Steering position           TO DO
    condition = models.CharField(max_length=20, )  # Condition
    customs_clearance = models.BooleanField(default=True)  # Is the car customs cleared?
    exchange_offer = models.BooleanField(default=False)  # Is exchange offered?
    availability = models.BooleanField(default=True)  # Is the car available?
    region_city = models.CharField(max_length=100, default="Бишкек")  # Region/City of sale
    country = models.CharField(max_length=100, default="Кыргызстан")  # Country where the car is registered

    # Define the Category model (if not already defined)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Foreign Key to Category model

    def __str__(self):
        return self.name_car


    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{}</span>',
            self.color,
        )
    # пока еще не решил зачем этот код но он был в на stackoverflow
    # для того чтобы выводить цвет машины через html
    # class CarAdmin(admin.ModelAdmin):
    #     list_display = ('name_car', 'color', 'colored_name')