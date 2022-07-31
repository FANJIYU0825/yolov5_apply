from flask import Flask, request, render_template,url_for,request
import datetime
  
x = datetime.datetime.now()
  
# Initializing flask app
app = Flask(__name__)
  
  
# Route for seeing a data
@app.route("/")#主頁面
def index():
    
    return render_template ('index.html' )

@app.route('/data')
def get_time():
  
    # Returning an api for showing in  reactjs
    return {
        'Name':"geek", 
        "Age":"22",
        "Date":123, 
        "programming":"python"
        }
  
# @app.route('/label')
# def get_time():
  
#     # Returning an api for showing in  reactjs
#     return {
       
#         }
  
        
# Running app
if __name__ == '__main__':
    app.run(debug=True)