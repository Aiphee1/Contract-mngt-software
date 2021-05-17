from django.db import models

# Create your models here.
class Currency(models.Model):
    order_currency = models.CharField(max_length=50) 
    def __str__(self):
        return self.order_currency
    
class sorecords(models.Model):
   
    order_desc = models.CharField(max_length=250)
    order_to = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50) 
    order_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    validity_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    order_value = models.CharField(max_length=20)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,null=True)
    remarks = models.CharField(max_length=10)  
    
    
    
def __str__(self):
    return self.order_desc