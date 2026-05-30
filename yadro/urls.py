from django.urls import path

from . import views

app_name = 'yadro'

urlpatterns = [
    path('', views.record_list, name='record_list'),
    path('structureproject/', views.record_list, name='structureproject'),
    path('add/', views.add_record, name='add_record'),
    path('<int:pk>/update/', views.update_record, name='update_record'),
    path('<int:pk>/delete/', views.delete_record, name='delete_record'),
]
