#importing the models needed
import csv
from farmer.models import District, Sub_county, Parish

#define my function
def main():
#here we open the csv file
        f = open ('jica.csv')
        #then read from the csv.reader
        reader = csv.reader(f)
        #we create a for loop to iterate through the data
        for district_name, sub_county_name, parish_name in reader:
                district, create = District.objects.get_or_create(name = district_name)
                sub_county, create = Sub_county.objects.get_or_create(name=sub_county_name,district=district)
                parish, create = Parish.objects.get_or_create(name = parish_name, sub_county = sub_county)
                print(f'added {district_name}, {sub_county_name}, {parish_name}')
                #we print the function to see all we have from the terminal
        return "all are added"  
#we finally call the function  
main()

