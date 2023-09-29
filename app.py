from distutils.log import debug
from fileinput import filename
from flask import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!<h1>'

# upload page route
@app.route('/upload')  
def main():  
    return render_template("file_upload.html")  
  
# loading page route
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']
        f.save('../flask-react-app/temp/' + f.filename) # saves the uploaded file to /temp
        return render_template("loading_page.html", name = f.filename)
    



if __name__ == '__main__':
    app.run(debug=True)