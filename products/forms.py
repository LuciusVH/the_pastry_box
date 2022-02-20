from django import forms
from .models import Brand, Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all()
        b_friendly_names = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = b_friendly_names
        self.fields['brand'].choices = c_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border'
