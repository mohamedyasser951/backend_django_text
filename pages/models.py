from django.db import models

# Create your models here.

#One To One    

class Female(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Male(models.Model):
    name = models.CharField(max_length=50)
    girl = models.OneToOneField(Female,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
#One To Many

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    def __str__(self):
        return self.product_name

class User(models.Model):
    username = models.CharField(max_length=50,)
    products = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.username

# Maney To Maney

class subject(models.Model):
    subject_name = models.CharField(max_length=50)

    def __str__(self):
        return self.subject_name


class Student(models.Model):
    name = models.CharField(max_length=50)
    subjects = models.ManyToManyField(subject)

    def __str__(self):
        return self.name
    

