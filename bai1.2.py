import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt
img2 = cv.imread('logo.png')
assert img2 is not None, "file could not be read, check with os.path.exists()"
x = np.uint8([250])
y = np.uint8([10])
print( cv.add(x,y) )
print( x+y )

img1 = cv.imread ( 'ml.jpg' )

assert img1 is not None, "file could not be read, check with os.path.exists()"


# sẽ pix lại chiều dài chiểu rộng của ảnh 2 theo ảnh 1 y=0, x=1
img2 = cv.resize(img2, (img1.shape[1], img1.shape[0]))

#Trộn hình ảnh vs công thức dst=src1⋅α+src2⋅β+γ
dst = cv.addWeighted (img1,0.7,img2,0.3,0)
cv.imshow ( 'dst' ,dst)
cv.waitKey (0)
cv.destroyAllWindows ()


img3 = cv.imread('messi5.jpg')

assert img3 is not None, "file could not be read, check with os.path.exists()"

#Lấy kích thước của logo
#Tạo ROI từ góc trên-trái của ảnh chính với kích thước bằng logo
rows,cols,channels = img2.shape
roi = img3[0:rows, 0:cols]
cv.imshow ( 'roi' ,roi)

#Chuyển logo sang ảnh xám
img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow ( 'img2gray' ,img2gray )
cv.waitKey ()
#Tạo mask nhị phân: pixel > 10 → trắng (255), pixel ≤ 10 → đen (0)
ret, mask = cv.threshold(img2gray, 10, 255, cv.THRESH_BINARY)
cv.imshow ( 'mask' ,mask )
#Tạo inverse mask (đảo ngược): trắng → đen, đen → trắng
mask_inv = cv.bitwise_not(mask)



#Chèn ảnh mash vào ảnh roi với phần đen bị xóa đi phàn trắng giữ nguyên tuy nhiên vì có mask_inv nên logic hiên ở ảnh img3_bg sẽ có màu đen
img3_bg = cv.bitwise_and(roi,roi,mask = mask_inv)
cv.imshow ( 'img3_bg' ,img3_bg )

# bỏ đi bg của ảnh 2
img2_fg = cv.bitwise_and(img2,img2,mask = mask)
cv.imshow ( 'img2_fg' ,img2_fg )


#Kết hợp hai phần lại với nhau
dst1 = cv.add(img3_bg,img2_fg)
img3[0:rows, 0:cols ] = dst1

cv.imshow('res',img3)
cv.waitKey(0)
cv.destroyAllWindows()