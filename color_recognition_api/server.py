import os
from flask import Flask, request
# import color_classification_image
from color_classification_image import image
from color_classification_webcam import cam
UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if request.form.get("submit"):
            if 'file1' not in request.files:
                return 'there is no file1 in form!'
            file1 = request.files['file1']
            path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
            file1.save(path)
            # image()
            image(path)
        # return "uploaded"
        if request.form.get("submit_a"):
            cam()

    # do something
        # return 'ok'

    # def c():
    #     cam()
    return '''
        <html>
            <head>
    <div>
        <h1>Upload new File</h1>
        <form method="post" enctype="multipart/form-data">
          <input type="file" name="file1">
          <input type="submit">
        </form>
        </div>
        <div>
        <h1>webcam</h1>
    
        <form method ="post" action="/">
        <button type="submit" name="Open Webcam" value="submit_a"> Open Webcam </button>
        </form> 
        </div>
    '''
# @app.route('/')
# def webcam():
#     return '''
#         <h1>Webcam</h1>
#         <button onclick="myFunction()">Click me</button>
#
#         '''


if __name__ == '__main__':
    app.run()