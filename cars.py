import bs4 as bs
import urllib.request
import json
from xlwt import Workbook
import locale


def CarsScraper():
    print("Enter cars.com listing: ", end="" )
    wb = Workbook()
    ws = wb.add_sheet("Sheet 1")
    ws.write(0,0, "Price")
    ws.write(0,1, "Mileage")
    ws.write(0,2, "Listing Id")
    ws.write(0,3, "Model")

    myUrl = input()
    sauce = urllib.request.urlopen(myUrl).read()
    soup = bs.BeautifulSoup(sauce, 'lxml')
    specificSoup = soup.find_all('div', class_='listing-row__details')
    count = 2  #helps with page count, looks through all pages


    row = 1
    while(len(specificSoup)):
        for div in specificSoup:
            #print(div.prettify())
            #print(div.find('cars-shop-shared-save-vehicle')['listing-data'])

            listingInfo = json.loads(div.find('cars-shop-shared-save-vehicle')['listing-data'])
            modelYear = listingInfo['modelYear']
            modelName = listingInfo['mdNm']
            modelTrim = "" if listingInfo['trimName'] == None else listingInfo['trimName']
            condition = div.find(itemprop="name").text.split()[0]
            brand = listingInfo['mkNm']
            listingId = listingInfo['listingId']

            price = div.find(itemprop="price")
            miles = div.find('span', {'class': "listing-row__mileage"})



            if (condition.lower() == "new" and price != None):
                print( "Price: ${:8}   Miles: {:6}    Id: {:8}".format(price.text, "new car", listingId))
            elif( (condition.lower() == "certified" or condition.lower() == "used")  and price != None and miles != None):
                print( "Price: ${:8}   Miles: {:6}     Id: {:8}     {} {} {} {} {}".format(price.text, miles.text[:-3], listingId, condition, modelYear, brand, modelName, modelTrim))
                model = condition + " " + str(modelYear) + " " + brand + " " + modelName + " " + modelTrim
                writeToWorkBook(ws, price.text, miles.text[:-3], listingId, model, row)
                row+=1
            else:
                print("NOT PRICED--------------------------------------------------------- at: " + str(listingId))



        firstpart = myUrl.split("&page")
        secondpart = firstpart[1].split("&perPage")
        myUrl = firstpart[0] + "&page=" + str(count) + "&perPage" + secondpart[1]
        count +=1

        sauce = urllib.request.urlopen(myUrl).read()
        soup = bs.BeautifulSoup(sauce, 'lxml')
        specificSoup = soup.find_all('div', class_='listing-row__details')

    wb.save("test.xls")

def writeToWorkBook(ws: Workbook, price: str, miles: str, listingId: int, model: str, row: int):
    locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) #help with numberes from json
    ws.write(row, 0, locale.atoi(price))
    ws.write(row, 1, locale.atoi(miles))
    ws.write(row, 2, listingId)
    ws.write(row, 3, model)





if __name__ == '__main__':
    CarsScraper()
