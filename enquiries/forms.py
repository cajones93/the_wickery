from django import forms
from .models import Enquiry


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'message_type', 'order_number', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name *'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email *'
        self.fields['subject'].widget.attrs['placeholder'] = 'Subject (Optional)'
        self.fields['order_number'].widget.attrs['placeholder'] = 'Order Number (Optional)'
        self.fields['message'].widget.attrs['placeholder'] = 'Your Message *'
        for field in self.fields:
            if field != 'message_type':
                self.fields[field].widget.attrs['class'] = 'form-control'
            self.fields[field].label = False

        self.fields['message_type'].label = "Type of Enquiry:"
        self.fields['message_type'].widget.attrs['class'] = 'form-control'
