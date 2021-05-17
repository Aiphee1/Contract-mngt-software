from django.urls import path
from .import views

urlpatterns = [
    path('', views.lpo_index,name='lpo_index'), #get and post request for insert operation
    path('lpo/', views.lpo_form,name='lpo_insert'), #get and post request for insert operation
    path('<int:id>/', views.lpo_form,name='lpo_update'), # get and post request for update operation
    path('delete/<int:id>/',views.lpo_delete,name='lpo_delete'),
    path('list/',views.lpo_list,name='lpo_list') #get request to retrieve and display all records
]