from flask import Flask,render_template,request
app = Flask(__name__)
import classifier as cl
import json

@app.route('/')
@app.route('/home')
def home():
    #cl.model_load()
    return render_template('home.html')

@app.route('/result', methods=['GET','POST'])
def result():

    if request.method == 'POST':

        image = request.files["pic"]
        image.save("static/uploads/"+image.filename)
        result = cl.classify(image.filename)
        print(result)
        if(result==1):
            ans="Benign"
            res=""
        else:
            ans="MALIGNANT"
            res="Cancer"  
        return render_template('result.html', imgname = image.filename, ans = ans,res=res)

if __name__ == "__main__":
    app.run(debug=True)