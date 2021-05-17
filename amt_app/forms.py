from bootstrap_datepicker.widgets import DatePicker
from django import forms
from .models import amtrecords

class Amtform(forms.ModelForm):
    
    class Meta:
        model = amtrecords
        fields = '__all__'
        labels = {
            'contract_desc':'Contract Description',
            'contractor':'Vendor',
            'listing_no':'Extract Number',
            'order_value':'Order Value',  
            'contract_value': 'Amount',            
            'remarks': 'Decision',                
            }
        
    def __init__(self, *args, **kwargs):
        super(Amtform,self).__init__(*args, **kwargs)
        self.fields['currency'].empty_label = 'Select Currency'
        
        
