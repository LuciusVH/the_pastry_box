from django import forms
from .models import Brand, Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all().order_by('name')
        c_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all().order_by('name')
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

        self.fields['category'].choices = c_friendly_names
        self.fields['brand'].choices = b_friendly_names
        for field_name, field in self.fields.items():
            if field_name != 'image':
                field.widget.attrs['class'] = 'border'
            if field_name == 'category' or field_name == 'brand' or \
                    field_name == 'description':
                field.widget.attrs['class'] = 'py-2'
        # for field in self.fields:
            # if field != 'category' or field != 'brand':
            #     if self.fields[field].required:
            #         placeholder = f'{placeholders[field]} *'
            #     else:
            #         placeholder = placeholders[field]
            # self.fields[field].widget.attrs['placeholder'] = placeholder
            # self.fields[field].label = False
