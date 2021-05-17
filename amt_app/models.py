from django.db import models

# Create your models here.
class Currency(models.Model):
    order_currency = models.CharField(max_length=50) 
    def __str__(self):
        return self.order_currency
    
class amtrecords(models.Model):
   
    contract_desc = models.CharField(max_length=250)
    contractor = models.CharField(max_length=100)
    listing_no = models.CharField(max_length=50) 
    amt_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    contract_value = models.CharField(max_length=20)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE,null=True)
    remarks = models.CharField(max_length=10)  
    
    
    
def __str__(self):
    return self.contract_desc