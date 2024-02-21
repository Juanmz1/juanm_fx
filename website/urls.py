from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('welcome/', views.welcome_user, name='welcome'),
    path('welcome/verify/', views.verify_account, name='verify'),
    path('starter/', views.start_user, name='starter'),
    path('gift_card/', views.gift_card_page, name='gift_card'),
    path('gift_card_detail/', views.gift_card_detail, name='gift_card_detail'),
    #path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.email_verification, name='activate'),
]
