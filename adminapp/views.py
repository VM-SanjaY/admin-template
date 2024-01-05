from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
# Create your views here.



def adminlogin(request):
    if request.user.is_superuser or request.user.is_staff:
        return redirect('adminhome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            if '@' in username:
                usermodal = User.objects.filter(email=username)
                if usermodal.exists():
                    user = authenticate(username=usermodal[0].username, password=password)
                else:
                    user = None
            else:
                user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('adminhome')
                elif user.is_staff:
                    return redirect('adminhome')
                else:
                    return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, 'logs/loginpage.html')
    








def adminregister(request):
    if request.user.is_superuser or request.user.is_staff:
        if request.method == "POST":
            name = request.POST.get('name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirmpassword = request.POST.get('confirmpassword')
            admincheck = request.POST.get('admin')
            if password == confirmpassword:
                if User.objects.filter(username=username).exists():      
                    messages.info(request,"Username already exist")
                    return redirect('adminregister')
                else:
                    if User.objects.filter(email=email).exists():
                        print("Email ID already exists")
                        return redirect('adminregister')
                    else:
                        if admincheck == "yes":
                            user = User.objects.create_user(username=username,email=email,password=password,first_name = name)
                            user.is_staff = True
                            user.is_superuser = True
                            user.save()
                            profileadmin = Profileadmin(customeruser=username)
                            profileadmin.save()
                            return redirect('adminhome')
                        else:
                            user = User.objects.create_user(username=username,email=email,password=password)
                            user.is_staff = True
                            user.save()
                            profileadmin = Profileadmin(customeruser=username)
                            profileadmin.save('adminhome')
            else:
                messages.info(request,"Both the password are not same")
                return redirect('adminregister')
        return render(request,'logs/registerpage.html')
    else:
        return redirect ('userpage')
    


def adminlogout(request):
    logout(request)
    return redirect('adminlogin')


def adminhome(request):
    if request.user.is_superuser or request.user.is_staff:
        page = "Dashboard"
        context = {"page":page}
        return render(request,'pages/dashboard.html',context)
    else:
        return redirect ('userpage')

def admintable(request):
    if request.user.is_superuser or request.user.is_staff:
        page = "Table"
        customerdetail = Profileadmin.objects.all()


        context = {"page":page,"customerdetail":customerdetail}
        return render(request,'pages/table1.html',context)
    else:
        return redirect ('userpage')

def admintableedit(request):
    if request.user.is_superuser:
        page = "Table"
        customerdetail = Profileadmin.objects.all()
        if request.method == "POST":
            isstaffs = {}
            for customer in customerdetail:
                if customer.customeruser.is_staff:
                    customer_id = customer.id
                    isstaff = request.POST.get(f'isstaff_{customer_id}')
                    if isstaff is not None:  # Check if the value exists
                        isstaffs[customer_id] = isstaff.capitalize()
                    else:
                        isstaffs[customer_id] =isstaff
            for customer_id, isstaff in isstaffs.items():
                custer = User.objects.get(id=customer_id)
                custer.is_staff = True
                print("value of cluster",custer)
                print(f"Quantity for item {customer_id} updated to {isstaff}")
                print(f"Quantity for item {customer_id}: {isstaff}")
                
                # return redirect('admintable')

            print("dictionary of staff", isstaffs)

        context = {"page": page, "customerdetail": customerdetail}
        return render(request, 'pages/table1edit.html', context)
    else:
        return redirect('userpage')



def adminprofile(request):
    if request.user.is_superuser or request.user.is_staff:
        page = "Profile"
        profiledetail = Profileadmin.objects.get(customeruser=request.user)
        context = {"page":page,"profiledetail":profiledetail}
        return render (request, 'pages/adminprofile.html',context)
    else:
        return redirect('userpage')
    
def editprofile(request):
    if request.user.is_superuser or request.user.is_staff:
        page = "Edit Profile"
        profiledetail = Profileadmin.objects.get(customeruser=request.user)
        context = {"page":page,"profiledetail":profiledetail}
        return render (request, 'pages/editprofile.html',context)
    else:
        return redirect('userpage')