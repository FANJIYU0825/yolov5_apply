

import cv2

from retinaface import RetinaFace

import os
class Regnation:
    
    def __init__(self, filepath,savepath,filename,labelname,labelnum):
        self.filepath = filepath 
        self.savepath = savepath
        self.filename = filename
       
        self.labelname = labelname
        self.labelnum = labelnum

    def detectionmodel(self):
        detector = RetinaFace(quality="normal")
        self.img_bgr = cv2.imread(self.filepath, cv2.IMREAD_COLOR)
        self.img_rgb = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2RGB)

        self.detections = detector.predict(self.img_bgr)
        #[1,2,4]
        
    def labelregnation(self):
        dectect =[]
        try:
            dectect = self.detections

            imgshape = self.img_bgr
            
            arr =[]
        
            xmin=dectect[0]['x1']
            xmax=dectect[0]['x2']
            ymin=dectect[0]['y1']
            ymax=dectect[0]['y2']
            
            image_h=imgshape.shape[0]
            image_w=imgshape.shape[1]

            x = (xmin + (xmax-xmin)/2) *1.0/image_w
            y = (ymin + (ymax-ymin)/2) *1.0/image_h
            w = (xmax-xmin)*1.0/image_w
            h = (ymax-ymin)*1.0/image_h
            arr.append (' '.join ([str(self.labelnum),str(x),str(y),str(w),str(h)]))

            with open( self.savepath +self.filename+self.labelname+'.txt','w') as f :
            
                f.write('\n'.join(arr))
        except:
            dectect 
            os.remove(self.filepath)