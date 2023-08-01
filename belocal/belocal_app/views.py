from django.shortcuts import render
import os

#http로 실행했을 때 오류 방지
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create your views here.
def cover(request):
    return render(request, 'cover.html')

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