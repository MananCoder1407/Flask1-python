# imorting the required things
from flask import request, jsonify, Flask;

# creating the app
FlaskApp = Flask('hello');

# creating the cntacts list
contacts = [
    {
        "Contact" : 123456789,
        "Name" : "ABC",
        "done" : False,
        "id" : 1,
    },
    {
        "Contact" : 987654321,
        "Name" : "DEF",
        "done" : False,
        "id" : 2,
    }
]

# jsonify is used to access the 2d list or dict data
@FlaskApp.route('/get-data', methods = ['GET'])
def get_data():
    return jsonify({
        "data" : contacts,
    })

@FlaskApp.route('/add-data', methods = ['POST'])
def add_data():
    if not request.json:
        return jsonify({
            'message' : 'Data not provided',
            'error' : '400',
        })
        
    contact = {
        "Contact" : request.json['Contact'],
        "Name" : request.json['Name'],
        "done" : False,
        "id" : request.json['id'],
    }
    
    contacts.append(contact);
    if request.json:
        return jsonify({
            'message' : 'User data addedd successfully',
            "currentData" : contacts,
        })
        
FlaskApp.run(debug = True);