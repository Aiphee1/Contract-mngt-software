from django.urls import path
from .import views


urlpatterns = [
    #path('', views.so_index,name='so_index'), #get and post request for insert operation
    path('form/', views.so_form,name='so_insert'), #get and post request for insert operation
    path('<int:id>/', views.so_form,name='so_update'), # get and post request for update operation
    path('delete/<int:id>/',views.so_delete,name='so_delete'),
    path('list/',views.so_list,name='so_list') #get request to retrieve and display all records
]