from selenium import webdriver
import os
import time
from bs4 import BeautifulSoup
import json
import pprint



driver=webdriver.Chrome(os.environ.get('CHROMEDRIVER_PATH'))

def read_url(url):
    driver.get(url)
    driver.maximize_window()

    time.sleep(3)
    html = driver.page_source
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep(2)
    html = driver.page_source #get the HTML file

    soup = BeautifulSoup(html, 'html.parser')
    return soup








def get_all_brands(url):
    soup = read_url(url)
    brand_divs = soup.select('div.brands a.marki_blok')
    brandsList = []
    for brand in brand_divs:
        title = brand.get('title')  # or brand['title']
        name = brand.select_one('strong').text.strip()
        link = brand.get('href')
        link = "https://www.auto-data.net"+link
        brandsList.append({'name':name,'cars':get_brand_cars()})
    return brandsList









def get_car_variant_details(car_variant_url):
    soup = read_url(car_variant_url)
    specs = {}
    current_section = None
    car_specs = soup.select("table.cardetailsout tr")
    for row in car_specs:
        # Handle section headers
        if "no" in row.get("class", []):
            th = row.find("th")
            if th:
                current_section = th.get_text(strip=True)
                specs[current_section] = {}
        else:
            th = row.find("th")
            td = row.find("td")
            if th and td and current_section:
                label = th.get_text(strip=True)
                value = td.get_text(" ", strip=True)
                specs[current_section][label] = value

    return specs




def get_model_variants(car_variant_url):
    soup = read_url(car_variant_url)
    car_variants_html = soup.select("table tr.i a")
    car_variants = []
    for car_variant in car_variants_html:
        car_variant_name = car_variant.get('title')

        if car_variant_name is None:
            continue
        else:
            car_variant_name = car_variant.select_one('strong span').text.strip()
            car_variant_url = "https://www.auto-data.net"+car_variant.get('href')
            car_variants.append({"car variant name":car_variant_name,"car variant details":get_car_variant_details(car_variant_url)})
            # car_variants.append({"car variant name":car_variant_name,"car variant details":car_variant_url})
    return car_variants










def get_brand_cars(url):
    soup = read_url(url)
    brand_cars_html = soup.select("ul.modelite li ul li a")
    brand_cars=[]
    for brand_car in brand_cars_html:
        link = "https://www.auto-data.net"+brand_car.get('href')  # or brand['title']
        model_name = brand_car.select_one('strong').text.strip()
        # brand_cars.append({'model_name':model_name,'car_variants':get_brand_car_models(link)})
        brand_cars.extend(get_brand_car_models(link))

    return brand_cars





def get_brand_car_models(url):
    soup = read_url(url)
    brand_cars_models_html = soup.select("table tr.f th.i a")
    brand_cars_models=[]
    for brand_cars_model in brand_cars_models_html:
        link = "https://www.auto-data.net"+brand_cars_model.get('href')  # or brand['title']
        model_name = brand_cars_model.select_one('strong').text.strip()
        brand_cars_models.append({'model name':model_name,'car_variants':get_model_variants(link)})

    return brand_cars_models




#---------------------run this if you want a single brand cars to be scraped (provide brand link)-----------------------------
brandcars = get_brand_cars("https://www.auto-data.net/en/zx-brand-130")
pprint.pprint(brandcars)
print(len(brandcars))




#---------------------run this if you want a single brand cars to be scraped-----------------------------
# brandcars = get_all_brands("https://www.auto-data.net/en/allbrands")
# pprint.pprint(brandcars)
# print(len(brandcars))

def saveAsJson(variable):
    with open("brandcars.json", "w", encoding="utf-8") as f:
        json.dump(brandcars, f, indent=2, ensure_ascii=False)

    print("✅ Saved as brandcars.json")

saveAsJson(brandcars)

