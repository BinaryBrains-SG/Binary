from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
# from agora_token_builder import RtcTokenBuilder as tb

# Create your views here.
def home(request):
    return render(request,'landing-page.html')

@csrf_exempt
def login(requst):
    name=requst.POST.get('name')
    email=requst.POST.get('email')
    pwd=requst.POST.get('pwd') 
    img=requst.FILES.get('img')
    return redirect(f'../student/dashboard/{email}')


@csrf_exempt
def tlogin(requst):
    name=requst.POST.get('name')
    email=requst.POST.get('email')
    pwd=requst.POST.get('pwd') 
    img=requst.FILES.get('img')
    return redirect(f'../instructor/dashboard/{email}')

def loginpage(request):
    return render(request,'student-login.html')

def tloginpage(request):
    return render(request,'teacher-login.html')

def dashboard(request,email):
    var=Student.objects.get(email=email)
    data={}
    data['name']=var.name
    data['url']=var.img
    print(var.img)
    data['levels']=[i for i in range(var.levels)]
    return render(request,'student-dashboard.html',data)

def tdashboard(request,email):
    var=Instructor.objects.get(email=email)
    data={}
    data['name']=var.name
    data['url']=var.img
    return render(request,'teacher-dashboard.html',data)

def room(request):
    return render(request,'index.html')

def community(request):
    var=Doubt.objects.all()
    dict1={}
    l=[]
    for i in var:
        # dict1[i.question]=i.answers
        l.append(i)
    dict2={"list":l}
    return render(request,'community.html',dict2)

@csrf_exempt
def search(request):
    text=request.POST.get('keyword')
    dict1={}
    l=[]
    var=Doubt.objects.all()
    for i in var:
        if text.lower() in i.question.lower():
            l.append(i)
    dict2={"list":l}
    return render(request,'community.html',dict2)















































    

def test1(request):
    return render(request,'quiz1.html')

def test2(request):
    return render(request,'quiz2.html')

def c(request):
    return render(request,'youtube/cyou.html')

def python(request):
    return render(request,'youtube/pythonyou.html')

def php(request):
    return render(request,'youtube/phpyou.html')

def next(request):
    return render(request,'youtube/next.html')

def react(request):
    return render(request,'youtube/reactjsyou.html')