from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import os
from .models import registers,Document
from .forms import Upload_data
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
import xdrlib
import glob
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('getdata')
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')    
    else:
        return render(request,'login.html')
    

def register(request):
    if request.method =="POST":
        username = request.POST['Username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            
            if User.objects.filter(username=username).exists():
                messages.info(request,'user name taken...')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password1,first_name=firstname,last_name=lastname,email=email)    
                user.save()
                messages.info(request,'user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching...')
            return redirect('register')    
        return redirect('/')
    else:    
        return render(request,'register.html') 

@login_required(login_url='/')

def amazon(request):
    
    if request.method == 'POST':
        print(BASE_DIR+"\\media\\media\\*")
        del_path=BASE_DIR+"\\media\\media\\*"
        files = glob.glob(del_path)
        for i in files:
            os.remove(i)
            
        form= Upload_data(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
    
        #"C:\\Users\\ROMIT SINGH\\Desktop\\chromedriver.exe"
        Data= Document.objects.all()
        Data=list(Data)
        Data.reverse()
        path=str(Data[0].ChromePath)
        pathTo = os.path.join(BASE_DIR,'media')
        print(pathTo)
        print(Data[0].Excel_file)
        driver = webdriver.Chrome(executable_path=path)
        doc_Dir = str(Data[0].Excel_file)
        doc_Dir = doc_Dir.split('/')
        doc_Dir = "\\media\\".join(doc_Dir)
        
        df = pd.read_excel(os.path.join(BASE_DIR,doc_Dir))
        data_list = df[str(Data[0].ColumnName)].head(int(Data[0].No_of_models)).tolist()
        
        
        productName=[]
        productPrice=[]
        product_orgPrice=[]
        product_img1=[]
        product_img2=[]
        product_img3=[]
        product_img4=[]
        product_description=[]
        specs1=[]
        specs2=[]
        specs3=[]
        specs4=[]
        specs5=[]
        specs6=[]
        specs7=[]
        specs8=[]
        specs9=[]
        specs10=[]
        specs11=[]
        specs12=[]
        specs13=[]
        specs14=[]
        specs15=[]
        specs16=[]
        specs17=[]
        downloadPath= str(Data[0].ImagePath)
        for i in data_list:
            url = "https://www.amazon.in/s?k="+i+"&ref=nb_sb_noss"
            driver.maximize_window()
            driver.get(url)

            try:
                title = driver.find_element_by_css_selector('span.a-size-base-plus.a-color-base.a-text-normal')
                symbol = driver.find_element_by_css_selector('span.a-price-symbol')
                price = driver.find_element_by_css_selector('span.a-price-whole')
                print('try1')
                print(title.text)
                productName.append(title.text)
                print('test')
                print(symbol.text,price.text)
                print('test1')
                pricedata=str(price.text)
                productPrice.append(pricedata)
                time.sleep(2)
                allData = driver.find_element_by_css_selector('a.a-link-normal.a-text-normal').get_attribute('href')
                driver.get(allData)
                main = WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, 'td.a-span7.a-size-base'))
                )
                time.sleep(4)
                try:
                    orgPrice = driver.find_element_by_css_selector('span.priceBlockStrikePriceString.a-text-strike')

                    product_orgPrice.append(orgPrice.text)
                    print(orgPrice.text)
                except:
                    product_orgPrice.append('Nan')
                dataCat= driver.find_elements_by_css_selector('th.a-span5.a-size-base')
                data = driver.find_elements_by_css_selector('td.a-span7.a-size-base')
        #---------------------------------------------------------------------------------------------------------------------------------------------
                #image scrapping

                img1 = driver.find_elements_by_css_selector('span.a-button-inner')
                new = img1[3]
                toggle = driver.find_element_by_css_selector('div.imgTagWrapper')
                product_img1.append(toggle.find_element_by_css_selector('img').get_attribute('src'))
                print(toggle.find_element_by_css_selector('img').get_attribute('src'))
                downImg= requests.get(toggle.find_element_by_css_selector('img').get_attribute('src')).content

                datas = open(downloadPath+str(i)+"1.jpg", 'wb')
                datas.write(downImg)

                ActionChains(driver).move_to_element(new).perform()
                s2 = driver.find_elements_by_css_selector('li.image.item.itemNo1.maintain-height')
                product_img2.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                datas = open(downloadPath + str(i) + "2.jpg", 'wb')
                datas.write(downImg)
                print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                ActionChains(driver).move_to_element(img1[4]).perform()
                s2 = driver.find_elements_by_css_selector('li.image.item.itemNo2.maintain-height')
                product_img3.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                datas = open(downloadPath + str(i) + "3.jpg", 'wb')
                datas.write(downImg)
                print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                ActionChains(driver).move_to_element(img1[5]).perform()
                s2 = driver.find_elements_by_css_selector('li.image.item.itemNo3.maintain-height')
                product_img4.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                datas = open(downloadPath + str(i) + "4.jpg", 'wb')
                datas.write(downImg)
                print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
        #--------------------------------------------------------------------------------------------------------------------------------------------
                # scrapping specs
                description = driver.find_element_by_id('productDescription').find_element_by_tag_name('p')
                print(description.text)
                product_description.append(description.text)

                print(dataCat[0].text,data[0].text)
                dataCat1 = str(dataCat[0].text)+" - "+str(data[0].text)
                specs1.append(dataCat1)
                print(dataCat[1].text,data[1].text)
                dataCat2 = str(dataCat[1].text)+" - "+str(data[1].text)
                specs2.append(dataCat2)
                print(dataCat[2].text,data[2].text)
                dataCat3 = str(dataCat[2].text) + " - "+str(data[2].text)
                specs3.append(dataCat3)
                print(dataCat[3].text,data[3].text)
                dataCat4 = str(dataCat[3].text) + " - "+str(data[3].text)
                specs4.append(dataCat4)
                print(dataCat[5].text,data[5].text)
                dataCat5 = str(dataCat[5].text) + " - "+str(data[5].text)
                specs5.append(dataCat5)
                print(dataCat[6].text,data[6].text)
                dataCat6 = str(dataCat[6].text) + " - "+str(data[6].text)
                specs6.append(dataCat6)
                print(dataCat[7].text,data[7].text)
                dataCat7 = str(dataCat[7].text) + " - "+str(data[7].text)
                specs7.append(dataCat7)
                print(dataCat[8].text,data[8].text)
                dataCat8 = str(dataCat[8].text) + " - "+str(data[8].text)
                specs8.append(dataCat8)
                print(dataCat[9].text,data[9].text)
                dataCat9 = str(dataCat[9].text) + " - "+str(data[9].text)
                specs9.append(dataCat9)
                print(dataCat[10].text,data[10].text)
                dataCat10 = str(dataCat[10].text) + " - "+str(data[10].text)
                specs10.append(dataCat10)
                print(dataCat[11].text,data[11].text)
                dataCat11 = str(dataCat[11].text) + " - "+str(data[11].text)
                specs11.append(dataCat11)
                print(dataCat[12].text,data[12].text)
                dataCat12 = str(dataCat[12].text) + " - "+str(data[12].text)
                specs12.append(dataCat12)
                print(dataCat[13].text,data[13].text)
                dataCat13 = str(dataCat[13].text) +" - "+ str(data[13].text)
                specs13.append(dataCat13)
                try:
                    print(dataCat[14].text, data[14].text)
                    dataCat14 = str(dataCat[14].text) + " - "+str(data[14].text)
                    specs14.append(dataCat14)
                except:
                    specs14.append("Nan")
                try:
                    print(dataCat[15].text, data[15].text)
                    dataCat15 = str(dataCat[15].text) + " - "+str(data[15].text)
                    specs15.append(dataCat15)
                except:
                    specs15.append("Nan")
                try:
                    print(dataCat[16].text, data[16].text)
                    dataCat16 = str(dataCat[16].text) + " - "+str(data[16].text)
                    specs16.append(dataCat16)
                except:
                    specs16.append("Nan")
                try:
                    print(dataCat[17].text, data[17].text)
                    dataCat17 = str(dataCat[17].text) + " - "+str(data[17].text)
                    specs17.append(dataCat17)
                except:
                    specs17.append("Nan")
            except:
                try:
                    print(i)
                    title = driver.find_element_by_css_selector('span.a-size-medium.a-color-base.a-text-normal')
                    symbol = driver.find_element_by_css_selector('span.a-price-symbol')
                    price = driver.find_element_by_css_selector('span.a-price-whole')
                    print(title.text)
                    productName.append(title.text)
                    print(symbol.text,price.text)
                    pricedata = str(price.text)
                    productPrice.append(pricedata)
                    allData = driver.find_element_by_css_selector('a.a-link-normal.a-text-normal').get_attribute('href')
                    driver.get(allData)
                    main = WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'td.a-span7.a-size-base'))
                    )
                    time.sleep(3)
                    try:
                        div = driver.find_element_by_id('price')
                        orgPrice = div.find_element_by_css_selector('span.priceBlockStrikePriceString.a-text-strike')

                        product_orgPrice.append(orgPrice.text)
                        print(orgPrice.text)
                    except:
                        product_orgPrice.append('Nan')
                    dataCat = driver.find_elements_by_css_selector('th.a-span5.a-size-base')
                    data = driver.find_elements_by_css_selector('td.a-span7.a-size-base')
        #--------------------------------------------------------------------------------------------------------------------------------------------
                    #image scrapping
                    img1 = driver.find_elements_by_css_selector('span.a-button-inner')
                    new = img1[3]
                    toggle = driver.find_element_by_css_selector('div.imgTagWrapper')
                    product_img1.append(toggle.find_element_by_css_selector('img').get_attribute('src'))
                    downImg = requests.get(toggle.find_element_by_css_selector('img').get_attribute('src')).content

                    datas = open(downloadPath + str(i) + "1.jpg", 'wb')
                    datas.write(downImg)
                    print(toggle.find_element_by_css_selector('img').get_attribute('src'))
                    time.sleep(4)

                    ActionChains(driver).move_to_element(new).perform()
                    try:
                        s2 = driver.find_elements_by_css_selector('li.image.item.itemNo1.maintain-height')
                        product_img2.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                        downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                        datas = open(downloadPath + str(i) + "2.jpg", 'wb')
                        datas.write(downImg)
                        print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                    except:
                        product_img2.append('Nan')
                    try:
                        ActionChains(driver).move_to_element(img1[4]).perform()
                        s2 = driver.find_elements_by_css_selector('li.image.item.itemNo2.maintain-height')
                        product_img3.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                        downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                        datas = open(downloadPath + str(i) + "3.jpg", 'wb')
                        datas.write(downImg)
                        print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                    except:
                        product_img3.append('Nan')
                    try:
                        ActionChains(driver).move_to_element(img1[5]).perform()
                        s2 = driver.find_elements_by_css_selector('li.image.item.itemNo3.maintain-height')
                        product_img4.append(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                        downImg = requests.get(s2[0].find_element_by_css_selector('img').get_attribute('src')).content

                        datas = open(downloadPath + str(i) + "4.jpg", 'wb')
                        datas.write(downImg)
                        print(s2[0].find_element_by_css_selector('img').get_attribute('src'))
                    except:
                        product_img4.append('Nan')
        #--------------------------------------------------------------------------------------------------------------------------------------------
                    # product specs
                    description = driver.find_element_by_id('productDescription').find_element_by_tag_name('p')
                    print(description)
                    print(description.text)
                    product_description.append(description.text)
                    print(dataCat[0].text, data[0].text)
                    dataCat1 = str(dataCat[0].text) + " - "+str(data[0].text)
                    specs1.append(dataCat1)
                    print(dataCat[1].text, data[1].text)
                    dataCat2 = str(dataCat[1].text) + " - "+str(data[1].text)
                    specs2.append(dataCat2)
                    print(dataCat[2].text, data[2].text)
                    dataCat3 = str(dataCat[2].text) +" - "+ str(data[2].text)
                    specs3.append(dataCat3)
                    print(dataCat[3].text, data[3].text)
                    dataCat4 = str(dataCat[3].text) +" - "+ str(data[3].text)
                    specs4.append(dataCat4)
                    print(dataCat[5].text, data[5].text)
                    dataCat5 = str(dataCat[5].text) + " - "+str(data[5].text)
                    specs5.append(dataCat5)
                    print(dataCat[6].text, data[6].text)
                    dataCat6 = str(dataCat[6].text) +" - "+ str(data[6].text)
                    specs6.append(dataCat6)
                    print(dataCat[7].text, data[7].text)
                    dataCat7 = str(dataCat[7].text) +" - "+ str(data[7].text)
                    specs7.append(dataCat7)
                    print(dataCat[8].text, data[8].text)
                    dataCat8 = str(dataCat[8].text) + " - "+str(data[8].text)
                    specs8.append(dataCat8)
                    print(dataCat[9].text, data[9].text)
                    dataCat9 = str(dataCat[9].text) + " - "+ str(data[9].text)
                    specs9.append(dataCat9)
                    print(dataCat[10].text, data[10].text)
                    dataCat10 = str(dataCat[10].text) + " - "+str(data[10].text)
                    specs10.append(dataCat10)
                    print(dataCat[11].text, data[11].text)
                    dataCat11 = str(dataCat[11].text) +" - "+ str(data[11].text)
                    specs11.append(dataCat11)
                    print(dataCat[12].text, data[12].text)
                    dataCat12 = str(dataCat[12].text) + " - "+str(data[12].text)
                    specs12.append(dataCat12)
                    print(dataCat[13].text, data[13].text)
                    dataCat13 = str(dataCat[13].text) +" - "+ str(data[13].text)
                    specs13.append(dataCat13)
                    try:
                        print(dataCat[14].text, data[14].text)
                        dataCat14 = str(dataCat[14].text) + " - "+str(data[14].text)
                        specs14.append(dataCat14)
                    except:
                        specs14.append("Nan")
                    try:
                        print(dataCat[15].text, data[15].text)
                        dataCat15 = str(dataCat[15].text) +" - "+str(data[15].text)
                        specs15.append(dataCat15)
                    except:
                        specs15.append("Nan")
                    try:
                        print(dataCat[16].text, data[16].text)
                        dataCat16 = str(dataCat[16].text) +" - "+str(data[16].text)
                        specs16.append(dataCat16)
                    except:
                        specs16.append("Nan")
                    try:
                        print(dataCat[17].text, data[17].text)
                        dataCat17 = str(dataCat[17].text) +" - "+str(data[17].text)
                        specs17.append(dataCat17)
                    except:
                        specs17.append("Nan")

                except:
                    pass

        driver.quit()

        rawdata = {'productName': productName,'productPrice':productPrice,'product_orgPrice': product_orgPrice,'product_img1':product_img1,'product_img2':product_img2,'product_img3':product_img3,'product_img4':product_img4,
                'product_description':product_description,'specs1':specs1,'specs2':specs2,'specs3':specs3,'specs4':specs4,'specs5':specs5,'specs6':specs6,
        'specs7':specs7,'specs8':specs8,'specs9':specs9,'specs10':specs10,'specs11':specs11,'specs12':specs12,'specs13':specs13,'specs14':specs14,'specs15':specs15,
        'specs16':specs16,'specs17':specs17,
        }
        df = pd.DataFrame(rawdata, columns=["productName","productPrice","product_orgPrice","product_img1","product_img2","product_img3","product_img4","product_description","specs1","specs2","specs3","specs4","specs5","specs6","specs7","specs8","specs9","specs10","specs11","specs12","specs13","specs14","specs15","specs16","specs17"])
        df.to_csv(os.path.join(BASE_DIR,'static/files/product_detail.csv'))
        print(df)
        messages.info(request,'Your file is ready you can download it.')

        return redirect('amazon')

    else:
        form= Upload_data()
    return render(request, 'amazon.html',{'form':form}) 
    

@login_required(login_url='/')
def scrap(request):
    Base_dir=""
    if request.method=='POST':
        del_path=BASE_DIR+"\\media\\media\\*"
        files = glob.glob(del_path)
        for i in files:
            os.remove(i)
        form= Upload_data(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
    
        #"C:\\Users\\ROMIT SINGH\\Desktop\\chromedriver.exe"
        Data= Document.objects.all()
        Data=list(Data)
        Data.reverse()
        path=str(Data[0].ChromePath)
        pathTo = os.path.join(BASE_DIR,'media')
        print(pathTo)
        print(Data[0].Excel_file)
        driver = webdriver.Chrome(executable_path=path)
        doc_Dir = str(Data[0].Excel_file)
        doc_Dir = doc_Dir.split('/')
        doc_Dir = "\\media\\".join(doc_Dir)
        
        df = pd.read_excel(os.path.join(BASE_DIR,doc_Dir))
        data_list = df[str(Data[0].ColumnName)].head(int(Data[0].No_of_models)).tolist()
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
                path=(str(Data[0].ImagePath)+"\\product"+i+".jpg")
                _image = requests.get(image_url[0].get_attribute('src')).content
                data = open(path,'wb')
                data.write(_image)
                image.append(image_url[0].get_attribute('src'))
                print(image_url[0].get_attribute('src'))

                all_image=driver.find_elements_by_css_selector('img.img-thumbnail.ng-scope')
                for j in range(1,len(image_url)):
                    try:
                        new_path = (str(Data[0].ImagePath)+"\\product"+i+"("+str(j)+").jpg")
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
        df.to_csv(os.path.join(BASE_DIR,'static/files/product_detail.csv'))

        print("data")
        messages.info(request,'Your file is ready you can download it.')
        return redirect('getdata')
    else:
        form= Upload_data()         	
    return render(request, 'scrap.html',{'form':form})
    

