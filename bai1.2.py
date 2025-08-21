import cv2 as cv

images = ['messi5.jpg', 'logo.png', 'ml.jpg']  # thêm các ảnh khác
logo_path = 'cat.png'

# Đọc logo và tạo mask
logo = cv.imread(logo_path)
assert logo is not None, "Logo không tồn tại"
logo = cv.resize(logo, (100, int(100 * logo.shape[0]/logo.shape[1])))
logo_gray = cv.cvtColor(logo, cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(logo_gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)
lh, lw = logo.shape[:2]

# Kích thước ảnh đầu tiên
first_img = cv.imread(images[0])
h, w = first_img.shape[:2]

cv.namedWindow('Slideshow', cv.WINDOW_NORMAL)

while True:
    for i in range(len(images)):
        img1 = cv.imread(images[i])
        img1 = cv.resize(img1, (w, h))
        img2 = cv.imread(images[(i+1) % len(images)])
        img2 = cv.resize(img2, (w, h))

        # Fade giữa hai ảnh
        for alpha in [x/20.0 for x in range(21)]:
            beta = 1.0 - alpha
            dst = cv.addWeighted(img1, beta, img2, alpha, 0)

            # Chèn logo vào góc trên bên trái
            roi = dst[0:lh, 0:lw]
            dst_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
            logo_fg = cv.bitwise_and(logo, logo, mask=mask)
            dst[0:lh, 0:lw] = cv.add(dst_bg, logo_fg)

            cv.imshow('Slideshow', dst)
            key = cv.waitKey(50)
            if key == 27:  # ESC để thoát
                cv.destroyAllWindows()
                exit()