# UAV-YOLOv10 Description--------------------------------
We proposed an improved UAV autonomous landing mark detection algorithm based on yolov10, and completed deployment, training and use in Windows. The improved network structure is detailed in Faster_DRB_SE.yaml.

# Experimental setup --------------------------------
In this study, all experiments were conducted in the same environment. The operating system used was Windows 10 64-bit, with Python version 3.9.19, PyTorch version 1.13.1, and CUDA version 11.7. The CPU was an Intel Core i7-7700, and the GPU was a GeForce GTX 1660 Ti. The experimental dataset was uniform, with a resolution of 640×640. The training cycle was set to 250 epochs, and the batch size was 2. The optimizer, learning rate, and weight parameters used for model training followed the default settings.

# Download --------------------------------
datasets:https://github.com/MengmingWu/UAV-datasets
When using, create a datasets/Raruco directory in the project folder and place all the files of the datasets in this directory.

# Training --------------------------------
from ultralytics import YOLOv10
model = YOLOv10('UAV-yolov10\ultralytics\cfg\models\v10\wmm_Faster_DRB_SE.yaml')  # build a new model from YAML
if __name__=="__main__":
    model.train(data='datasets\Raruco\data.yaml', epochs=250 , name="train_wmm_Faster_DRB_SE", batch=2, close_mosaic=0)

# Required dependencies --------------------------------
torch==2.0.1
torchvision==0.15.2
onnx==1.14.0
onnxruntime==1.15.1
pycocotools==2.0.7
PyYAML==6.0.1
scipy==1.13.0
onnxsim==0.4.36
onnxruntime-gpu==1.18.0

# Citation --------------------------------
Paper title: "Enhanced UAV Autonomous Landing through YOLOv10-based Marker Detection with Lightweight and Context-aware Network"
Submitted to "The Vision Computer"
