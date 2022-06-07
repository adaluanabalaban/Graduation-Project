import cv2
from pyzbar import pyzbar
from getProductsAH import getProductTitleAllergies
from supermarktconnector.ah import AHConnector

import pandas as pd
import numpy as np
#import math
from sklearn.decomposition import TruncatedSVD

connector = AHConnector()




#a = input()
#a = int(a)
a = 1
global list_item_name
list_item_name = []
for _ in range(a):
    def image_taker():
        cam = cv2.VideoCapture(0)
        
        cv2.namedWindow("capture the product")
        
        img_counter = 0
        
        while True:
            ret, frame = cam.read()
            if not ret:
                print("failed to grab frame")
                break
            cv2.imshow("capture the product", frame)
        
            k = cv2.waitKey(1)
            if k%256 == 27:
                # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:
                # SPACE pressed
                img_name = "product_{}.jpg".format(img_counter)
                cv2.imwrite(img_name, frame)
                print("{} written!".format(img_name))
                img_counter += 1
        
        cam.release()
        
        cv2.destroyAllWindows() 
    image_taker()
        
        #code taken from https://stackoverflow.com/questions/34588464/python-how-to-capture-image-from-webcam-on-click-using-opencv
    
    
    def barcoder():
        def decodeIMG(image):
            ean_code = []
            # decodes all barcodes from an image
            decoded_objects = pyzbar.decode(image)
            for obj in decoded_objects:
                # GET THE BARCODE NUMBER OF EVERY DECODED OBJECT
                ean_code.append(obj.data)
            #RETURN THE BARCODE NUMBER
            return ean_code
        
        def draw_barcode(decoded, image):
           
            image = cv2.rectangle(image, (decoded.rect.left, decoded.rect.top), 
                                    (decoded.rect.left + decoded.rect.width, decoded.rect.top + decoded.rect.height),
                                    color=(0, 255, 0),
                                    thickness=5)
            return image
        
        if __name__ == "__main__":
            from glob import glob
            global testProd
            testProd = []
            decodedIMG = []
            barcodes = glob("product_0.jpg")
            for barcode_file in barcodes:
                # load the image to opencv
                img = cv2.imread(barcode_file)
                decodedIMG = decodeIMG(img)
                testProd.append(getProductTitleAllergies(decodedIMG[0].decode('utf-8')))
                list_item_name.append(testProd)
    barcoder()
        #https://www.thepythoncode.com/article/making-a-barcode-scanner-in-python
#---------------------------------------
# INPUT FILES
#---------------------------------------
# READ AND PREPARE PRODUCTS AND CUSTOMERS
products = pd.read_excel('allproducts_updated.xlsx')
# BIG TABLE WITH THE SHOPPING CARTS OF DIFFERENT USERS
customers_cart_big = pd.read_excel('userRatings.xlsx')
# # SMALLER CART FOR THE SAKE OF TESTING
# customers_cart_small = pd.read_excel('shortUserData.xlsx')

new_user = customers_cart_big[-2:-1]
new_user = new_user.reset_index(drop=True)


for each in new_user.columns:
    new_user[each] = 0 
new_user['Users'] = len(customers_cart_big)+1
customers_cart_big = pd.concat([customers_cart_big,new_user])

for _ in range(len(list_item_name)):
    strs = ''
    for each in list_item_name[_][0][0]['title']:
        strs = strs + each
        strs = strs.lower()


    customers_cart_big[strs] = 1

customers_cart_random = customers_cart_big.iloc[:, 1:]

#---------------------------------------
# Transpose matrix 
#---------------------------------------
customers_cart_random_Transposed = customers_cart_random.T

#---------------------------------------
# Run valued decomposition parameters tweakable
#---------------------------------------
SVD = TruncatedSVD(n_components=3, random_state=5)
resultant_matrix = SVD.fit_transform(customers_cart_random_Transposed)
resultant_matrix.shape
### correlation matrix
corr_mat = np.corrcoef(resultant_matrix)
corr_mat.shape



for _ in range(len(list_item_name)):
    col_idx = customers_cart_random.columns.get_loc(strs)
    selected_product_carbon = np.unique(products.loc[products['name'] == strs]["CO2/quantity"])

    corr_specific = corr_mat[col_idx]
    recommendations = pd.DataFrame({'corr_specific':corr_specific, 'name': customers_cart_random.columns})\
    .sort_values('corr_specific', ascending=False)
    
    recommendations = recommendations.iloc[1:,:]
    recommendations.name = recommendations.name.str.lower()
    #print('ts2')
#---------------------------------------
# Filter by diet and allergy
#---------------------------------------

    allergens = []
    diets = []
    #print('ts3')
    # TEST THAT USER IS VEGAN AND HAS MILK ALLERGIES
    user_diet = "vegan"
    user_allergies = "oats"
    #print('ts4')
    products.name = products.name.str.lower()
    for allergen in products.columns[12:15]:
        allergens.append(products.loc[products['name'] == strs].iloc[0,:].loc[allergen])
    #print('ts5')
    for diet in products.columns[7:11]:
        diets.append(products.loc[products['name'] == strs].iloc[0,:].loc[diet])
        
    category = products.loc[products['name'] == strs].iloc[0,:].loc["category"]
    
    df_merged = recommendations.merge(products,how='inner',on='name')
    
    rec_df = df_merged[(df_merged.category== category)]
    # rec_df = rec_df[rec_df['diet types']== user_diet]
    rec_df = rec_df[rec_df['allergens ']!=user_allergies]
    df_carbon = rec_df.sort_values("CO2/quantity", ascending=True)
    
 

    
    #next show only 3 products and ask user if he/she likes it
    #do you like the product? 
    df_carbon = df_carbon[['name', 'CO2/quantity']]
    print("The recommendations are: ")
    print(df_carbon.iloc[0:3])
    
    
    
    feedback = input('Do you like these products? ')
    asnwers = ['yes', 'no']
    feedback_answer = ''
    
    if feedback != 'yes':
        print(df_carbon.iloc[4:7])
        ble = input("Do you like these products? ")
        if ble == 'yes':
            f = input('Please pick one product: ')
            print('You have chosen ' + f +". Congrats, it has a lower carbon footprint than the scanned product")
            for x in f:
                feedback_answer = feedback_answer + x
                feedback_answer = feedback_answer.lower()
            customers_cart_big[feedback_answer] = 1
        else: 
             print(df_carbon.iloc[8:11])
             bla = input('Do you like these products? ')
             if bla == 'yes':
                 f1 = input('Please pick one product: ')
                 print('You have chosen ' + f1 +". Congrats, it has a lower carbon footprint than the scanned product")
                 for x in f1:
                    feedback_answer = feedback_answer + x
                    feedback_answer = feedback_answer.lower()
                 customers_cart_big[feedback_answer] = 1
             else: 
                 print(df_carbon.iloc[12:15])
                 bli = input('Do you like these products? ')
                 if bli != 'yes':
                     print(df_carbon.iloc[16:19])
                     blo = input('Please pick one product: ')
                 else: 
                     blau = input('Please pick one product: ')
                     print("You have chosen " + blau + '. Congrats, it has a lower carbon footprint than the scanned product!')
                     for x in blau:
                        feedback_answer = feedback_answer + x
                        feedback_answer = feedback_answer.lower()
                     customers_cart_big[feedback_answer] = 1
                
    else: 
        f2 = input('Please pick one product: ')
        print("You have chosen " + f2 + '. Congrats, it has a lower carbon footprint than the scanned product!')
        for x in f2:
            feedback_answer = feedback_answer + x
            feedback_answer = feedback_answer.lower()
        customers_cart_big[feedback_answer] = 1
    
    
    
  
customers_cart_big.to_excel("user_ratings_looped.xlsx")