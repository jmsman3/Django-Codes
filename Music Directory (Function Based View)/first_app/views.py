from django.shortcuts import render ,redirect
from first_app.forms import MusicianForm , AlbumForm , RegistrationForm
from first_app.models import MusicianModel , AlbumModel
from django.contrib import messages
from django.contrib.auth import authenticate  ,login , logout ,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm ,SetPasswordForm ,PasswordChangeForm
from django.contrib.auth import forms
# Create your views here.
def person(request):
    if request.user.is_authenticated:
        form = MusicianForm(request.POST)
        if request.method == 'POST':
            if form.is_valid():
                print(form.cleaned_data)
                messages.success(request , f"Congratulations , Musician Added Successfully")
                form.save()
                return redirect('album_page')
        else:
            form = MusicianForm()
        return render(request , 'person.html' , {'form' : form})
    else:
        return redirect('home_page')


def album(request):
    if request.user.is_authenticated:
        form = AlbumForm(request.POST)
        if request.method =='POST':
            if form.is_valid():
                print(form.cleaned_data)
                messages.success(request , f"Congratulations ,Album Added Successfully")
                form.save()
                return redirect('profile_page')
        else:
            form = AlbumForm()
        return render( request , 'album.html' , {'form' : form})
    else:
        return redirect('home_page')

def home(request):
    data = AlbumModel.objects.all()
    return render( request , 'home.html' , {'data' : data})

def SignUp(request):
    if not request.user.is_authenticated:
            
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                user_name = form.cleaned_data.get('username')
                messages.success(request , f"Congratulations ,{user_name} - Your Account Created Successfully")
                form.save()
                return redirect('login_page')
        else:
            form = RegistrationForm()
        return render(request , 'signup.html' , {'form' : form})
    else:
        return redirect('home_page')

def login_system(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request , data = request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = user_name , password = userpass)
                if user is not None:
                    messages.success(request , f"Hey,{user_name} - Your Login Successfully")
                    login(request , user)
                    return redirect('profile_page')
        else:
            form = AuthenticationForm()
        return render(request , 'login.html' , {'form' : form})
    else:
        return redirect('home_page')


def logout_system(request):
    logout(request)
    return redirect('home_page')


 
def profile(request):
    data = AlbumModel.objects.all()
    return render( request , 'profile.html' , {'data' : data})




def edit_person(request ,id):
    if  request.user.is_authenticated:
        album_instance = MusicianModel.objects.get(pk = id)
        form = MusicianForm(instance = album_instance)
        if request.method == 'POST':
            form = MusicianForm(request.POST , instance = album_instance)
            if form.is_valid():
                messages.success(request , f"Congratulations- Musician Edited Successfully")
                form.save()
                return redirect('profile_page')
        return render(request , 'person_edit.html' , {'form' : form})
    else:
        return redirect('home_page')

def album_edit(request ,id):
    if  request.user.is_authenticated:
        album_instance = AlbumModel.objects.get(pk = id)
        form = AlbumForm(instance = album_instance)
        if request.method == 'POST':
            form = AlbumForm(request.POST , instance = album_instance)
            if form.is_valid():
                messages.success(request , f"Congratulations - Album Edited Successfully")
                form.save()
                return redirect('profile_page')
        return render(request , 'album.html' , {'form' : form})
    else:
        return redirect('home_page')

def delete_musician(request , id):
    target_person = AlbumModel.objects.get(pk = id )
    target_person.delete()
    return redirect('profile_page')