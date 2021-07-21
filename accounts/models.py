from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
	user=models.OneToOneField(User,blank=True,null=True,on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	profile_pic=models.ImageField(default='blog1.jpg' , null=True,blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		if self.name is not None:
			return self.name
		else:
			return "Default"

	#@property
	def get_photo_url(self):
		if self.profile_pic and hasattr(self.profile_pic, 'url'):
			return self.profile_pic.url
		else:
			return "/static/images/blog1.jpg"


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)

	def __str__(self):
		return self.product.name