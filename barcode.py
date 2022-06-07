from pyzbar import pyzbar
from getProductsAH import getProductTitleAllergies
import cv2

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
    ean_codes = []
    testProd = []
    decodedIMG = []
    barcodes = glob("cheeeeeese.jpg")
    for barcode_file in barcodes:
        # load the image to opencv
        img = cv2.imread(barcode_file)
        decodedIMG = decodeIMG(img)
        testProd.append(getProductTitleAllergies(decodedIMG[0].decode('utf-8')))

        
        
#https://www.thepythoncode.com/article/making-a-barcode-scanner-in-python