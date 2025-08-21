import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # --- Define màu ---
    # Xanh dương
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv.inRange(hsv, lower_blue, upper_blue)

    # Xanh lá
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask_green = cv.inRange(hsv, lower_green, upper_green)

    # Đỏ (cần 2 khoảng do vòng tròn HSV)
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 50, 50])
    upper_red2 = np.array([180, 255, 255])
    mask_red = cv.inRange(hsv, lower_red1, upper_red1) + cv.inRange(hsv, lower_red2, upper_red2)

    # --- Kết hợp mask ---
    combined_mask = cv.bitwise_or(mask_blue, mask_green)
    combined_mask = cv.bitwise_or(combined_mask, mask_red)

    # --- Áp dụng mask lên ảnh gốc ---
    result = cv.bitwise_and(frame, frame, mask=combined_mask)

    # Hiển thị
    cv.imshow('Original', frame)
    cv.imshow('Combined Mask', combined_mask)
    cv.imshow('Result', result)

    if cv.waitKey(5) & 0xFF == 27:  # ESC để thoát
        break

cap.release()
cv.destroyAllWindows()