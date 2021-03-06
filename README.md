# Cars.com-webscraper
Help first time car buyers

My app scrapes data from car listings via Cars.com. It then exports data to an
excel sheet where users can manipulate data/notice trends. This will serve
helpful for first time buyers or any car buyers for that matter, to know the true price
of a certain vehicle they are looking for.   

App was written in Python3 and utilizes the BeautifulSoup4 library to parse data.



## Tools
Python3: https://www.python.org/download/releases/3.0/  

BeautifulSoup4(WebScraper): https://www.crummy.com/software/BeautifulSoup/bs4/doc/  

Data: https://www.cars.com/  

##HOW TO USE:
1.) Clone project    
2.) Narrow down search results on Cars.com.  
3.) Change listing results to `100 per page`. Copy url address.   
3.) Run 'cars.py'   
4.) When asked for input, enter previously saved cars.com url address.      
5.) Check local folder for excel sheet.  
6.) Enjoy :)  

##TIP:
1.) Individual car listing can be found with this url format:  
    `https://www.cars.com/vehicledetail/detail/` +  "LISTING_ID"  + `/overview/`      

##Preview
This data shows all 2016/2017 Honda Accord Sport for sale in the USA at the time.       
Average Price: $22,693.12   
Average Mileage: 9,942    

![screen shot 2016-12-30 at 12 47 58 am](https://cloud.githubusercontent.com/assets/14288364/21562067/eec35108-ce29-11e6-8b48-34b8b1f4f636.png)



This data shows all 2014 Porsche Carrera S Coupe for sale in the USA at the time.   
Average Price: $82,564   
Average Mileage: 19,039   

![screen shot 2016-12-30 at 12 31 22 am](https://cloud.githubusercontent.com/assets/14288364/21562065/eac3fe54-ce29-11e6-8f31-02950df38cca.png)

