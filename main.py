import cv2

img = cv2.imread('test.jpg', 0)
rows, cols = img.shape

for width in range(cols):
    for height in range(rows):
        pixel = img[height, width]
        print(f'Width: {width} - Height: {height} - Pixel: {pixel}')

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
