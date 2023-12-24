from django.db import models

# Create your models here.
class Car(models.Model):
    name_of_car = models.CharField(max_length=255)
    # dollar_price = models.DecimalField(max_digits=10, decimal_places=2)
    # som_price = models.DecimalField(max_digits=10, decimal_places=2)
    Year_of_Manufacture = models.PositiveIntegerField()
    Mileage = models.PositiveIntegerField()
    Body_Type = models.CharField(max_length=255)
    Color = models.CharField(max_length=255)
    Transmission = models.CharField(max_length=255)
    Drive = models.CharField(max_length=255)
    Steering = models.CharField(max_length=255)
    Condition = models.CharField(max_length=255)
    Customs = models.CharField(max_length=255)
    Availability = models.CharField(max_length=255)
    Region_City_of_Sale = models.CharField(max_length=255)
    Registration = models.CharField(max_length=255)
    Engine_volume = models.DecimalField(max_digits=5, decimal_places=2)
    Engine_fuel_type = models.CharField(max_length=255)
    Car_make = models.CharField(max_length=255)
    Door_num = models.PositiveIntegerField()

    def __str__(self):
        return self.name_of_car