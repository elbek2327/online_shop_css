from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Category
from .models import Product
from shop.forms import ProductForm, ProductModelForm



# Create your views here.


def index(request, category_id: int | None = None):
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all().order_by('-updated_at')  # select * from products order by updated_at DESC
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
        'categories': categories
    }
    return render(request, 'shop/product_detail.html', context)



def home(request):
    return render(request, 'shop/home.html')





# def product_list(request):
#     categories = Category.objects.all()
#     context = {'categories': categories}
#     return render(request, 'product_list.html', context)


def related_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    related_products = product.get_related_products() 

    context = {
        'product': product,
        'related_products': related_products,
    }
    return render(request, 'shop/detail.html', context)



@login_required(login_url='/admin/')
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)

            return redirect('index')

    context = {
        'form': form
    }
    return render(request, 'shop/add-product.html', context)





@login_required
def product_update(request,product_id):
    product = get_object_or_404(Product, id= product_id)
    form = ProductModelForm(instance=product)
    if request.method == 'POST':
        form = ProductModelForm(request.POST, request.FILES, instance = product)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
    'form': form,
    'product': product
    }
    return render(request, 'shop/product_update.html', context)
    
    
    
    
    
@login_required
def product_delete(request, product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('index')
    return render(request, 'shop/product_delete.html', {'product': product})