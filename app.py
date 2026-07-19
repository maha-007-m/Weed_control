from flask import Flask,redirect, url_for, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('index.html')
@app.route('/prediction',methods=['GET','POST'])
def prediction():
    return render_template('prediction.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')
@app.route('/check', methods=['POST'])
def check():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    if not username or not password:
        return redirect(url_for('login'))
    if username == 'admin' and password == 'admin':
        return redirect(url_for('prediction'))
    return redirect(url_for('login'))

@app.route('/upload_file', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('img')
        if file is None or file.filename == '':
            return render_template('prediction.html', img=None, con='No file uploaded', discription='Please upload an image file to analyze.', effects='')

        weed = secure_filename(file.filename)
        con = 'Unable to classify image'
        discription = 'The uploaded image did not match any known crop or weed patterns. Please try a different image.'
        effects = 'No prediction is available for this file name.'

        print(weed)
        if "crop" in weed:
            con = "Detected Crop Disease"
            discription = "The crop is infected with a disease. Please take necessary actions to treat the disease and prevent further spread."
            effects = "The disease can cause reduced crop yield, poor quality produce, and economic losses for farmers. It can also affect the health of the soil and surrounding ecosystem."
            print(con)
        elif "Alien" in weed:
            con = "Detected Alien Invasion"
            discription = "The crop is under attack by an alien species. Please take necessary actions to protect the crops and prevent further damage."
            effects = "The alien invasion can cause significant damage to the crops, leading to reduced yield and economic losses for farmers. It can also disrupt the local ecosystem and biodiversity."
            print(con)
        elif "Apophytes" in weed:
            con = "Detected Apophytes Infestation"
            discription = "The crop is infested with apophytes. Please take necessary actions to control the infestation and prevent further damage."
            effects = "The apophytes infestation can cause reduced crop yield, poor quality produce, and economic losses for farmers. It can also affect the health of the soil and surrounding ecosystem."
            print(con)
        elif "Lambsquarters" in weed:
            con = "Detected Lambsquarters Infestation"
            discription = "The crop is infested with lambsquarters. Please take necessary actions to control the infestation and prevent further damage."
            effects = "The lambsquarters infestation can cause reduced crop yield, poor quality produce, and economic losses for farmers. It can also affect the health of the soil and surrounding ecosystem."
            print(con)
        elif "Canada" in weed:
            con = "Detected Canada Thistle Infestation"
            discription = "The crop is infected with a disease. Please take necessary actions to treat the disease and prevent further spread."
            effects = "The Canada Thistle infestation can cause reduced crop yield, poor quality produce, and economic losses for farmers. It can also affect the health of the soil and surrounding ecosystem."
            print(con)
        elif "Curled" in weed:
            con = "Detected Curled Weed Infestation"
            discription = "The crop is infested with curlew weed. Please take necessary actions to control the infestation and prevent further damage."
            effects = "The curlew weed infestation can cause reduced crop yield, poor quality produce, and economic losses for farmers. It can also affect the health of the soil and surrounding ecosystem."
            print(con)

        file.save(os.path.join(app.config['UPLOAD'], weed))
        img = os.path.join(app.config['UPLOAD'], weed)
        return render_template('prediction.html', img=img, con=con, discription=discription, effects=effects)
    return render_template('prediction.html')
if __name__ == "__main__":
    app.run()