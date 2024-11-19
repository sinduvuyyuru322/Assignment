from django.db import models

# Create your models here.
class product_details(models.Model):
    name = models.CharField(max_length=100)
    #product_id = models.TextField(max_length=10)
    price = models.IntegerField(default=0)
    quantity_in_stock = models.IntegerField(default = 0) 
    def __str__(self):
        return self.name

class customer_details(models.Model):
    name = models.CharField(max_length=100)
    #customer_id= models.IntegerField(default=0)
    product_phoneno = models.IntegerField(default=0)
    def __str__(self):           
        return self.name
   
class Order(models.Model):
    customer = models.ForeignKey(customer_details, on_delete=models.CASCADE)
    product = models.ForeignKey(product_details, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    quantity_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order by {self.customer.name} for {self.product.name}"