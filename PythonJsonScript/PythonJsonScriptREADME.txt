AUTHOR DATA
```````````
# __author__ = "Dhrumil Amish Shah"
# __copyright__ = "Copyright 2019"
# __credits__ = ["Dhrumil Amish Shah"]
# __version__ = "1.0.0"
# __maintainer__ = "Dhrumil Amish Shah"
# __github__ = "https://github.com/DhrumilShah98/"
# __linkedIn__ = "https://linkedin.com/in/dhrumilshah98/"
####################################################################################################################################

# NOTE: I CAN NOT SHARE THE NAME OF THE WEBSITE, JSON FILE OR EXCEL SHEET.
# IF YOU WANT JSON OR EXCEL SHEET, CONTACT ME :)
# I WAS ABLE TO GET TOTAL 1238 CAR DETAILS. PRETTY AMAZING RIGHT :) 

# THESE 1238 cars were further modularized as below
# Format of the new JSON which I created for simplicity.
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
##### I found one data source (JSON file) which I used to call multiple URLs which were within it
    # from which i got chunks of data. [CONTAINS A LOT DATA OUT OF WHICH I USED ONLY FEW]
##### Then I cleaned all the data and I decided what should I keep and what I should not. (TEDIOUS TASK)
##### I used that file (Here I downloaded it first, but instead I could also have made a network call)
##### Well..... I downloaded it first.
##### Below is the code. It calls multiple URLs one by one, get required data by parsing and then make a excel structure out of it.
    
##### Summarizing....
##### Got a data source (JSON form), called multiple URLS by analyzaing the JSON form, 
##### from multiple URLs, I got a chunks of data after which I created a simple excel structure.
##### You can contact me on linkedIn if you want this data either in Excel or JSON.
####################################################################################################################################

NOTE: I HAVE NOT ADDED SPECIFICATIONS FOR EACH CAR VARIANT IN THE EXCEL SHEET. I AM WORKING ON IT CURRENTLY
      BUT, I HAVE ADDED ALL THE SPECIFICATIONS IN THE JSON. I AM WORKING TO DO SAME IN THE EXCEL TOO.
####################################################################################################################################

SAMPLE JSON 
```````````
EACH VARIANT HAS MORE THAN 45 PROPERITES. PRETTY COOL RIGHT...???
I HAVE SHOW HERE A SMALL JSON HERE BELOW....
{
 "make": [
  {
   "model": [
    {
     "variant": [
      {
       "variantName": "RXE",
       "variantUrl": "variant_url_with_many_different_properites_apart_from_this_in_json",
       "Driver Airbag": "Yes",
       "Rear Tread (mm)": "1545",
       "Fuel Supply System": "Multi Point Fuel Injection",
	.
	.
	45 plus
      },
      {
       "variantName": "RXL"
       "variantUrl": "variant_url_with_many_different_properites_apart_from_this_in_json",
       "Driver Airbag": "Yes",
       "Rear Tread (mm)": "1545",
       "Fuel Supply System": "Multi Point Fuel Injection",
       "Body Type": "MUV",
	.
	.
	45 plus
      }
     ],
     "modelName": "Triber"
    },
      {"model <2>": [{"variant: [{<1,2,....n>}]}], "modelName 2": "model_name"},
      {"model <2>": [{"variant: [{<1,2,....n>}]}], "modelName 2": "model_name"}
      ],
      "name": "Renault"
    }
  ]
}


# 'make' is an array of multiple objects.
# Each object in 'make' contains "name" of make and an array of 'model'
# 'model' is an array of multiple objects.
# Each object in 'model' contains "modelName" of make and an array of 'variant'
# 'variant' is an array of multiple objects.
# Each object in 'variant' contains multiple properties like 'variantName' and more...

+ 45 MORE SPECIFICATIONS FOR EACH CAR VARIANT. 
ALSO, THERE ARE MANY MORE FEATURES WHICH I HAVE NOT SCRAPPED BUT I WILL DO IT IN FUTURE IF I GET SOME MORE TIME ;)
