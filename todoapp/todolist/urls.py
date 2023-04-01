from django.urls import path
from .views import export_to_excel_view

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('update/<int:todo_id>/', views.update, name='update'),
    path('delete/<int:todo_id>/', views.delete, name='delete'),
    path('export-to-excel/', export_to_excel_view, name='export_to_excel')
]