from flask import Flask,jsonify,abort,make_response,request
from waitress import serve
import subprocess

api = Flask(__name__)
@api.route('/create',methods=['GET'])
def get():
    subprocess.run(['python3','convertE2Y.py'],shell=True)
    print('yamlファイルを作成しました。')
    return make_response('success')

@api.route('/ansible',methods=['GET'])
def get():
    subprocess.run(['ansible-playbook','mai.yaml'],shell=True)
    print('Ansibleを実行しました。')
    return make_response('success')

if __name__ == '__main__':
    serve(api,host='0.0.0.0',port=3000)