from django.db import models
from Users.models import Users


class CarCategory(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class Car(models.Model) :

    FUEL_TYPE_CHOICES =[
        ('P','Petrol'),
        ('D','Diesel'),
        ('C','CNG'),
        ('E','Ev')
    ]

    GEAR_TYPE = [
        ('A','Automatic'),
        ('M','Manual'),
        ('I','IMT'),
    ]

    id = models.AutoField(primary_key=True)

    brand = models.CharField(max_length=50)

    name = models.CharField(max_length=50)

    category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)

    year = models.PositiveIntegerField()

    fuel_type = models.CharField(max_length=1,choices=FUEL_TYPE_CHOICES)

    gear_type = models.CharField(max_length=1,choices=GEAR_TYPE)

    average = models.PositiveIntegerField()

    Seat = models.PositiveIntegerField()

    rent = models.DecimalField(max_digits=10,decimal_places=2)

    is_avail = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.brand} {self.name}"

class CarImages(models.Model):

    car_id = models.ForeignKey(Car,on_delete=models.CASCADE,related_name='images')
    img = models.ImageField(upload_to='car_images')

    def __str__(self):
        return f"Image for {self.car.name}"

class CarRating(models.Model) :

    RATING_CHOICES = [
        (1,'1 Star'),
        (2,'2 Star'),
        (3,'3 Star'),
        (4,'4 Star'),
        (5,'5 Star')
    ]

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users,on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car,on_delete=models.CASCADE)

    rating = models.IntegerField(choices=RATING_CHOICES)

    comment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.rating} - {self.car_id}"


class Booking(models.Model):
    id = models.CharField(unique=True,primary_key=True)
    user = models.ForeignKey(Users,on_delete=models.CASCADE)
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    aadhar = models.CharField(max_length=12)
    aadhar_dob = models.DateField(null=True,blank=True)
    licence = models.CharField(max_length=20)
    licence_exp = models.DateField(null=True,blank=True)
    mobile_no = models.CharField(max_length=10)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)
    rent = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.id