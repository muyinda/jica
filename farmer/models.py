import csv
from django.db import models
from django.contrib.auth.models import User
# Required models.

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    login_id = models.IntegerField(null=True)
    username = models.CharField(max_length=20, null=True)
    login_id = models.IntegerField(null=True)
    password = models.CharField(max_length=20, null=True)
    District = models.CharField(max_length=20, null=True)
    parish = models.CharField(max_length=20, null=True)
    sub_county = models.CharField(max_length=20, null=True)
    telephone = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    District = models.CharField(max_length=20, null=True)
    sub_county = models.CharField(max_length=20, null=True)
    parish = models.CharField(max_length=20, null=True)
    village = models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=20, null=True)
    age = models. IntegerField(null=True)
    marriage_status = models.CharField(max_length=20, null=True)
    language = models.CharField(max_length=20, null=True)
    telephone = models.IntegerField(null=True)
    photo = models.FileField(null=True)
    community_status = models.TextField(null=True)
    instructor_possibility = models.BooleanField(null=True)
    farm_area = models.CharField(max_length=20, null=True)
    crop_type = models.CharField(max_length=20, null=True)
    past_harvest = models.TextField(null=True)
    
    def __str__(self):
        return self.user.username

class Report(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    season = models.CharField(max_length=20, null=True)
    area = models.CharField(max_length=20, null=True)
    rice_type = models.CharField(max_length=20, null=True)
    sowing_date = models.CharField(max_length=20, null=True)
    sowing_type = models.CharField(max_length=20, null=True)
    planting_type = models.CharField(max_length=20, null=True)
    levelling = models.CharField(max_length=20, null=True)
    watercourse_state = models.CharField(max_length=20, null=True)
    fertilizer1_type = models.CharField(max_length=20, null=True)
    fertilizer1_amount = models.IntegerField(null=True)
    fertilizer2_type = models.CharField(max_length=20, null=True)
    fertilizer2_amount = models.IntegerField(null=True)
    weed_condition = models.CharField(max_length=20, null=True)
    total_weedtimes = models.IntegerField(null=True)
    harvest_date = models.DateTimeField(null=True)
    harvest_amount = models.IntegerField(null=True)
    note = models.TextField(null=True)
    photo1 = models. FileField(null=True)
    photo2 = models. FileField(null=True)
    photo3 = models. FileField(null=True)
    photo4 = models. FileField(null=True)
    
    def __str__(self):
        return self.user.username

class Season(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE, null=True)
    username = models.CharField(max_length = 15, null=True)
    season = models.CharField(max_length=15, null=True)
    area = models.IntegerField(null=True)
    harvest = models.IntegerField(null=True)


    def __str__(self):
        return self.username     



#District model
class District(models.Model):
    name = models.CharField(max_length = 40, null=True)
    def __str__(self):
        return self.name

#sub_county model
class Sub_county(models.Model):
    name = models.CharField(max_length = 40, null=True)
    #we now relate the sub_county to the district
    district = models.ForeignKey('District', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name

#parish model
class Parish(models.Model):
    name = models.CharField(max_length = 40, null=True)
    #we now relate the sub_county to the district
    sub_county = models.ForeignKey('Sub_county', on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.name
