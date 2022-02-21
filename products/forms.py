from django import forms
from .widgets import CustomClearableFileInput
from .models import Brand, Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False,
                             widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all().order_by('name')
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all().order_by('name')
        b_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = c_friendly_names
        self.fields['brand'].choices = b_friendly_names
        for field_name, field in self.fields.items():
            if field_name != 'image':
                field.widget.attrs['class'] = 'border'
            if field_name == 'category' or field_name == 'brand' or \
                    field_name == 'description':
                field.widget.attrs['class'] = 'py-2'
