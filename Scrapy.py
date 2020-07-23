from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import csv
import requests
from selenium.webdriver.common.action_chains import ActionChains


path="C:\\Users\\ROMIT SINGH\\Desktop\\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)
doc_Dir = 'R:'
df = pd.read_excel(str(doc_Dir)+'\\titan_samples.xlsx')
data_list = df['Model No'].head(10).tolist()

name=[]
price=[]
image=[]
spec_1=[]
spec_2=[]
spec_3=[]
spec_4=[]
spec_5=[]
spec_6=[]
spec_7=[]
spec_8=[]
spec_9=[]
spec_10=[]
spec_11=[]
spec_12=[]
spec_13=[]
spec_14=[]
spec_15=[]
spec_16=[]
spec_17=[]
model=[]
org_price = []


description=[]
driver.maximize_window()
driver.get("https://www.titan.co.in/")
#ext_list = ['','NL','N', 'NA', 'NB', 'NC', 'ND', 'NE', 'NF', 'NG', 'NH', 'NK', 'NM', 'NJ']

for i in data_list:
    main = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "searchIcon"))
    )
    inputElement = driver.find_element_by_id("searchIcon")
    inputElement.click()
    main1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "searchTextBox"))
    )
    search = driver.find_element_by_id("searchTextBox")
    search.send_keys(i)
    search.send_keys(Keys.RETURN)
    time.sleep(5)


    try:
        try:
            print(i)
            try:
                main2 = WebDriverWait(driver, 25).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-xs-12.product-detail.hidden-xs"))
                )
            except:
                time.sleep(4)
            time.sleep(3)
            product_name = str(driver.find_element_by_css_selector('div.col-xs-12.product-detail.hidden-xs').find_element_by_css_selector('h1').text)
            model_no = driver.find_element_by_css_selector('div.col-xs-12.product-detail.hidden-xs').find_element_by_tag_name('span').text
            print(model_no)
            if product_name == '':
                time.sleep(4)
                product_name = str(driver.find_element_by_css_selector('div.col-xs-12.product-detail.hidden-xs').find_element_by_css_selector('h1').text)
                if product_name == '':
                    product_name = 'Not found'
                print(product_name)
                name.append(product_name)
            else:
                print(product_name)
                name.append(product_name)
        except:
            new_link = driver.find_element_by_css_selector('a.nav-link').get_attribute('href')
            print(new_link)
            driver.get(new_link)
            time.sleep(5)
            try:
                main2 = WebDriverWait(driver, 25).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.col-xs-12.product-detail.hidden-xs"))
                )
            except:
                time.sleep(4)
            product_name = str(driver.find_element_by_css_selector(
                'div.col-xs-12.product-detail.hidden-xs').find_element_by_css_selector('h1').text)
            model_no = driver.find_element_by_css_selector(
                'div.col-xs-12.product-detail.hidden-xs').find_element_by_tag_name('span').text
            print(model_no)
            if product_name == '':
                time.sleep(3)
                product_name = str(driver.find_element_by_css_selector(
                    'div.col-xs-12.product-detail.hidden-xs').find_element_by_css_selector('h1').text)
                if product_name== '':
                    product_name = 'Not found'
                print(product_name)
                name.append(product_name)
            else:
                print(product_name)
                name.append(product_name)
        model.append(i)
        try:
            main2 = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CLASS_NAME, "last-price"))
            )
            time.sleep(2)
            try:
                old_price = driver.find_element_by_css_selector('span.old-price-value.ng-binding').text
                print(old_price)
                org_price.append(old_price)
            except:
                org_price.append('Nan')
            print(driver.find_element_by_class_name("last-price").text)
            price.append(driver.find_element_by_class_name("last-price").text)
        except:
            try:
                old_price = driver.find_element_by_css_selector('span.old-price-value.ng-binding').text
                print(old_price)
                org_price.append(old_price)
            except:
                org_price.append('Nan')
            print('Nan')
            price.append('Nan')
        main2 = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.col-xs-6.col-sm-6.col-md-6.no-padding.ng-binding"))
        )
        print(driver.find_element_by_css_selector('h3.col-xs-6.col-sm-6.col-md-6.no-padding.ng-binding').text)
        main2 = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "h3.col-xs-6.col-sm-6.col-md-6.no-padding.ng-binding"))
        )
        time.sleep(5)
        image_url = driver.find_elements_by_css_selector('img.img-responsive.ng-scope')
        path=("R:\\tnt_images\\product"+i+".jpg")
        _image = requests.get(image_url[0].get_attribute('src')).content
        data = open(path,'wb')
        data.write(_image)
        image.append(image_url[0].get_attribute('src'))
        print(image_url[0].get_attribute('src'))

        all_image=driver.find_elements_by_css_selector('img.img-thumbnail.ng-scope')
        for j in range(1,len(image_url)):
            try:
                new_path = ("R:\\tnt_images\\thumb\\product"+i+"("+str(j)+").jpg")
                print(image_url[j].get_attribute('src'))
                thumb_image=requests.get(image_url[j].get_attribute('src')).content
                thumb_image_loc = open(new_path,'wb')
                thumb_image_loc.write(thumb_image)
            except:
                pass


        try:
            main3 = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link.ng-binding"))
            )
        except:
            pass
        element = driver.find_elements_by_css_selector('a.nav-link.ng-binding')
        scrollElement = driver.find_element_by_css_selector('h3.ng-binding')
        print(scrollElement.text)
        scrollElement.location_once_scrolled_into_view
        try:
            mains = WebDriverWait(driver, 25).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-description.row.animated.fadeIn.ng-scope"))
            )
            desc=driver.find_element_by_css_selector('div.product-description.row.animated.fadeIn.ng-scope').text
            print(desc)
            spec_1.append(desc)
        except:
            spec_1.append("Nan")
        element[1].click()
        main4 = WebDriverWait(driver, 25).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.col-xs-12.col-md-6.list_15"))
        )

        specs1 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_1')
        cate = specs1.find_element_by_tag_name('h3').text
        glass_type = specs1.find_element_by_tag_name('p').text
        glass_type= str(cate)+' - '+str(glass_type)
        print(glass_type)
        spec_2.append(glass_type)
        specs2 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_2')
        cate = specs2.find_element_by_tag_name('h3').text
        glass_type = specs2.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_3.append(glass_type)
        specs3 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_3')
        cate = specs3.find_element_by_tag_name('h3').text
        glass_type = specs3.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_4.append(glass_type)
        specs4 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_4')
        cate = specs4.find_element_by_tag_name('h3').text
        glass_type = specs4.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_5.append(glass_type)
        specs5 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_5')
        cate = specs5.find_element_by_tag_name('h3').text
        glass_type = specs5.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_6.append(glass_type)
        specs6 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_6')
        cate = specs6.find_element_by_tag_name('h3').text
        glass_type = specs6.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_7.append(glass_type)
        specs7 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_7')
        cate = specs7.find_element_by_tag_name('h3').text
        glass_type = specs7.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_8.append(glass_type)
        specs8 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_8')
        cate = specs8.find_element_by_tag_name('h3').text
        glass_type = specs8.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_9.append(glass_type)
        specs9 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_9')
        cate = specs9.find_element_by_tag_name('h3').text
        glass_type = specs9.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_10.append(glass_type)
        specs10 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_10')
        cate = specs10.find_element_by_tag_name('h3').text
        glass_type = specs10.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_11.append(glass_type)
        specs11 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_11')
        cate = specs11.find_element_by_tag_name('h3').text
        glass_type = specs11.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_12.append(glass_type)
        specs12 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_12')
        cate = specs12.find_element_by_tag_name('h3').text
        glass_type = specs12.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_13.append(glass_type)
        specs13 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_13')
        cate = specs13.find_element_by_tag_name('h3').text
        glass_type = specs13.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_14.append(glass_type)
        specs14 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_14')
        cate = specs14.find_element_by_tag_name('h3').text
        glass_type = specs14.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_15.append(glass_type)
        specs15 = driver.find_element_by_css_selector('li.col-xs-12.col-md-6.list_15')
        cate = specs15.find_element_by_tag_name('h3').text
        glass_type = specs15.find_element_by_tag_name('p').text
        glass_type = str(cate) + ' - ' + str(glass_type)
        print(glass_type)
        spec_16.append(glass_type)
    except:
        pass

print(name,'\n',price,'\n',org_price,'\n',image,'\n',model,'\n',spec_1,'\n',spec_2,'\n',spec_3,'\n',spec_4,'\n',spec_5,'\n',spec_6,'\n',spec_7,'\n',spec_8,'\n',spec_9,'\n',spec_10,'\n',spec_11,'\n'
      ,spec_12,'\n',spec_13,'\n',spec_14,'\n',spec_15,'\n',spec_16,'\n')
driver.quit()
rawdata = {
    "name": name,"model":model,"org_price":org_price,"price":price,"image":image,"spec_1":spec_1,"spec_2":spec_2,"spec_3":spec_3,"spec_4":spec_4,"spec_5":spec_5,"spec_6":spec_6,"spec_7":spec_7,
"spec_8":spec_8,"spec_9":spec_9,"spec_10":spec_10,"spec_11":spec_11,"spec_12":spec_12,"spec_13":spec_13,"spec_14":spec_14,"spec_15":spec_15,"spec_16":spec_16
}
df = pd.DataFrame(rawdata, columns=["name","model","org_price","price","image","spec_1","spec_2","spec_3","spec_4",
                                    "spec_5","spec_6","spec_7","spec_8","spec_9","spec_10","spec_11","spec_12","spec_13","spec_14","spec_15","spec_16"])
df.to_csv("D:\\user\\tnt_Product7.csv")
print(df)




