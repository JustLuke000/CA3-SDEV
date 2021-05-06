# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from datetime import date
import calendar
from calendar import HTMLCalendar

# def index(request):
#     return HttpResponse("Hello World. You're at the home page of appone")
#
# def about(request):
#     title = 'Software for the Global Market 2 2020-2021'
#     author= 'Replace this with your name'
#     html = '''<!DOCTYPE html>    <html>    <head>
#     <title>''' + title + '''</title>
#     </head>
#     <body>
#     <h1>About ''' + title + '''</h1>
#     <p>This Website was developed by ''' + author + '''.</p>
#     </body>
#     </html>'''
#
#     return HttpResponse(html)

# def index(request, year=date.today().year, month=date.today().month):
#     year = int(year)
#     month = int(month)
#     if year < 1900 or year > 2099: year = date.today().year
#     month_name = calendar.month_name[month]
#     # Give the Django variables title and cal values
#     title = "Basic Calendar - %s %s" % (month_name, year)
#     cal = HTMLCalendar().formatmonth(year, month)
#     # return base.html passing our populated variables title and cal as parameters
#     return render(request, 'calender_base.html', {'title': title, 'cal': cal})

def ascription_index(request):
    return render(request, 'ascription_index.html')

def achievement_index(request):
    return render(request, 'achievement_index.html')

def base(request):
    return render(request, 'base.html')
#
# def testlang(request):
#     return HttpResponse(_('Welcome to language translation!'))