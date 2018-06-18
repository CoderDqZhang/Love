from django.shortcuts import render
import json
import time
import datetime
import re
import datetime,time
from  django.http import  HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from love.models import Love
# Create your views here.

def home(request):
    return render(request, 'Z&H/love.html')

# def loveTime(request):
#     love = Love.objects.order_by('-id').first()
#     if not love:
#         love = Love(girl_name="huanying", boy_name="zhangdquan", girl_age=26, boy_age=25)
#         love.love_startTime = datetime.datetime.now()
#         love.save()
#     d = love.love_startTime
#     return render(request, 'Z&H/loveTime.html', {'year': d.year,'mouth': d.month,'day': d.day,'hh':
#         d.hour + 8,'mm': d.minute,'ss': d.second})

@csrf_exempt
def testPost(request):
    return HttpResponse("" + "")