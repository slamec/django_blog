from django.http import HttpResponse
from django.shortcuts import render_to_response, render
import datetime
from django.conf import settings
 
 
def index(request):
    return HttpResponse("Hello I am Miro bro")
 
 
def today_is(request):
    now = datetime.datetime.now()
    return render(request, 'blog/datetime.html', {
                                    'now': now,
                                    'template_name': 'blog/nav.html' ,
                                    'base_dir': settings.BASE_DIR }
                                )