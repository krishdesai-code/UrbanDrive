from django.db import models

class CarCategory(models.Model) :
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.id
    

class Car(models.Model) :

    FULE_TYPE_CHOICE =[
        ('P','Petrol'),
        ('D','Diesel'),
        ('E','Ev')
    ]

    id = models.AutoField(primary_key=True)

    brand = models.CharField(max_length=50)

    name = models.CharField(max_length=50)

    category = models.ForeignKey(CarCategory,on_delete=models.CASCADE)

    year = models.PositiveIntegerField()

    fule_type = models.CharField(max_length=1,choices=FULE_TYPE_CHOICE)

    Average = models.IntegerField()

    km = models.DecimalField(max_digits=7,decimal_places=2)

    rent = models.DecimalField(max_digits=10,decimal_places=2)

    is_avail = models.BooleanField(default=False)

    def __str__(self):
        return self.name
