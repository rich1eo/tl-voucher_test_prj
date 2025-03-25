from django.urls import path
from . import views

urlpatterns = [
    path('html/', views.voucher_html, name='voucher_html'),
    path('pdf/', views.voucher_pdf, name='voucher_pdf'),
]