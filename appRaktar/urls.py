from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('details/<int:pk>/', views.inventory_details, name='inventory_details'),
    path('backup/', views.backup_database, name='backup_database'),
    path('restore/', views.restore_database, name='restore_database'),
    path("export/csv/", views.export_machines_csv, name="export_machines_csv"),
    path("export/excel/", views.export_machines_excel, name="export_machines_excel"),
]