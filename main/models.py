from django.db import models

# Create your models here.
class Tolist(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class User(models.Model):
    Tolist = models.ForeignKey(Tolist, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name
#
# class LoginUser(models.Model):
#     Tolist = models.ForeignKey(Tolist, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name