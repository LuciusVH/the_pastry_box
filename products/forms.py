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
        # placeholders = {
        #     'category': 'Category',
        #     'name': 'Name',
        #     'brand': 'Brand',
        #     'sku': 'SKU',
        #     'description': 'Description',
        #     'price': 'Price',
        #     'image_url': 'image_url',
        #     'image': 'Image import',
        # }

        self.fields['category'].choices = b_friendly_names
        self.fields['brand'].choices = c_friendly_names
        for field_name, field in self.fields.items():
            if field_name != 'image':
                field.widget.attrs['class'] = 'border'
        # for field in self.fields:
            # if field != 'category' or field != 'brand':
            #     if self.fields[field].required:
            #         placeholder = f'{placeholders[field]} *'
            #     else:
            #         placeholder = placeholders[field]
            # self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].label = False
