import cv2

img_path = 'image/Hanni_OLENS_2.jpg'

image = cv2.imread(img_path)

smoothed = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)

cvt_to_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(cvt_to_gray, 100, 200)

edges_inv = cv2.bitwise_not(edges)

anime_style = cv2.bitwise_and(smoothed, smoothed, mask=edges_inv)
anime_style = cv2.addWeighted(anime_style, 1, image, 0.1, 1)

cv2.imshow('image', anime_style)

cv2.waitKey()