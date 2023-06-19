from django.shortcuts import render,redirect
from .models import Info
# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def signup_data(request):
    if request.method == "POST":
        type_of = request.POST.get('type')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        prof_pic = request.POST.get('profile_pic')
        add = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pincode')
        password = request.POST.get('password')
        password1 = request.POST.get('confirm_password')
        if Info.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username is already taken.'})
        print(type_of,first_name,last_name,username,email,prof_pic,add,city,state,pin,password,password1)
        if (password == password1):
            
            user = Info(type_of= type_of ,first_name=first_name, last_name=last_name, prof_pic=prof_pic,
                        username=username, email=email, password=password, address=add,
                        city=city, state=state, pincode=pin)
            user.save()
            
            return render(request,'login.html',{'message':'User Created Successfully , Login Now'})
        
        else:
            return render(request,'signup.html',{'error':'Password and confirm Password not match'})
    return render(request ,'signup.html')

def login_check(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Info.objects.get(username=username, password=password)

            return render(request,'dashboard.html' , {'user':user})
        except Info.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid username or password.'})
    return render(request , 'login.html' )

def logout(request):
    
    return render(request,'login.html' , {'message': 'Logout Successfully'})

def login(request):
    return render(request,'login.html')