from django.shortcuts import render
from django.contrib.auth.models import User,Group
from .models import Farmer,Season,Report,Officer
from rest_framework import viewsets
from .serializer  import UserSerializer,GroupSerializer,FarmerSerializer,ReportSerializer,SeasonSerializer,OfficerSerializer


def index(request):
    return render(request,"farmer/index.html")



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FarmerViewSet(viewsets.ModelViewSet):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer

class OfficerViewSet(viewsets.ModelViewSet):
    queryset = Officer.objects.all()
    serializer_class = OfficerSerializer

class SeasonViewSet(viewsets.ModelViewSet):
    queryset = Season.objects.all()
    serializer_class = SeasonSerializer

class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

