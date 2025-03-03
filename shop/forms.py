from django import forms
from shop.models import Product, Category, Comment
from .models import Order


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=14, decimal_places=2)
    image = forms.ImageField(required=False)
    quantity = forms.IntegerField(required=False)
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    discount = forms.IntegerField(required=False, min_value=0, max_value=100)
    rating = forms.ChoiceField(choices=Product.RatingChoice)
    
    def save(self, commit=True):
        cd = self.cleaned_data
        product = None
        if commit:
            product = Product.objects.create(
                name=cd.get('name'),
                description=cd.get('description'),
                price=cd.get('price'),
                image=cd.get('image'),
                quantity=cd.get('quantity'),
                category=cd.get('category'),
                discount=cd.get('discount'),
                rating=cd.get('rating')
            )
        return product
        


class ProductModelForm(forms.ModelForm):
    
    class Meta:
        model = Product
        # fields = ['name', 'description', 'price', 'image', 'quantity', 'category', 'discount', 'rating']
        exclude = ()
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Your name"}),
            'surname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Your surname"}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Your phone"}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': "Quantity"})
        }
        
        
        
        
    def clean_quantity(self):
        quantity = self.cleaned_data['quantity']
        product_id = self.initial.get('product_id')
        product = Product.objects.get(id=product_id)

        if quantity > product.quantity:
            raise forms.ValidationError("Not enough stock available.")
        return quantity
    




# added new
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commenter_name', 'comment')
        widgets = {
            'commenter_name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'}),
        }

