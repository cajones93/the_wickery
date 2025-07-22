from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)
        widgets = {
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]{11}',
                                            'title': 'Please enter an 11-digit phone number (e.g., 07123456789)'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        self.fields['phone_number'].widget.attrs['type'] = 'tel'
        for field_name, field_object in self.fields.items():
            if field_name == 'country':
                field_object.widget.attrs['aria-label'] = 'Country'
            else:
                if field_object.required:
                    placeholder = f'{placeholders[field_name]} *'
                else:
                    placeholder = placeholders[field_name]
                field_object.widget.attrs['placeholder'] = placeholder
                field_object.widget.attrs['aria-label'] = placeholder

            field_object.widget.attrs['class'] = 'stripe-style-input'
            field_object.label = False
