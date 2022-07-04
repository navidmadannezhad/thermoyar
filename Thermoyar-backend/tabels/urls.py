from .views import SuperHeatList, Sub_ColdList, saturateList
from . import views
from django.urls import path


urlpatterns = [
    path('superheat/', SuperHeatList.as_view()),
    path('sub_cold/', Sub_ColdList.as_view()),
    path('saturate/', saturateList.as_view()),

]