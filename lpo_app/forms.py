
from bootstrap_datepicker.widgets import DatePicker
from django import forms
from .models import lporecords

class Lpoform(forms.ModelForm):
    
    class Meta:
        model = lporecords
        fields = '__all__'
        labels = {
            'order_desc':'Order Description',
            'order_to':'Vendor',
            'order_no':'Order Number',
            'order_value':'Order Value',         
            }
        
    def __init__(self, *args, **kwargs):
        super(Lpoform,self).__init__(*args, **kwargs)
        self.fields['currency'].empty_label = 'Select Currency'
        self.fields['currency'].required = True
        self.fields['order_date'].required = True
        self.fields['validity_date'].required = True
        