import torch

# Model

# Images
def predictionreulst():
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/best.pt', force_reload=True)