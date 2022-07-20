from django.contrib import admin
from django.urls import path
from home import bisection, gaussSeidle, newtonraphson, regulafalsi, secant, views

urlpatterns = [
    path('', views.home, name='home'),
    path('GaussSeidle', gaussSeidle.GaussSeidle, name='GaussSeidle'),
    path('RegulaFalsi', regulafalsi.RegulaFalsi, name='RegulaFalsi'),
    path('Secant', secant.Secant, name='Secant'),
    path('NewtonRaphson', newtonraphson.NewtonRaphson, name='NewtonRaphson'),
    path('BiSection', bisection.BiSection, name='BiSection'),
    path('formpage', views.form_name_view, name = 'form_name'),
    path('about', views.about, name = 'about')


]