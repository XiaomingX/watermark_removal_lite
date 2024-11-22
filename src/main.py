import cv2

def main():
    # 读取同目录下的 image.png 文件
    input_file = "image.png"
    output_file = "new_image.png"
    
    # 使用 OpenCV 加载图像
    image = cv2.imread(input_file)
    if image is None:
        print(f"Error: File '{input_file}' not found or cannot be opened.")
        return
    
    # 获取图像的高度和宽度
    height, width, _ = image.shape
    
    # 去掉最下面高度为20px
    if height > 100:
        cropped_image = image[:-100, :]
    else:
        print("Error: Image height is less than or equal to 20px, cannot crop.")
        return
    
    # 保存裁剪后的图像
    cv2.imwrite(output_file, cropped_image)
    print(f"New image saved as '{output_file}'.")

if __name__ == "__main__":
    main()
