from django.contrib.auth.models  import User,Group
from .models import Farmer,Report,Season,Officer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("url", "username", "email", "groups")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("url", "name")



class OfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Officer
        fields = ("username", "login_id","parish", "password", "District", "sub_county", "telephone")

class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = ("username", "season", "area","harvest")

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ("user", "season", "area", "rice_type", "sowing_date","sowing_type", "planting_type", 
        "levelling", "watercourse_state", "fertilizer1_type", "fertilizer1_amount", "fertilizer2_type", 
        "fertilizer2_amount","weed_condition", "total_weedtimes", "harvest_date", "harvest_amount","note", "photo1",
        "photo2", "photo3", "photo4")

class FarmerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmer
        fields = ("District","sub_county","parish","village","gender","marriage_status","language","photo","community_status","instructor_possibility","farm_area","crop_type","past_harvest")
