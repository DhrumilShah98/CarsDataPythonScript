# CarsDataPythonScript

### SCRAPING JSON WEBPAGE
<pre>
author     = "Dhrumil Amish Shah"
copyright  = "Copyright 2019"
credits    = ["Dhrumil Amish Shah"]
version    = "1.0.0"
maintainer = "Dhrumil Amish Shah"
github     = "https://github.com/DhrumilShah98/"
linkedIn   = "https://linkedin.com/in/dhrumilshah98/"
</pre>
**NOTE: I CAN NOT SHARE THE NAME OF THE WEBSITE**

I WAS ABLE TO GET TOTAL OF 1238 CAR DETAILS. PRETTY AMAZING RIGHT :)

## FOLDER: PythonExcelScript :- 1. CarCreateSpecsExcelScript
* Fetch the data from 'car_website_name' website. Lucky Me: I was able to find a JSON which contains a lot of data.
* I invested a lot of time to find the main data source on "car_website_name's"
* I found one data source (JSON file) which I used to call multiple URLs which were within it
    from which i got chunks of data. [CONTAINS A LOT DATA OUT OF WHICH I USED ONLY FEW]
* Then I cleaned all the data and I decided what should I keep and what I should not. [TEDIOUS TASK]
* I used that file (Here I downloaded it first, but instead I could also have made a network call) Well... I downloaded it first.
* Below is the code. It calls multiple URLs one by one, get required data by parsing and then make an Excel structure out of it.
    
### Summarizing....
1. Got a data source (JSON form), called multiple URLS by analyzaing the JSON form, 
2. From multiple URLs, I got a chunks of data after which I created a simple excel structure.
3. You can contact me on linkedIn if you want this data either in Excel or JSON.

**NOTE:** I HAVE NOT ADDED SPECIFICATIONS FOR EACH CAR VARIANT IN THE EXCEL SHEET. I AM WORKING ON IT CURRENTLY
      BUT, I HAVE ADDED ALL THE SPECIFICATIONS IN THE JSON. I AM WORKING TO DO SAME IN THE EXCEL TOO.
<pre>
TOTAL NUMBER OF COLUMNS: 38 COLUMNS

1) brandName			Eg: Hyundai
2) name				Eg: Hyundai Grand i10
3) engine			Eg: 1197cc
4) mileage			Eg: 17.0kmpl
5) seating			Eg: 5 seater
6) modelShortName		Eg: Grand i10
7) subText			Eg: 1197cc, 18.9kmpl
8) fuelName			Eg: Petrol
9) carVariantId			Eg: Hyundai Grand i10 1.2 Kappa Sportz Dual Tone
10) title			Eg: Hyundai Grand i10 1.2 Kappa Sportz Dual Tone
11) highWayAvg			Eg: 18.9
12) urbanAvg			Eg: 19.1
13) displayCarVariantId		Eg: Hyundai Grand i10 1.2 Kappa Sportz Dual Tone
14) vehicleType			Eg: Hatchback
15) priceRange			Eg: 6.4 Lakh
16) modelPriceRange		Eg: 4.97 - 7.63 Lakh
17) oem_name			Eg: hyundai
18) model_name			Eg: hyundai grand i10
19) variant_name		Eg: hyundai-grand-i10-1.2-kappa-sportz-dual-tone
20) car_segment			Eg: hatchback cars
21) engine_cc			Eg: 1197
22) fuel_type			Eg: petrol
23) transmission_type		Eg: manual
24) brand_new			Eg: hyundai
25) model_new			Eg: hyundai grand i10
26) display_model_new		Eg: Hyundai Grand i10
27) variant_new			Eg: hyundai grand i10 1.2 kappa sportz dual tone
28) fuel_type_new		Eg: petrol
29) engine_capacity_new		Eg: 1000cc - 2000cc
30) max_engine_capacity_new	Eg: 1197
31) min_engine_capacity_new	Eg: 1197
32) transmission_type_new	Eg: manual
33) mileage_new			Eg: 15 kmpl and above
34) max_mileage_new		Eg: 18
35) min_mileage_new		Eg: 18 
36) seating_capacity_new	Eg: 5 
37) transmission_type		Eg: manual 
38) url - JSON			Eg: url for many other data in json form

45 MORE SPECIFICATIONS FOR EACH CAR VARIANT(variant_name). 
ALSO, THERE ARE MANY MORE FEATURES WHICH I HAVE NOT SCRAPPED BUT I WILL DO IT IN FUTURE IF I GET SOME MORE TIME ;)

</pre>

## FOLDER: PythonJsonScript :- 1. CarCreateSpecsJsonScript & 2.CarCleanJsonScript
The first file (1. CarCreateSpecsJsonScript) is responsible for getting all the data while the second file (2. CarCleanJsonScript)
is responsible for structuring and cleaning of the data. [THIS CAN BE DONE IN ONE FILE, BUT I DID IN 2 FILES]

* Fetch data from 'car_website_name' website. Lucky Me: I was able to find a JSON which contains a lot of data.
* I invested a lot of time to find a main data source on "car_website_name's"
* I found one data source (JSON file) which I used to call multiple URLs which were within it
  from which i got chunks of data. [CONTAINS A LOT DATA OUT OF WHICH I USED ONLY FEW]
* Then I cleaned all the data and I decided what should I keep and what I should not. (TEDIOUS TASK)
* I used that file (Here I downloaded it first, but instead I could also have made a network call)
* Well..... I downloaded it first.
* Below is the code. It calls multiple URLs one by one, get required data by parsing and then make a JSON structure out of it.
    
### Summarizing....
1.  Got a data source (JSON form), called multiple URLS by analyzaing the JSON form, 
2.  From multiple URLs, I got a chunks of data after which I created an awesome JSON structure.
3.  You can contact me on linkedIn if you want this data either in Excel or JSON.

THESE 1238 cars were further modularized as below
<pre>
Format of the new JSON which I created for simplicity.

{
  "make": [
    {
      "name": "makeName",
      "model": [
        {
          "modelName": "modelName1",
          "variant": [
            {
            "variantName": "variantName1",
            "specification1": "specification",
            "specification2": "specification",...
            },
            {
            "variantName": "variantName2",
            "specification1": "specification",
            "specification2": "specification",...
            }
          ]
        },
        {  
          "modelName": "modelName2",
          "variant": [
            {
            "variantName": "variantName",
            "specification1": "specification",
            "specification2": "specification",...
            }
          ]
        }
      ]
    }
  ]
}
</pre>

## SAMPLE JSON 
<pre>
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

'make' is an array of multiple objects.
Each object in 'make' contains "name" of make and an array of 'model'.
'model' is an array of multiple objects.
Each object in 'model' contains "modelName" of make and an array of 'variant'.
'variant' is an array of multiple objects.
Each object in 'variant' contains multiple properties like 'variantName' and more...
</pre>

45 MORE SPECIFICATIONS FOR EACH CAR VARIANT. 
ALSO, THERE ARE MANY MORE FEATURES WHICH I HAVE NOT SCRAPPED BUT I WILL DO IT IN FUTURE IF I GET SOME MORE TIME ;)

THIS PROJECT WAS FUN :)
