from django.shortcuts import render
from django.shortcuts import render_to_response

from models import User
from forms import LoginForm
from forms import RegisterForm
# Create your views here.
def index(request):
    form = LoginForm()
    return render_to_response('form.html',{'loginform':form})
def auth(request):
    form = None
    if request.method=='POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            email_user = cd['email'] 
            u = User.objects.get(email=email_user.replace('%40','@'))

            if u.passwd == cd['passwd']:

                request.session['username']=u.nickname
                
                return render_to_response('welcome.html',{'username':cd['email'],'nickname':u.nickname})
    else:
                return index(request)
            
def register(request):
    form = RegisterForm()
    return render_to_response('signup.html',{'regform':form})
def signup(request):
    form = None
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            try :
                User.objects.create(email = cd['email'],
                                passwd = cd['passwd'],
                                nickname = cd['nickname'],
                                label = cd['label'],
                                birthday = cd['birthday'],
                                address  = cd['address'],
                                job = cd['job']
                )
                print 'create over'
                return index(request)
            except:
                print 'create error '
                return register(request)
    else:
        return register(request)

def welcome(request):
    username = request.session['username']
    return render_to_response('welcome.html',{'username':username})
def addblog(request):
    pass
2