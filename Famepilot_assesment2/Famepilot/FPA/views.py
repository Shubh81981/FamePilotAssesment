from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from .forms import ProfileForm


@api_view(['GET','POST'])
def Profile_list(request):
    if request.method=='GET':
        Profiles = Profile.objects.all()
        serializer = ProfileSerializer(Profiles,many=True)
        return Response(serializer.data)
    elif request.method=='POST':

        serializer = ProfileSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def register(request):
    if request.method == 'POST':

        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        user_name = request.POST['Username']
        email = request.POST['Email']
        password1 = request.POST['Password1']
        password2 = request.POST['Password2']
        if password1 == password2:
            if get_user_model().objects.filter(username = user_name).exists():
                messages.info(request,'username taken')
                return redirect('/FPA')
            elif get_user_model().objects.filter(email = email).exists():
                messages.info(request,'email taken')
                return redirect('/FPA')
            else:
                myuser = get_user_model().objects.create_user(user_name, email, password1)
                myuser.First_name = first_name
                myuser.Last_name = last_name
                myuser.save();
                print("user created")
                messages.info(request, 'your account has been created')
                return redirect('/FPA')
        else:
            return redirect('/FPA')
    else:
        return render(request,'register.html')

def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/FPA/data')
        else:
            messages.info(request,'invalid user')
            return redirect('/FPA')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/FPA')

def data(request):
    user = authenticate(username='username', password='password')
    if  request.user.is_authenticated:

        Profiles = Profile.objects.all()
        serializer = ProfileSerializer(Profiles, many=True)

        return render(request, 'data.html', {'data': serializer.data})
    else:
        return HttpResponse("error 401")

def add_data(request):
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/FPA')
    context = {'form':form}
    return render(request, 'add_data.html', context)



