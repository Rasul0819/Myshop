from django.urls import path
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('product/<int:id>/',views.detail,name='detail'),

    path('registration/',views.sign_up,name='sign_up'),
    path('login/',views.sign_in,name='sign_in'),
    path('logout/',views.log_out,name='log_out'),

]