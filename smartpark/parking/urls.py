from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('entrance/', views.choose_entrance, name='choose_entrance'),
    path('entrance/<str:entrance>/levels/', views.choose_level, name='choose_level'),
    path('entrance/<str:entrance>/level/<int:level>/slots/', views.slots, name='slots'),
    path('confirm-slot/', views.confirm_slot, name='confirm_slot'),
    path('receipt/', views.receipt, name='receipt'),
    path('parked/', views.parked, name='parked'),
    path('exit/', views.exit_form, name='exit_form'),
    path('exit/verify/', views.verify_exit, name='verify_exit'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
