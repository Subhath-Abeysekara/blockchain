from flask import Flask, request
from flask_cors import CORS, cross_origin
import handle_complain

app = Flask(__name__)
CORS(app, resources={r"/": {"origins": "*"}})

@app.route("/")
def main():
    return "Home"


@app.route("/addcomplain", methods=["POST"])
@cross_origin()
def addcomplain():
    try:
        if request.data:
            print(request.json)
            return handle_complain.add_complain(request.json)
        else:
            return {
                "state": False
            }
    except:
        return {
            "state": False
        }

@app.route("/getuser/<private_key>")
@cross_origin()
def getuser(private_key):
    try:
        return handle_complain.get_complain_by_user(private_key)
    except:
        return {
            "state": False
        }

@app.route("/getreviewer/<reviewer_id>")
@cross_origin()
def getreviewer(reviewer_id):
    try:
        return handle_complain.get_complain_by_reviewer(reviewer_id=reviewer_id)
    except:
        return {
            "state": False
        }

@app.route("/getadmin")
@cross_origin()
def getadmin():
    try:
        return handle_complain.get_complain_by_admin()
    except:
        return {
            "state": False
        }

@app.route("/addreviewer/<id>/<reviewer_id>")
@cross_origin()
def addreviewer( id,reviewer_id):
    try:
        return handle_complain.add_reviewer(id=id,reviewer_id=reviewer_id)
    except:
        return {
            "state": False
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)

