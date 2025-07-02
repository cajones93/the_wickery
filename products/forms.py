from django import forms
from .models import Product, Category, Scent, CandleSize, WaxType


class ProductForm(forms.ModelForm):

    available_scents = forms.ModelMultipleChoiceField(
        queryset=Scent.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    available_sizes = forms.ModelMultipleChoiceField(
        queryset=CandleSize.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    available_wax_types = forms.ModelMultipleChoiceField(
        queryset=WaxType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
    
    has_scents = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False,
        label="Has Scents?"
    )
    has_sizes = forms.BooleanField(
        widget=forms.CheckboxInput,
        required=False,
        label="Has Sizes?"
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'sku',
            'description',
            'price',
            'rating',
            'image',
            'image_url',
            'category',
            'has_scents',
            'available_scents',
            'has_sizes',
            'available_sizes',
            'available_wax_types',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # get objects
        categories = Category.objects.all()
        available_wax_types = WaxType.objects.all()
        available_sizes = CandleSize.objects.all()
        available_scents = Scent.objects.all()
        
        # get friendly names
        cat_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        wax_friendly_names = [(w.id, w.get_friendly_name()) for w in available_wax_types]
        size_friendly_names = [(si.id, si.get_friendly_name()) for si in available_sizes]
        scent_friendly_names = [(sc.id, sc.get_friendly_name()) for sc in available_scents]

        # set friendly names
        self.fields['category'].choices = cat_friendly_names
        self.fields['available_wax_types'].choices = wax_friendly_names
        self.fields['available_sizes'].choices = size_friendly_names
        self.fields['available_scents'].choices = scent_friendly_names
        
            
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
