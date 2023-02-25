from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature,Client
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST': #TO handle Request Cmin from register.html
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        cpassword = request.POST['pass1']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request,'USER ALREADY EXSITS')
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username Already EXSITS')
                return redirect("register")
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request,message="Passwords Are not the Same")
            return redirect("register")
    
    else:
        return render(request,'register.html') #To directly Redirect to register.html


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['pass']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:

            messages.info(request,message='Invalid Userame or Password')
            return redirect('login')
    else:
        return render(request,'login.html')


@login_required
def home(request):
    return render(request,'home.html')


@login_required
def post(request,pk):
    return render(request,'post.html',{'pk':pk})

def logout(request):
    auth.logout(request)
    return redirect('/')



def index(request):
    # feat1  = Feature()
    # feat1.id = 1
    # feat1.name = 'Fast'
    # feat1.details = 'VERY FAST'
    # feat1.is_true = True

    # feat2  = Feature()
    # feat2.id = 2
    # feat2.name = 'slow'
    # feat2.details = 'LITTLE SLOW'
    # feat2.is_true = False
    
    # features = [feat1,feat2] 
    features = Feature.objects.all()
    #print(features)
    
    #return render(request,features)
    return render(request,'index.html',{'feature':features})

@login_required
def counter(request):
    posts = [1,2,3,4]
    return render(request,'counter.html',{'posts':posts})
    #print(request.GET['text'])

    
    context = {
        'text' : request.POST['text'],
        'len':len(request.POST['text']) 
    }
    
    return render(request,'counter.html',context)
    
