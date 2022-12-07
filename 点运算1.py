# 数字图像处理 点运算
import cv2
import matplotlib.pyplot as plt
import numpy as np
img = cv2.imread('1.jpg',0)

# 获取图像的高度和宽度
height, width= img.shape

# 创建一副图像， uint8 是专门用于存储各种图像的（包括RGB, 灰度图像等）， 范围是从0-255
result = np.zeros((height,width), np.uint8)

# 图像灰度上移变换 DB = DA + 50
for i in range(height):
    for j in range(width):
        gray = int(img[i, j]) + 50
        if gray > 255:
            gray = 255
        result[i, j] = np.uint8(gray)

# 显示图像
plt.figure(num='comparison')
titles = ['gray Image', 'gray upshift transformation']
images = [img, result]
for i in range(2):
    plt.subplot(1,2,i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()