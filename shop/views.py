# from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'shop/index.html')


def analytics(request):
    return render(request, 'shop/dashboard/analytics.html')

def crm(request):
    return render(request, 'shop/dashboard/crm.html')

def e_commerce(request):
    return render(request, 'shop/dashboard/e-commerce.html')

def project_management(request):
    return render(request, 'shop/dashboard/project-management.html')

def saas(request):
    return render(request, 'shop/dashboard/saas.html')
def calendar_view(request):
    return render(request, 'shop/app/calendar.html')

# Chat Views
def chat_view(request):
    return render(request, 'shop/app/chat.html')

# Email Views
def inbox_view(request):
    return render(request, 'shop/app/email/inbox.html')

def email_detail_view(request):
    return render(request, 'shop/app/email/email-detail.html')

def compose_email_view(request):
    return render(request, 'shop/app/email/compose.html')

# Events Views
def create_event_view(request):
    return render(request, 'shop/app/events/create-an-event.html')

def event_detail_view(request):
    return render(request, 'shop/app/events/event-detail.html')

def event_list_view(request):
    return render(request, 'shop/app/events/event-list.html')

# Kanban Views
def kanban_view(request):
    return render(request, 'shop/app/kanban.html')

# Social Views
def social_feed_view(request):
    return render(request, 'shop/app/social/feed.html')

def social_activity_log_view(request):
    return render(request, 'shop/app/social/activity-log.html')

def social_notifications_view(request):
    return render(request, 'shop/app/social/notifications.html')

def social_followers_view(request):
    return render(request, 'shop/app/social/followers.html')

# e-commerce Views

def order_list(request):
    return render(request, 'shop/app/e-commerce/orders/order-list.html')

def order_details(request):
    return render(request, 'shop/app/e-commerce/orders/order-details.html')

def product_list(request):
    return render(request, 'shop/app/e-commerce/product/product-list.html')

def product_grid(request):
    return render(request, 'shop/app/e-commerce/product/product-grid.html')

def product_details(request):
    return render(request, 'shop/app/e-commerce/product/product-details.html')

def billing(request):
    return render(request, 'shop/app/e-commerce/billing.html')

def checkout(request):
    return render(request, 'shop/app/e-commerce/checkout.html')

def customer_details(request):
    return render(request, 'shop/app/e-commerce/customer-details.html')

def customers(request):
    return render(request, 'shop/app/e-commerce/customers.html')

def invoice(request):
    return render(request, 'shop/app/e-commerce/invoice.html')

def shopping_cart(request):
    return render(request, 'shop/app/e-commerce/shopping-cart.html')

def social_followers(request):
    return render(request, 'shop/app/social/followers.html') # Ensure correct template path

# pages/views.py
from django.shortcuts import render

def starter(request):
    return render(request, 'shop/pages/starter.html')

def landing(request):
    return render(request, 'shop/pages/landing.html')

def simple_login(request):
    return render(request, 'shop/pages/authentication/simple/login.html')

def simple_logout(request):
    return render(request, 'shop/pages/authentication/simple/logout.html')

def simple_register(request):
    return render(request, 'shop/pages/authentication/simple/register.html')

def simple_forgot_password(request):
    return render(request, 'shop/pages/authentication/simple/forgot-password.html')

def simple_confirm_mail(request):
    return render(request, 'shop/pages/authentication/simple/confirm-mail.html')

def simple_reset_password(request):
    return render(request, 'shop/pages/authentication/simple/reset-password.html')

def simple_lock_screen(request):
    return render(request, 'shop/pages/authentication/simple/lock-screen.html')

def authentication_wizard(request):
    return render(request, 'shop/pages/authentication/wizard.html')

def user_profile(request):
    return render(request, 'shop/pages/user/profile.html')

def user_settings(request):
    return render(request, 'shop/pages/user/settings.html')

def error_404(request):
    return render(request, 'shop/pages/errors/404.html')

def error_500(request):
    return render(request, 'shop/pages/errors/500.html')

def widgets(request):
    return render(request, 'shop/widgets.html')

# dashboard/views.py
from django.shortcuts import render



# app/views.py
from django.shortcuts import render

def event_detail(request):
    return render(request, 'shop/app/events/event-detail.html')

def e_commerce_customers(request):
    return render(request, 'shop/app/e-commerce/customers.html')