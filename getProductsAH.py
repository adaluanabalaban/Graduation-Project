from supermarktconnector.ah import AHConnector
connector = AHConnector()

def getProductTitleAllergies(barcode):
    productAllInfo = []
    productDetails = []
    productFilteredInfo = []
    allergiesList = []
    
    # OldAmsterdam cheese barcode
    # white rice barcode = '8710400412175'
    
    print(barcode)
    productAllInfo = connector.get_product_by_barcode(barcode)
    
    # webshopId = 193636   (old Amsterdam)
    # webshopId = 4004   (Mince Meat)
    
    # GET PRODUCT DETAILS FROM WEBSHOPID FOUND IN THE GET_PRODUCT_B_BARCODE REQUEST
    productDetails = connector.get_product_details(productAllInfo['webshopId'])
    
    #APPEND TITLE OF PRODUCT TO OUR FILTERED INFO DICT
    productFilteredInfo.append({'title': productDetails['productCard']['title']})
    
    # GET ALLERGY TO LOOP AND APPEND ALLERGIES LIST TO OUT FILTERED INFO DICT
    allergies = productDetails['tradeItem']['allergenInformation'][0]['items']

    for allergy in allergies:
        if allergy['levelOfContainmentCode']['value'] == 'CONTAINS':
            allergiesList.append(allergy['typeCode']['label'])
    
    productFilteredInfo.append({'allergies': allergiesList})
    print(productFilteredInfo)
    
    return productFilteredInfo


#https://github.com/bartmachielsen/SupermarktConnector 


