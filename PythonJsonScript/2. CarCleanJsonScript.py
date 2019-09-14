# __author__ = "Dhrumil Amish Shah"
# __copyright__ = "Copyright 2019"
# __credits__ = ["Dhrumil Amish Shah"]
# __version__ = "1.0.0"
# __maintainer__ = "Dhrumil Amish Shah"
# __github__ = "https://github.com/DhrumilShah98/"

# NOTE: I CAN NOT SHARE THE NAME OF THE WEBSITE
# I WAS ABLE TO GET TOTAL 1238 CAR DETAILS. PRETTY AMAZING RIGHT :) 

# Format of the new JSON data structure
# ACTUAL AMAZING FORMAT.....
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


# 'make' is an array of multiple objects.
# Each object in 'make' contains "name" of make and an array of 'model'
# 'model' is an array of multiple objects.
# Each object in 'model' contains "modelName" of make and an array of 'variant'
# 'variant' is an array of multiple objects.
# Each object in 'variant' contains multiple properties like 'variantName' and more...

import json

# This will open(open()) and load(load()) the file and will make it JSON parseable.
car_website_json_data = json.load(open('2. file_name.json'))

# 'all_car_old_make' will contain array of all the makes.
all_car_old_make = car_website_json_data["make"]

# 'all_car_new_make' will contain array of all the makes collected from 'all_car_old_make' to form a new structure.
all_car_new_make = {"make": []}

# Iterate through all the 'make' in 'all_car_old_make'. 'old_make' will have one 'make' at a time.
for old_make in all_car_old_make:
    
    # 'old_car_make' will contain "name" of the current make.
    old_car_make = old_make["name"]
    # Iterate through all the 'model' in 'old_make'. 'old_model' will have one 'model' at a time.
    for old_model in old_make["model"]:
        
        # 'old_car_model' will contain "modelName" of the current model.
        old_car_model = old_model["modelName"]
        # 'make_flag' True will check if there is any make with the same name in 'new_make["name"]'.
        # If there it it will be set to False.
        make_flag = True
        # Iterate through all the 'make'(new) in 'all_car_new_make'. 'new_make' will have one 'make' at a time. New make.
        for new_make in all_car_new_make["make"]:
            
            if old_car_make == new_make["name"]:
                make_flag = False
                # 'model_flag' True will check if there is any model with the same name in 'new_make["modelName"]'.
                # If there it it will be set to False.
                model_flag = True
                for new_model in new_make["model"]:
                    
                    if old_car_model == new_model["modelName"]:
                        model_flag = False
                        # make and model both are found in 'all_car_new_make'. 
                        # Simply append the old_car_variant to current_new_make => current_new_model.
                        for old_car_variant in old_model["variant"]:
                            new_model["variant"].append(old_car_variant)
                    else:
                        continue
                
                if model_flag:
                    # Make a whole new structre of current model as it was not found in new_model and append the modelName and variant to it.
                    new_make["model"].append({"modelName": old_car_model, "variant": old_model["variant"]})
                    break
                continue
            else:
                continue
            
        if make_flag: 
            # Make a whole new structre of current make as it was not found in new_make and append the name, model and variant to it.
            all_car_new_make["make"].append({"name":old_car_make, "model": [{"modelName": old_car_model, "variant": old_model["variant"]}]})
            break
     
# This part is use for cleaning the make name(name), model name(modelName) and variant name (variantName)  
# make: Rolls-Royce                       ->  Rolls Royce
# model: Rolls Royce Dawn                 ->  Dawn
# variant: Rolls-Royce Dawn Convertible   ->  Convertible

# Hyundai                                 ->  Hyundai
# Hyundai Elite i20                       ->  Elite i20
# Hyundai i20 Era                         ->  i20 Era   
for curr_make in all_car_new_make["make"]:

    curr_make_name = curr_make["name"].replace("-", " ").strip()
    for curr_model in curr_make["model"]:
        
        curr_model_name = curr_model["modelName"].replace("-", " ").strip()
        
        for curr_variant in curr_model["variant"]:
        
            curr_model_split = curr_model_name.split(" ")
            curr_variant["variantName"] = curr_variant["variantName"].replace("-"," ").strip()
            for element in curr_model_split:
                curr_variant["variantName"] = curr_variant["variantName"].replace(element," ").strip()
            
        curr_model["modelName"] = curr_model_name.replace(curr_make_name, '').strip()
        
    curr_make["name"] = curr_make["name"].replace("-", " ").strip()

# JSON will be stored in '3. file_name.json' file
json_file = open("3. file_name.json", "w")
json_file.write(json.dumps(all_car_new_make, indent=1))
json_file.close()   