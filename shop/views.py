from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from shop.models import Product, Category
from .models import Product



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

    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/detail.html', context)



def home(request):
    return render(request, 'shop/home.html')

def popular_products(request):
    products = Product.objects.order_by('-rating')[:12]
    return render(request, 'shop/popular_products.html', {'products': products})

def new_arrivals(request):
    products = Product.objects.order_by('-updated_at')[:12]
    return render(request, 'shop/new_arrivals.html', {'products': products})



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