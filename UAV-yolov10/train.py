from ultralytics import YOLOv10
model = YOLOv10(r'D:\yolov10-main\ultralytics\cfg\models\v10\Faster_DRB_SE.yaml')  # build a new model from YAML
if __name__=="__main__":
    model.train(data='datasets\Raruco\data.yaml', epochs=250 , name="train", batch=2, close_mosaic=0)
  
