import cv2

# 设置输入和输出文件路径
input_path = "D:\\System folder\\Desktop\\1\\新建文件夹\\2.mp4"
output_path = "D:\\System folder\\Desktop\\1\\新建文件夹\\2_bw.mp4"

# 创建VideoCapture对象
cap = cv2.VideoCapture(input_path)

# 获取输入视频的帧率、宽度和高度
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象，用于输出处理后的视频
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 设置编码格式为MP4
out = cv2.VideoWriter(output_path, fourcc, fps, (1280, 720), False)  # 设置输出视频的尺寸为720p

# 逐帧处理视频并写入输出文件
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # 将每一帧转换为灰度图像
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 将每一帧缩放到720p
    resized_frame = cv2.resize(gray_frame, (1280, 720))
    # 写入输出文件
    out.write(resized_frame)

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()
