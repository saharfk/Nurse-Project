from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('P1/', views.index, name='home'),
    path('step1/P1/', views.step1, name='S1'),
    path('step2/P1/', views.step2, name='S2'),
    path('step3/P1/', views.step3, name='S3'),
    path('step4/P1/', views.step4, name='S4'),
    path('step5/P1/', views.step5, name='S5'),
    path('step6/P1/', views.step6, name='S6'),
    path('step7/P1/', views.step7, name='S7'),
    path('step8/P1/', views.step8, name='S8'),
    path('step9/P1/', views.step9, name='S9'),
    path('step10/P1/', views.step10, name='S10'),
    path('step11/P1/', views.step11, name='S11'),
    path('step12/P1/', views.step12, name='S12'),
    path('step13/P1/', views.step13, name='S13'),
    path('step14/P1/', views.step14, name='S14'),
    path('step15/P1/', views.step15, name='S15'),
    path('step16/P1/', views.step16, name='S16'),
    path('step17/P1/', views.step17, name='S17'),
    path('step18/P1/', views.step18, name='S18'),
    path('step19/P1/', views.step19, name='S19'),
    path('step20/P1/', views.step20, name='S20'),
    path('step21/P1/', views.step21, name='S21'),
    path('step22/P1/', views.step22, name='S22'),
    path('step3/P1/reports/', views.reports, name='reports'),
    path('step7/P1/reportsP/', views.reportTextP, name='reportsP'),
    path('step11/P1/reportsWE/', views.reportTextWE, name='reportsWE'),
]
