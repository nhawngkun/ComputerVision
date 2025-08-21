import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt
img = cv.imread('messi5.jpg')
assert img is not None, "file could not be read, check with os.path.exists()"
#cv.imshow("Image", img)
#cv.waitKey()

#lấy tòa độ y=100 , x=100 rồi in ra màu tại px đó
px = img[100,100]
print( px )

# như trên nhưng chỉ lấy blue, vs blue=0 , gre=1, red=2
blue = img[100,100,0]
print( blue )

#cho bgr tại px đó bàng 255 ( trắng)
img[100,100] = [255,255,255]
print( img[100,100] )

# lấy kich thước ảnh [hàng, cốt, kênh màu]
print( img.shape )
# kich thước ảnh hàng * côy * kênh màu
print( img.size )
#kiểu dữ liệu
print( img.dtype )
#cắt ra một vùng ảnh hình chữ nhật y=340 - 280  x= 390 - 280 rôi lưu vào ball
ball = img[280:340, 330:390]
#gán vùng ảnh ball vào vị trí khác trên cùng ảnh
img[273:333, 100:160] = ball
#tách ảnh thành 3 kênh: Blue, Green, Red.
b,g,r = cv.split(img)
#ghép 3 kênh đó lại thành một ảnh màu.
img = cv.merge((b,g,r))

cv.imshow("Image", img)
cv.waitKey()


BLUE = [255, 0, 0]

img1 = cv.imread('logo.png')
assert img1 is not None, "file could not be read, check with os.path.exists()"
#cv.copyMakeBorder(src, top, bottom, left, right, borderType, value)

replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=BLUE)
#Hiển thị ảnh với matplotlib vs 231 là 2 hàng, 3 cột, vị trí 1.
plt.subplot(231), plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232), plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233), plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234), plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235), plt.imshow(wrap, 'gray'), plt.title('WRAP')
plt.subplot(236), plt.imshow(constant, 'gray'), plt.title('CONSTANT')

plt.show()
