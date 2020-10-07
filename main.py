from flask import Flask
from flask import render_template
from flask import request
import yaml

def get_yaml_data(yaml_file='_conf.yml'):
    # 打开yaml文件
# 直接打开读出来
    f = open(yaml_file,'r',encoding='utf-8')
    result = f.read()
    # 转换成字典读出来
    a = yaml.load(result,Loader=yaml.FullLoader)
    return a
conf = get_yaml_data()

readUser = conf.get("username")
readPassword = conf.get("password")
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def index():

    if request.method=="POST":
        user = request.form['user']
        password = request.form['password']
        if user == readUser and password==readPassword:
            return render_template('_temp/index.html',user=user
        )

    else:
        return render_template('_temp/layout.html')
@app.errorhandler(500)
def internal_server_error(e):
    return render_template("_temp/500.html"),500

if __name__=='__main__':
    app.run()
