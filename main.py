import json
import subprocess
from flask import Flask, request, jsonify
from flask_restx import Api, Resource, reqparse, Namespace


app = Flask(__name__)
api = Api(app)


#Create a sample api for hello

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'hello'


#Create api for image scan

@api.route('/imagescan')
class ImageScan(Resource):
    @api.doc(params={'imageurl': 'The Image url for scan'})
    def get(self):
        imageurl = request.args.get('imageurl')
        output = subprocess.check_output("trivy image " + imageurl + " -f json",shell=True)
        return output.decode("utf-8")


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0")


