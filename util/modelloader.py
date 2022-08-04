import torch
import pandas as pd

def predictionreulst(img):
    # I have change the package     
    model = torch.hub.load('FANJIYU0825/yolov5', 'custom', path='best.pt', force_reload=True)
    results = model(img)
    results.save("../img")
    frame=results.pandas().xyxy[0]
    df=pd.DataFrame(frame) 
    ytber= df['name'][0]
    d = pd.read_excel("name.xlsx")
#     print(ytber)
    for idx,key in enumerate(d['label']):
                if key == ytber:
                        trans=d['translation'][idx]
                        ins = d['Ins'][idx]
                        YT = d['YT'][idx]
    
#     print(trans)
    if trans:
         return YT,ins,trans,df
    else :    
         return YT,ins,"查無資料" ,df
        