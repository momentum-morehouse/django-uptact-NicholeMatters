from django import forms
from .models import Contact
import datetime


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
            'note'
        ]

        widgets = {
        'birthday': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
         
class DateForm(forms.Form):
   day = forms.DateField(initial=datetime.date.today)
print(DateForm())       
        

#class Note(forms.Form):
   #Contact = forms.ForeignKey(ContactForm, on_delete= forms.CASCADE)
