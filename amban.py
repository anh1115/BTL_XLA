import cv2

# Đọc ảnh từ file
image = cv2.imread('img/meo.jpg')

# Chuyển ảnh sang ảnh âm bản
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Lưu ảnh âm bản thành một file mới
cv2.imwrite('img/meo_am_ban.jpg', gray_image)

# Hiển thị ảnh âm bản (nếu cần)
cv2.imshow('Ảnh âm bản', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
