# 基于机器学习的行人识别系统毕业设计
## 功能实现
### 登陆系统
- 支持默认用户名登录密码通过sha256加密
### 单路监控
#### 从摄像头识别
- 当文件源为空时自动进入摄像头识别，默认识别内容为人脸以及行人，支持侧载数据集与模型。输入自定义数据集后会自动识别目标，默认名称为XML_Model，识别过程中会显示实时帧率，CPU/GPU/MEM占用。
#### 从文件识别
- 输入文件源自动进入识别界面，仅支持mp4格式文件
### 多路监控
- 输入文件路径进入视频合成，由于计算机性能瓶颈，目前限定为四路视频识别，在目标路径中寻找到四路视频，合成为同一画面后自动识别，该功能为CPU密集型，出现未响应为正常现象
### 高级识别
-  实现更多类型的目标检测，支持GPU加速，支持基于YOLOv5的深度学习模型构造，支持目标流动数量检测
### 模型训练
#### 本地训练
- 选择80%的文件为训练集剩余的为测试集，调用tensorflow训练编译模型，训练文件保存到该目录下，标签为model_wedgits，名称为model.h5格式
#### 连接到服务器
- 由于需求量以及网络环境要求高，暂时关闭该功能
### 出错处理
- 本系统会对输入路径进行验证，严重的问题会弹出警告窗口
- 一般的信息会通过Windows API进行通知推送
### 使用框架
- https://github.com/Sharpiless/Yolov5-deepsort-inference
- https://github.com/ultralytics/yolov5/
- https://github.com/ZQPei/deep_sort_pytorch
- https://github.com/dyh/unbox_yolov5_deepsort_counting

**北方工业大学**
**计19-3**
**钱晟**

### 可通过以下方式联系我
- mail:xinyaoqian694@gmail.com
- github:https://github.com/Xinyao0512
- twitter:@qian2697581590

# Graduation design of pedestrian recognition system based on machine learning
## Function realization
### login system
- Support default user name login password encrypted by sha256
### Single channel monitoring
#### Identify from camera
- When the file source is empty, it automatically enters the camera recognition. The default recognition content is faces and pedestrians. It supports sideloading datasets and models. After entering the custom data set, the target will be automatically recognized. The default name is XML_Model. During the recognition process, the real-time frame rate and CPU/GPU/MEM occupancy will be displayed.
#### Identify from file
- The input file source automatically enters the recognition interface, and only supports mp4 format files
### Multichannel monitoring
- The input file path enters the video synthesis. Due to the computer performance bottleneck, it is currently limited to four-channel video recognition. Four channels of video are found in the target path, and are automatically recognized after being synthesized into the same image. This function is CPU-intensive, and non-response is normal
### Advanced Identification
- Achieve more types of target detection, support GPU acceleration, support deep learning model construction based on YOLOv5, and support target flow quantity detection
### Model training
#### Local training
- Select 80% of the files as the training set and the rest as the test set, call tensorflow to train and compile the model, and save the training file to this directory with the label model_wedgits and the name model.h5 format
#### Connect to server
- Due to the high demand and network environment requirements, this function is temporarily closed
### Error handling
- The system will verify the input path, and a warning window will pop up for serious problems
- General information will be notified and pushed through Windows API
### Using Frames
- https://github.com/Sharpiless/Yolov5-deepsort-inference
- https://github.com/ultralytics/yolov5/
- https://github.com/ZQPei/deep_sort_pytorch
- https://github.com/dyh/unbox_yolov5_deepsort_counting

**North China University of Technology**
**Computer Science 19-3**
**Sheng Qian**

### You can contact me in the following ways
- mail:xinyaoqian694@gmail.com
- github:https://github.com/Xinyao0512
- twitter:@qian2697581590

# 機械学習に基づく歩行者識別システム卒業設計
## 機能実装
## ログインシステム
- sha256 で暗号化されたデフォルトのユーザー名ログイン パスワードをサポート
### シングルパスモニタ
#### カメラから認識
- ファイル ソースが空の場合、自動的にカメラ認識に入ります. デフォルトの認識コンテンツは顔と歩行者です. データセットとモデルのサイドローディングをサポートします. カスタム データ セットを入力すると、ターゲットが自動的に認識されます。デフォルト名は XML_Model です。認識プロセス中、リアルタイムのフレーム レートと CPU/GPU/MEM 占有率が表示されます。
#### ファイルから識別
- 入力ファイルソースは自動的に識別インタフェースに入り、mp4形式ファイルのみをサポートする
### 多重監視
- 入力ファイルパスはビデオ合成に入り、コンピュータ性能のボトルネックのため、現在は4ウェイビデオ認識に限定され、目標パスの中で4ウェイビデオを探し、同じ画面に合成すると自動的に認識される。この機能はCPU密集型で、未応答が正常な現象が現れる
### 高度な識別
- より多くのタイプの目標検出を実現し、GPU加速をサポートし、YOLOv 5に基づく深さ学習モデル構造をサポートし、目標流動量検出をサポートする
### モデルトレーニング
#### ローカルトレーニング
- ファイルの 80% をトレーニング セットとして選択し、残りをテスト セットとして選択し、tensorflow を呼び出してモデルをトレーニングおよびコンパイルし、このディレクトリにトレーニング ファイルを model_wedgits というラベルと model.h5 形式の名前で保存します。
#### サーバに接続
- 需要が高く、ネットワーク環境要件が高いため、この機能は一時的に閉鎖されています
### エラー処理
- このシステムは入力パスを検証し、重大な問題は警告ウィンドウをポップアップします
- 一般的な情報はWindows APIを介して通知プッシュされます
### フレームワークの使用
- https://github.com/Sharpiless/Yolov5-deepsort-inference
- https://github.com/ultralytics/yolov5/
- https://github.com/ZQPei/deep_sort_pytorch
- https://github.com/dyh/unbox_yolov5_deepsort_counting


**北方工業大学**
**情報科学19-3**
**銭晟**

###### 以下の方法で私に連絡することができます
- mail:xinyaoqian694@gmail.com
- github:https://github.com/Xinyao0512
- twitter:@qian2697581590

# ZH_Hans/EN_US/JA_jp readme 
