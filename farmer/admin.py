from django.contrib import admin
from farmer.models import Farmer,Officer,Report,Season
from import_export.admin import ImportExportModelAdmin

#Registration of models
@admin.register(Farmer)
class FarmerAdmin(ImportExportModelAdmin):
    list_display = ("District","sub_county","parish","village","gender","marriage_status","language","photo","community_status","instructor_possibility","farm_area","crop_type","past_harvest")

@admin.register(Officer)
class OfficerAdmin(ImportExportModelAdmin):
    list_display = ("username", "login_id","parish", "password", "District", "sub_county", "telephone")

@admin.register(Report)
class ReportAdmin(ImportExportModelAdmin):
    list_display = ("user", "season", "area", "rice_type", "sowing_date","sowing_type", "planting_type", 
        "levelling", "watercourse_state", "fertilizer1_type", "fertilizer1_amount", "fertilizer2_type", 
        "fertilizer2_amount","weed_condition", "total_weedtimes", "harvest_date", "harvest_amount","note", "photo1",
        "photo2", "photo3", "photo4")

@admin.register(Season)
class SeasonAdmin(ImportExportModelAdmin):
    list_display = ("username", "season", "area","harvest")

    
# admin.site.register(Farmer)
# admin.site.register(Officer)
# admin.site.register(Report)
# admin.site.register(Season)


admin.site.site_header = "PRIDE_JICA"
