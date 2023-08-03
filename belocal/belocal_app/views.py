from django.shortcuts import render
import os

#http로 실행했을 때 오류 방지
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create your views here.
def cover(request):
    return render(request, 'cover.html')

def init(request):
    return render(request, 'init.html')

def login_personal(request):
    return render(request, 'login_personal.html')

def signin(request):
    return render(request,'signin.html')

def signup(request):
    return render(request,'signup.html')

def profile(request):
    return render(request,'profile.html')

def register_course(request):
    return render(request,'register_course.html')