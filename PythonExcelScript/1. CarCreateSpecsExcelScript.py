# __author__ = "Dhrumil Amish Shah"
# __copyright__ = "Copyright 2019"
# __credits__ = ["Dhrumil Amish Shah"]
# __version__ = "1.0.0"
# __maintainer__ = "Dhrumil Amish Shah"
# __github__ = "https://github.com/DhrumilShah98/"

# NOTE: I CAN NOT SHARE THE NAME OF THE WEBSITE
# I WAS ABLE TO GET TOTAL 1238 CAR DETAILS. PRETTY AMAZING RIGHT :) 

##### Fetch data from 'car_website_name' Website.
##### Lucky Me: I was able to find a JSON which contains a lot of data.
##### I invested a lot of time to find a main data source on "car_website_name's"
##### I found one data source (JSON file) which I used to call multiple URLs which were within it
    # from which i got chunks of data.
##### Then I cleaned all the data and I decided what should I keep and what I should not. (TEDIOUS TASK)
##### I used that file (Here I downloaded it first, but instead I could also have made a network call)
##### Well..... I downloaded it first.
##### Below is the code. It calls multiple URLs one by one, get required data by parsing and then make a excel structure out of it.
    
  ### Summarizing....
  ### Got a data source (JSON form), called multiple URLS by analyzaing the JSON form, 
  ### from multiple URLs, I got a chunks of data after which I created a simple excel structure.
import json
import requests
import xlwt 
from xlwt import Workbook 

# Create object of Workbook
wb = Workbook() 

# 'add_sheet' is used to create sheet. 
cars_data_sheet = wb.add_sheet('1_sheet_name')

# Data loaded from '1_file_name.json' file in form of json
cars_json_data = json.load(open('1_file_name.json'))

# 'all_cars' is an array of objects and each object contains data of single car. 
all_cars = cars_json_data["data"]["cars"]["cars"]

# Total number of variants
total_variants = 0

# Primary URL of Website
car_website = "car_website_name"

# 'i' if for each row (outer loop)
i = 0
# 'j' is for each column (inner loop). Each car has 'n' variants where n > 1
j = 0
# Loop through 'all_cars' array and get each object stored in 'car'
for car in all_cars:
    # 'all_variants' is an array of all the variants for a given 'car'
    all_variants = car["variants"]
    # Loop through 'all_variants' array and get object stored in 'variant'
    for variant in all_variants:
        
        # Increase the count for the 'total_variants'
        total_variants = total_variants + 1
        
        # After every iternation, increment i by one (new row).
        i = i + 1
        # 'j' is for each column. Every time it is turned to '1' to start from the 1st cell of new row
        j = 1
        cars_data_sheet.write(i,j, car["brandName"])
        j = j + 1
        cars_data_sheet.write(i,j, car["name"])
        j = j + 1
        cars_data_sheet.write(i,j, car["engine"])
        j = j + 1
        cars_data_sheet.write(i,j, car["mileage"])
        j = j + 1
        cars_data_sheet.write(i,j, car["seating"])
        j = j + 1
        cars_data_sheet.write(i,j, car["modelShortName"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["subText"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["fuelName"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["carVariantId"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["title"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["highWayAvg"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["urbanAvg"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["displayCarVariantId"])
        j = j + 1        
        cars_data_sheet.write(i,j, variant["vehicleType"])
        
        # 'variant_url' is the url for the given car variant.
        variant_url = variant["url"].split('/')
        car_brand = variant_url[2]
        car_model = variant_url[3][:-4]
        # JSON data for each car variant can be fetched from the 'car_string'
        # This 'car_string' I prepared by looking at many data source and I found a structure in this URL.
        # This "URL" was based on makeName, modelName and variantName. 
        # This URL helped me to get all specifications for a given makeName, modelName. AMAZING RIGHT ;)
        car_string = """car_website_name"""
        
        # 'res' object will contain the data received when 'car_string' is called.
        res = requests.get(car_string).text
        # 'loads' will make the json parsable. 
        json_res = json.loads(res)
        
        # 'data' is the parent layer
        data = json_res["data"]
        
        # overView object contains 'priceRange' and 'modelPriceRange'
        j = j + 1
        if "priceRange" in data["overView"].keys():
            cars_data_sheet.write(i,j, data["overView"]["priceRange"])
        j = j + 1
        if "modelPriceRange" in data["overView"].keys():
            cars_data_sheet.write(i,j, data["overView"]["modelPriceRange"])
        
        # dataLayer object contains many different car properties
        dataLayer = json_res["data"]["dataLayer"]
        j = j + 1
        if "oem_name" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["oem_name"])
        j = j + 1
        if "model_name" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["model_name"])
        j = j + 1
        if "variant_name" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["variant_name"])
        j = j + 1
        if "car_segment" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["car_segment"])
        j = j + 1
        if "engine_cc" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["engine_cc"])
        j = j + 1
        if "fuel_type" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["fuel_type"])
        j = j + 1
        if "transmission_type" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["transmission_type"])
        j = j + 1
        if "brand_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["brand_new"])
        j = j + 1
        if "model_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["model_new"])
        j = j + 1
        if "display_model_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["display_model_new"])
        j = j + 1
        if "variant_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["variant_new"])
        j = j + 1
        if "fuel_type_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["fuel_type_new"])
        j = j + 1
        if "engine_capacity_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["engine_capacity_new"])
        j = j + 1
        if "max_engine_capacity_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["max_engine_capacity_new"])
        j = j + 1
        if "min_engine_capacity_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["min_engine_capacity_new"])
        j = j + 1
        if "transmission_type_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["transmission_type_new"])
        j = j + 1
        if "mileage_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["mileage_new"])
        j = j + 1
        if "max_mileage_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["max_mileage_new"])
        j = j + 1
        if "min_mileage_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["min_mileage_new"])
        j = j + 1
        if "seating_capacity_new" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["seating_capacity_new"])
        j = j + 1
        if "transmission_type" in dataLayer.keys():
            cars_data_sheet.write(i,j, dataLayer["transmission_type"])
        j = j + 1
        cars_data_sheet.write(i,j, car_string)
        # Print 'total_variants' to see how many variants are being stored in the workbook
        print (total_variants)
        # Store all the car -> variant detains in the workbook
        wb.save('cars_data_sheet.xls')  
# Print 'total_variants' at the end        
print (total_variants)
        
 
        
        
        