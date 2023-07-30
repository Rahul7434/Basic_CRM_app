from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
   # path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('signup/',views.register_user,name='signup'),
    path('record/',views.customer_record,name='record'),
    path('delete_record/',views.delete_record,name='delete'),
    path('add_record/',views.add_record,name='add'),
    path('update/',views.update_record,name="update"),
]
