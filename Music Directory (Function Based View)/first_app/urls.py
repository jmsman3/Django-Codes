from django.urls import path , include
from .import views
urlpatterns = [
    path('person/', views.person , name= 'person_page' ),                   
    path('album/', views.album , name= 'album_page' ),                   
    path('home/', views.home , name= 'home_page' ),       
    path('profile/', views.profile , name= 'profile_page' ),       

    path('signup/', views.SignUp , name= 'signup_page' ),                   
    path('login/', views.login_system , name= 'login_page' ),                   
    path('logout/', views.logout_system , name= 'logout_page' ),                   
    path('album_edit/<int:id>', views.album_edit , name= 'album_edit_page' ),                   
    path('person_edit/<int:id>', views.edit_person , name= 'person_edit_page' ),                   
    path('delete_musician/<int:id>', views.delete_musician , name= 'delete_musician' ),                   
]
