import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def plot_image(index, img, strName,color='viridis'):
    """
    绘制图像并设置子图属性。

    参数：
    - index: 子图的索引
    - img: 要绘制的图像（RGB 格式）
    - strName: 子图的标题
    """
    plt.subplot(index), plt.imshow(img,color), plt.title(strName)
    plt.xticks([]), plt.yticks([])


def padding_image_with_black(img, scale):
    # 获取图像的原始尺寸
    height, width = img.shape[:2]

    # 计算新的尺寸
    new_height = int(height * scale)
    new_width = int(width * scale)

    # 创建新的黑色背景图像
    background = np.zeros((new_height, new_width, 3), dtype=np.uint8)

    # 计算图像在新背景中的起始坐标
    start_x = (new_width - width) // 2
    start_y = (new_height - height) // 2

    # 将原始图像复制到背景图像中心的相应位置
    background[start_y:start_y+height, start_x:start_x+width] = img

    # 返回结果图像
    return background





def AddSaltPepperNoise(src, rate):
    """
    给输入图像添加椒盐噪声。

    参数：
        - src: 输入图像
        - rate: 噪声比例，取值范围为 [0, 1]

    返回值：
        添加了椒盐噪声的图像副本
    """
    srcCopy = src.copy()
    height, width = srcCopy.shape[0:2]
    noiseCount = int(rate * height * width / 2)

    # 添加椒盐噪声
    # 添加白色噪声（椒噪声）
    X = np.random.randint(width, size=(noiseCount,))
    Y = np.random.randint(height, size=(noiseCount,))
    srcCopy[Y, X] = 255

    # 添加黑色噪声（盐噪声）
    X = np.random.randint(width, size=(noiseCount,))
    Y = np.random.randint(height, size=(noiseCount,))
    srcCopy[Y, X] = 0

    return srcCopy


def AddGaussNoise(src, sigma):
    """
    向图像添加高斯噪声
    :param src: 输入图像
    :param sigma: 高斯噪声的标准差，控制噪声强度
    :return: 添加噪声后的图像
    """
    mean = 0
    # 获取图片的高度和宽度
    height, width = src.shape[0:2]
    if len(src.shape) == 2:  # 处理灰度图像，没有通道维度
        gauss = np.random.normal(mean, sigma, (height, width))
        noisy_img = np.uint8(src + gauss)
    else:  # 处理彩色图像，有通道维度
        channels = src.shape[2]
        gauss = np.random.normal(mean, sigma, (height, width, channels))
        noisy_img = np.uint8(src + gauss)
    return noisy_img