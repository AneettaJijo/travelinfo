# from django.contrib import messages
# from django.contrib.auth.models import User,auth
# from django.shortcuts import render, redirect
#
#
# # Create your views here.
# def login(request):
#     if request.method == 'POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         auth.login(request,user)
#         return redirect('/')
#         # return redirect('login')
#     else:
#         return render(request,'login.html')
#
# def reg(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         first_name=request.POST['first_name']
#         last_name=request.POST['last_name']
#         email=request.POST['email']
#         password=request.POST['password']
#         cpassword=request.POST['cpassword']
#
#         if password==cpassword:
#            if User.objects.filter(username=username).exists():
#                messages.info(request,'username taken')
#                return redirect('reg')
#            elif User.objects.filter(email=email).exists():
#                messages.info(request,'email taken')
#                return redirect('reg')
#
#            else:
#                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email)
#                user.save()
#                return redirect('login')
#
#
#         else:
#             messages.info(request,'password do not match')
#             return redirect('reg')
#         return redirect('/')
#     return render(request,'reg.html')
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect


# Create your views here.
def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('reg')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, email=email)
                user.save()
                return redirect('login')


        else:
            messages.info(request, "password not matching")
            return redirect('reg')
        return redirect('/')
    return render(request, "reg.html")


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid details")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


