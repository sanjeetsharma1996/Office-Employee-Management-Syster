from django.urls import path
from . import views

urlpatterns = [
    path('',views.view_all_emp, name='view_all_emp'),
    path('add/', views.add_emp_View.as_view(), name='add_emp_View'),
    path('remove/<int:pk>',views.remove_emp, name='remove'),
    path('update/<int:pk>/',views.update, name='update'),
]
