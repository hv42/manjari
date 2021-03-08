import pytesseract
# import PIL
# from PIL import Image, ImageEnhance, ImageOps
# import cv2

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# result = pytesseract.image_to_string(img)
# print(result.strip().split('\n'))

# Using Image: Open the original image and apply grayscale image with 'L' mode.
# img = Image.open('C:\\Users\\harithavhs\\Documents\\github\\indic\\landscape.jpg').convert('L')
# img.show()

# enhancer1 = ImageEnhance.Sharpness(img)
# enhancer2 = ImageEnhance.Contrast(img)

# Using cv2 module: Open image and convert image to grayscale
# img = cv2.imread('C:\\Users\\harithavhs\\Documents\\github\\indic\\landscape.jpg')

# grayimg = img
# height, width, channels = img.shape

# for h in range(height):
#     for w in range(width):
#         grayimg[h,w] = 0.3 * img[h,w][0] + 0.59 * img[h,w][1] + 0.11 * img[h,w][2]

#cv2.imshow('source image', img)
# cv2.imshow('gray image', grayimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


