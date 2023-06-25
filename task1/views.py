from django.shortcuts import render, redirect
from .models import Info, Post, Draft
from django.contrib.auth.decorators import login_required

# Create your views here.


def signup(request):
    return render(request, 'signup.html')


def create(request):
    return render(request, 'create.html')


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

        if (password == password1):

            user = Info(type_of=type_of, first_name=first_name, last_name=last_name, prof_pic=prof_pic,
                        username=username, email=email, password=password, address=add,
                        city=city, state=state, pincode=pin)
            user.save()

            return render(request, 'login.html', {'message': 'User Created Successfully , Login Now'})

        else:
            return render(request, 'signup.html', {'error': 'Password and confirm Password not match'})
    return render(request, 'signup.html')


def login_check(request):
    global username
    username = ''
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Info.objects.get(username=username, password=password)

            return render(request, 'dashboard.html', {'user': user})
        except Info.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid username or password.'})
    return render(request, 'login.html')


def logout(request):

    return render(request, 'login.html', {'message': 'Logout Successfully'})


def login(request):
    return render(request, 'login.html')


def publish(request):
    print('HELLO')
    if request.method == "POST":

        task = request.POST.get('task')
        title = request.POST.get('title')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        summary = request.POST.get('summary')
        content = request.POST.get('content')
        print('Hi')
        if (category == 'a'):
                category = 'Mental Health'
        elif (category == 'b'):
                category = 'Heart Disease'
        elif (category == 'c'):
                category = 'Covid 19'
        else:
                category = 'Immunization'
        if task == 'Submit':
                post = Post(title=title, img=image, category=category,
                            summary=summary, content1=content)
                post.save()
                return redirect('view_post')
        else:
                hi = Draft(title=title, img=image, category=category,
                           summary=summary, content1=content)
                hi.save()
                return render(request, 'create.html', {'message': "Draft Saved Succesfully"})

    return render(request, 'create.html')


def view_post(request):
    
    posts = Post.objects.all()
    return render(request, 'view_posts.html', {'posts': posts})

def view_spec(request,pk):
    posts = Post.objects.get(id=pk)
    return render(request, 'posts.html', {'posts' : posts})
def view_draft(request,pk):
    posts = Draft.objects.get(id=pk)
    return render(request, 'posts.html', {'posts' : posts})
def all(request):
    post = Post.objects.all()
    post1 = Draft.objects.all()
    combined = list(post)+list(post1)
    context = {
        'posts': combined,
    }
    return render(request, 'all.html', context)
