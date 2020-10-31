from ebaysdk.finding import Connection
import ezgmail, json


def apiCall(keywords, min, max, listing):
    api = Connection(config_file=r'ebay.yaml', debug=True, siteid="EBAY-US")

    request = {
        'keywords': keywords,
        'itemFilter': [
            {'name': 'MinPrice', 'value': min}, 
            {'name': 'MaxPrice', 'value': max},
            {'name': 'ListingType', 'value': listing}
        ],
        'paginationInput': {
            'entriesPerPage': 10,
            'pageNumber': 1
        },
        'sortOrder': 'PricePlusShippingLowest'
    }

    return api.execute('findItemsByKeywords', request)


def saveThis(code):
    with open('itemIDs.txt', 'a') as f:
        f.write('\n' + code)


def searchForItem(keywords, min, max, listing):
    response = apiCall(keywords, min, max, listing)
    
    if response.reply.searchResult._count != "0":
        with open('itemIDs.txt') as saveFile:
          data = [line.rstrip('\n') for line in saveFile] #Each item id is stored on a new line so they are easily distinguishable

          for item in response.reply.searchResult.item: 
            if item.itemId not in data: #Whenever an item whose id we have already indexed is encountered, we do not send a new email
                items.append(f"Title: {item.title}\nPrice: ${item.sellingStatus.currentPrice.value}\nURL: {item.viewItemURL}")
                saveThis(item.itemId)

                
        
def formatMessage():
    formattedText = "The following items have been listed:"
    for item in items:
        formattedText += "\n" + item + "\n"

    return formattedText



if __name__=="__main__":
    items = []
    with open('itemNames.json') as itemNames:
      searchData = json.load(itemNames)
      for item in searchData:
          searchForItem(item["name"], item["minPrice"], item["maxPrice"], item["listing"])
    if formatMessage() != "The following items have been listed:":  #This is to ensure we don't get an email when no items have been found
        ezgmail.send('youremailhere@gmail.com', 'New Items have been Listed', formatMessage())

