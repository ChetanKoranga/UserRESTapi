from django.db import models

# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    age = models.IntegerField(default=18)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    web = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id) + ". " + self.first_name +" "+ self.last_name