from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<id>',views.delete,name='delete'),
    path('uncross/<id>',views.uncross,name='uncross'),
    path('cross_off/<id>',views.cross_off,name='cross_off'),
    path('edit/<id>',views.edit,name='edit'),
]
