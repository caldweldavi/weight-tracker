from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.weight_record_list, name='weight_record_list'),
    path('import/', views.import_weight_records, name='import_weight_records'),
    path('<slug:slug>/', views.weight_record_detail, name='weight_record_detail'),
]