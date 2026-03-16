from django.db import models

class Admin_login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.email