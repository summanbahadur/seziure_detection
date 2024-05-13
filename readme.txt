Two models are trained
1 - Detecting Rodents , count and bounding boxes
2- Detecting Seziure on each rodent

!yolo task=detect mode=predict model=best.pt show=True conf=0.5 source=../test-vedioes/1.mp4