from django.shortcuts import render
import os

#http로 실행했을 때 오류 방지
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


# API 키
API_KEY1 = 'AIzaSyCcis4wzheGUE8j9hRQ9xp43w7LREedD6M'
API_KEY2 = 'AIzaSyCybUkLvjkdaWFgdc7GtVdnn-vgal0g0mg'
API_KEY3 = 'AIzaSyD1mS8iqeHOniuebnom3cFT_yVG1VI1odA'
API_KEY4 = 'AIzaSyA2-DRryTN0JYnI3P-letj_bl-sj9wpVKw'
API_KEY5 = 'AIzaSyB5nnPCXwDu3BWpCQxcrpa8mdJYqBZANjQ'

# Create your views here.
def cover(request):
    return render(request, 'cover.html')

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

def reward_ask(request):
    return render(request, 'reward_quest/reward_ask.html')

def question1(request):
    return render(request, 'reward_quest/question1.html')

def question2(request):
    return render(request, 'reward_quest/question2.html')

def reward_done(request):
    return render(request, 'reward_quest/reward_done.html')

def main_home(request):
    return render(request, 'main/home.html')

def main_wallet(request):
    return render(request, 'main/wallet.html')

def main_map(request):
    return render(request, 'main/map.html')

def main_chat(request):
    return render(request, 'main/chat.html')

def guide_home(request):
    return render(request, 'guide/home.html')
