from django.urls import path
from appone.views import *

# urlpatterns = [
#     path('', index, name='index'),
#     path('about', about, name='about'),
# ]

app_name = 'appone'
urlpatterns = [
    path('AscOurStory', ascription_index, name="ascription_index"),
    path('AchOurStory', achievement_index, name="achievement_index"),
    path('', base, name="base")
]