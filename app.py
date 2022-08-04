from distutils import file_util
from flask import Flask, request, render_template,url_for,request,redirect,flash
import os
from PIL import Image
import util.modelloader as modelloader
import io
from flask_wtf.file import FileField, FileAllowed, FileRequired
import os
# from flask_uploads import UploadSet, IMAGES, configure_uploads
# model = modelloader.predictionreulst  

from werkzeug.datastructures import MultiDict,FileStorage
from flask_wtf import FlaskForm
from wtforms import SubmitField
from werkzeug.utils import secure_filename



app = Flask(__name__)
  
  
# Route for seeing a data
UPLOAD_FOLDER = "static/orgin"
app.config['SECRET_KEY'] = 'development'
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER
app.config['UPLOADED_DEF_URL'] = '\\img'

# abc = UploadSet(name='def', extensions=IMAGES)
# class FormUploads(FlaskForm):
#     btn_uploads = FileField('uploads', validators=[
#         FileAllowed(abc, 'IMAGE ONLY'),
#         FileRequired('IMAGE REQUIRED PLEASE')
#     ])
#     submit = SubmitField('Upload_IMG')

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template("index.html",fileupload =True )

@app.route('/data', methods=['POST'])
def uploads():
    if request.method == 'POST':
        file = request.files['file']
  
       
        if file :
            filename = secure_filename(file.filename)
            print("save")
            user_image = 'static/orgin/'+file.filename
            print(user_image)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],file.filename))
            print("save fin")
            YT,ins,predic,dataframe =  modelloader.predictionreulst(user_image)
            dectecpath = 'static/img/'
            dectdir= [ i for i in os.listdir(dectecpath) if i is not i.endswith('.jpg')]
            imgpa=[ i for i in os.listdir(dectecpath+dectdir[-1])]

            imgdect = imgpa[-1]
            imgdect ='img/'+ dectdir[-1]+"/"+file.filename
            
            return render_template("index.html",predic = predic,user_image = imgdect,ins_url =ins,chanel = YT)
       
        

        # return render_template('index.html',user_image= user_image)
    



if __name__ == '__main__':
    # model=modelloader.predictionreulst()
    # model.eval()
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)