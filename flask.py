from flask import Flask
app=Flask(__name__)

@app.route("/add-data",methods=["POST"])
def add_task():
    if not requests.json:
        return jsonify({
            "status":"error",
            "message":"Please provide the data"

        },400)
contact={
    'id':tasks[-1]['id']+1,
    'Name':requests.json['Name'],
    'Contact':request.json.get('Contact',"")
    'done':False
}
contact2={
    'id':tasks[-2]['id']+1,
    'Name':requests.json['Name'],
    'Contact':request.json.get('Contact',"")
    'done':False
    
}       
contact3={
    'id':tasks[-3]['id']+1,
    'Name':requests.json['Name'],
    'Contact':request.json.get('Contact',"")
    'done':False
} 

