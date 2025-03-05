from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Product
from shop.models import  Category, Comment
from shop.forms import ProductForm, ProductModelForm, OrderForm, CommentForm
from datetime import datetime



def index(request, category_id: int | None = None):
    search_query = request.GET.get('q', '')
    categories = Category.objects.all()
    if category_id:
        products = Product.objects.filter(category_id=category_id)
    else:
        products = Product.objects.all().order_by('-updated_at') 
    
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(description__icontains=search_query))
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'shop/home.html', context)


def product_detail(request, product_id):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=product_id)
    
    num_comments = Comment.objects.filter(product=product).count() #couunt comments for each product
    
    context = {
        'product': product,
        'categories': categories,
        'num_comments': num_comments
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
        'related_products': related_products
    }
    return render(request, 'shop/product_detail.html', context)



@login_required
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
    return render(request, 'shop/product_create.html', context)





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




@login_required
def product_placing(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = OrderForm(request.POST or None, product_id=product.id) #html da topishi uchun kk boldi
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.user = request.user

            if order.quantity > product.quantity:
                form.add_error('quantity', 'Not enough stock available')
            else:
                product.quantity -= order.quantity
                product.save()
                order.is_placed = True
                order.save()
                return redirect('index')

    else:
        form = OrderForm()  # empty form bo

    return render(request, 'shop/product_detail.html', {'product': product, 'form': form})






# adding def comment  '''fisrys one'''
# @login_required
# def add_comment(request, pk):
#     product =  Product.objects.get(id=pk)
#     form = CommentForm(request.POST)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=product)
#         if form.is_valid():
#             name = request.user.username
#             body = form.cleaned_data['comment']
            
#             c = Comment(product = product, commenter_name=name, comment=body, date_added = datetime.now())
#             c.save()
        
#             return redirect('product_detail')
#         else:
#             print('Form is invalid message from views')
#     else:
#         form = CommentForm()
        
#     context = {
#         'form': form 
#     }
#     return render(request, 'shop/add_comment.html', context)













@login_required
def add_comment(request, pk):
    product = get_object_or_404(Product, id=pk)  
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            name = request.user.username
            body = form.cleaned_data['comment']  

            c = Comment(product=product, commenter_name=name, comment=body, date_added=datetime.now())
            c.save()

            return redirect('product_detail', product_id=pk)  
    else:
        form = CommentForm()

    return render(request, 'shop/add_comment.html', {'form': form})