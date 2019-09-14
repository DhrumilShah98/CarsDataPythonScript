# __author__ = "Dhrumil Amish Shah"
# __copyright__ = "Copyright 2019"
# __credits__ = ["Dhrumil Amish Shah"]
# __version__ = "1.0.0"
# __maintainer__ = "Dhrumil Amish Shah"
# __github__ = "https://github.com/DhrumilShah98/"

# NOTE: I CAN NOT SHARE THE NAME OF THE WEBSITE
# I WAS ABLE TO GET TOTAL 1238 CAR DETAILS. PRETTY AMAZING RIGHT :) 

# Format of the new JSON which is to be created.
#{
#  "make": [
#    {
#      "name": "makeName",
#      "model": [
#        {
#          "modelName": "modelName1",
#          "variant": [
#           {
#             "variantName": "variantName1",
#             "specification1": "specification",
#             "specification2": "specification",...
#           },
#           {
#             "variantName": "variantName2",
#             "specification1": "specification",
#             "specification2": "specification",...
#           }
#         ]
#       },
#       {  
#          "modelName": "modelName2",
#          "variant": [
#           {
#             "variantName": "variantName",
#             "specification1": "specification",
#             "specification2": "specification",...
#           }
#         ]
#       }
#     ]
#   }
#  ]
#}

##### Fetch data from 'car_website_name' Website.
##### Lucky Me: I was able to find a JSON which contains a lot of data.
##### I invested a lot of time to find a main data source on "car_website_name's"
##### I found one data source (JSON file) which I used to call multiple URLs from which i got chunks of data.
##### Then I cleaned all the data and I decided what should I keep and what I should not. (TEDIOUS TASK)
##### I used that file (Here I downloaded it first, but instead I could also have made a network call)
##### Well..... I downloaded it first.
##### Below is the code. It calls multiple URLs one by one, get required data by parsing and then make a good structure out of it.
##### Well.... Structure I created here was not perfect. I could have made to code more complex and in corporate everything
    # in one file. But instead I used two files and I created actual structure in '2.CarCleanJsonScript'
    
  ### Summarizing....
  ### Got a data source (JSON form), called multiple URLS by analyzaing the JSON form, 
  ### from multiple URLs, I got a chunks of data after which I created a simple structure. (Not the final one).
  ### In the second file '2. CarCleanJsonScript', I created an ACTUAL STRUCTURE as above in the beginning and removed
    # redundany from makeName, modelName and variantName.
import json
import requests
from collections import OrderedDict
# Data loaded from 'file_name.json' file in form of json
car_website_json_data = json.load(open('1. file_name.json'))

# 'all_cars' is an array of objects and each object contains data of single car. 
all_cars = car_website_json_data["data"]["cars"]["cars"]

# Total number of variants
total_variants = 0

# Primary URL of Website
car_website = "car_website_name"

# all_cars_specs will be array of multiple cars with each car having array of multiple variant objects
all_cars_specs = {"make":[]}

# i is used to manage the car - for each car it will be incremented  by one
i = 0
# Loop through 'all_cars' array and get each object stored in 'car'
for car in all_cars:
    
    all_cars_specs["make"].append({"name": car["brandName"], "model": [{"modelName": car["name"], "variant": []}]})
    
    # 'all_variants' is an array of all the variants for a given 'car'
    all_variants = car["variants"]
    # Loop through 'all_variants' array and get object stored in 'variant'

    for variant in all_variants:
        # Increase the count for the 'total_variants'
        total_variants = total_variants + 1        
        
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
        
        curr_varient = OrderedDict()
        curr_varient["variantName"] = variant["carVariantId"]
        curr_varient["variantUrl"] = car_string
        
        # all_specification will contain all the specifications of the car variant
        all_specification = data["specs"]["specification"]
        for specification in all_specification:
            current_specs_array = specification["items"]
            
            # 'curr_spec_item' is item for the current specification
            for curr_spec_item in current_specs_array:
                curr_varient[curr_spec_item["text"]] = curr_spec_item["value"]
        
        all_cars_specs["make"][i]["model"][0]["variant"].append(curr_varient)
        # Print 'total_variants' to see how many variants are being stored in the workbook
        # There were total 1238 variants. Each with LOTS OF DATA in it.
        print (total_variants)
        
    # i wil increment for new car
    i = i + 1
    
# Print 'total_variants' at the end        
print (total_variants)

# JSON will be stored in '2.file_name json' file
text_file = open("2. file_name.json", "w")
text_file.write(json.dumps(all_cars_specs, indent=1))
text_file.close()
  
        