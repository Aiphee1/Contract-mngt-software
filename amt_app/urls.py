from django.urls import path
from .import views

urlpatterns = [
    #path('', views.so_index,name='so_index'), #get and post request for insert operation
    path('form/', views.amt_form,name='amt_insert'), #get and post request for insert operation
    path('<int:id>/', views.amt_form,name='amt_update'), # get and post request for update operation
    path('delete/<int:id>/',views.amt_delete,name='amt_delete'),
    path('list/',views.amt_list,name='amt_list') #get request to retrieve and display all records
]
