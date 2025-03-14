# from django.contrib import admin
from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('dashboard/analytics/', views.analytics, name='dashboard_analytics'),
    path('dashboard/crm/', views.crm, name='dashboard_crm'),
    path('dashboard/e-commerce/', views.e_commerce, name='dashboard_e_commerce'),
    path('dashboard/project-management/', views.project_management, name='dashboard_project_management'),
    path('dashboard/saas/', views.saas, name='dashboard_saas'),
# Calendar
    path('app/calendar/', views.calendar_view, name='calendar'),

    # Chat
    path('app/chat/', views.chat_view, name='chat'),

    # Email
    path('app/email/inbox/', views.inbox_view, name='email_inbox'),
    path('app/email/email-detail/', views.email_detail_view, name='email_detail'),
    path('app/email/compose/', views.compose_email_view, name='compose_email'),

    # Events
    path('app/events/create-an-event/', views.create_event_view, name='create_event'),
    path('app/events/event-detail/', views.event_detail_view, name='event_detail'),
    path('app/events/event-list/', views.event_list_view, name='event_list'),

    # Kanban
    path('app/kanban/', views.kanban_view, name='kanban'),

    # Social
    path('app/social/feed/', views.social_feed_view, name='social_feed'),
    path('app/social/activity-log/', views.social_activity_log_view, name='social_activity_log'),
    path('app/social/notifications/', views.social_notifications_view, name='social_notifications'),
    path('app/social/followers/', views.social_followers_view, name='social_followers'),

#     e commerce
path('orders/', views.order_list, name='order-list'),
    path('orders/details/', views.order_details, name='order-details'),
    path('products/list/', views.product_list, name='product-list'),
    path('products/grid/', views.product_grid, name='product-grid'),
    path('products/details/', views.product_details, name='product-details'),
    path('billing/', views.billing, name='billing'),
    path('checkout/', views.checkout, name='checkout'),
    path('customer-details/', views.customer_details, name='customer-details'),
    path('customers/', views.customers, name='customers'),
    path('invoice/', views.invoice, name='invoice'),
    path('shopping-cart/', views.shopping_cart, name='shopping-cart'),
path('starter/', views.starter, name='starter'),
    path('landing/', views.landing, name='landing'),
    path('authentication/simple/login/', views.simple_login, name='authentication/simple/login'),
    path('authentication/simple/logout/', views.simple_logout, name='authentication/simple/logout'),
    path('authentication/simple/register/', views.simple_register, name='authentication/simple/register'),
    path('authentication/simple/forgot-password/', views.simple_forgot_password, name='authentication/simple/forgot-password'),
    path('authentication/simple/confirm-mail/', views.simple_confirm_mail, name='authentication/simple/confirm-mail'),
    path('authentication/simple/reset-password/', views.simple_reset_password, name='authentication/simple/reset-password'),
    path('authentication/simple/lock-screen/', views.simple_lock_screen, name='authentication/simple/lock-screen'),
    path('authentication/wizard/', views.authentication_wizard, name='authentication/wizard'),
    path('user/profile/', views.user_profile, name='user/profile'),
    path('user/settings/', views.user_settings, name='user/settings'),
    path('errors/404/', views.error_404, name='errors/404'),
    path('errors/500/', views.error_500, name='errors/500'),
    path('widgets/', views.widgets, name='widgets'),
]
