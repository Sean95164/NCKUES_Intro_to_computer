import cv2 as cv
import numpy as np

# 讀取原始圖片
def read_image(filepath):
    image = cv.imread(filepath)
    return image

# 暫停 opencv 的視窗
def pause():
    cv.waitKey(0)
    cv.destroyAllWindows()

# 使用 opencv 內部的函式將圖片轉成灰階
def BGRtoGRAY_1(img):
    gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    return gray_image

# 手動計算 RGB 的比例將圖片轉成灰階
def BGRtoGRAY_2(img):
    w = np.array([ 0.114, 0.587,  0.299])
    # 0.299*R + 0.587*G + 0.114*B
    # 將圖片每個像素的 RGB 乘上對應參數並且將加，再轉換成 8-bit type
    # gray = cv.convertScaleAbs(np.sum(img*w, axis=2))
    gray = np.sum(img*w, axis=2, dtype=np.uint8)
    return gray

# 將以轉成灰階的圖片二值化
def binarization(img):
    _,thresh1 = cv.threshold(img,245,255,cv.THRESH_BINARY)
    return thresh1

def main():
    # 檔案的相對路徑
    filepath = "TW.jpg"

    # 讀取原始圖片
    original = read_image(filepath)
    cv.imshow("original", original)

    # 使用內建函式將圖片轉灰階
    grayscale_image1 = BGRtoGRAY_1(original)
    cv.imshow("grayscale_image1", grayscale_image1)

    # 手動計算圖片轉灰階
    grayscale_image2 = BGRtoGRAY_2(original)
    cv.imshow("grayscale_image2", grayscale_image2)

    # 將灰階圖片進行二值化
    binarized_image = binarization(grayscale_image1)
    cv.imshow("binarized_image", binarized_image)

    # 暫停視窗
    pause()

# 執行主程式
main()