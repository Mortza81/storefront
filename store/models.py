from django.db import models
class Collection(models.Model):
    title=models.CharField(max_length=255,unique=True)
class Product(models.Model):
    title=models.CharField(max_length=255)
    inventory=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    description=models.TextField()
    collection=models.ForeignKey(Collection,on_delete=models.CASCADE)
    last_update=models.DateTimeField(auto_now=True)
class Customer(models.Model):
    MEMBERSHIP_VALUES=[
        ('B','bronze'),
        ('S','silver'),
        ('G','gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255,unique=True)
    phone_number = models.CharField(max_length=25)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,choices=MEMBERSHIP_VALUES,default='b')
class Order(models.Model):
    STATUS_VALUES=[
        ('P','pending'),
        ('C','Complete'),
        ('F','failed'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=STATUS_VALUES,default='P')
    products=models.ManyToManyField(Product,through='OrderProduct')
    # protect prevent deleting the child records if parent record deleted
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)
class OrderProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    quantity=models.PositiveIntegerField()
    unit_price=models.PositiveIntegerField()
class Address(models.Model):
    city=models.CharField(max_length=255)
    street=models.CharField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)
class Cart(models.Model):
    user=models.OneToOneField(Customer,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    products=models.ManyToManyField(Product)
# There is two way for implementing many to many relationships:
# One is to use association class, in this method you go to one of the models and use models.ManyToManyField
# The other one is you implement the rel table as an independent entity and make a one to many rel with each entity
