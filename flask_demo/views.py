import json

from flask import  render_template,request,jsonify
import os
from flask import Flask

#importing decarator from seperate file
from deca import login_required

app = Flask(__name__)


app.config['SECRECT_KEY'] = '0r7iynyhyls6#ow2_$e&6$x05je2b6zzxwb290'
app.secret_key = os.urandom(12)
custom_key = "0r7iynyhyls6ow2_$eia29012"

@app.route("/home", methods=['GET'])
@login_required
def employee_profile():
    data={}
    return render_template('index.html', data=data)


if __name__ == '__main__':
   app.run(debug = True, host='0.0.0.0',port=8000)





