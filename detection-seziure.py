
from IPython import display
from IPython.display import Image
import ultralytics
from ultralytics import YOLO
import cv2


vedio_path = './Chloroform + PTZ Acute study video-Small.mp4'


cap = cv2.VideoCapture(vedio_path)

if not cap.isOpened():
    print("Error: Unable to open video file")
    exit()

model=YOLO("./best.pt")

ret = True

while ret:
  ret, frame = cap.read()
  if not ret:
        break
  results = model.track(frame, persist=True)
  frame_ = results[0].plot()
  cv2.imshow('frame',frame_)
  if cv2.waitKey(25) & 0xFF == ord('q'):
        break
