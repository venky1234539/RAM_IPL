
from flask import Flask, jsonify, request, redirect, url_for, render_template
from config import Config
from models import db,Ferry
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/home_view', methods = ['GET'])
def home_fun():
    # return jsonify(msg = "i love anushka")
    return " home page", 201

@app.route('/about', methods = ['GET'])
def abt_fun():
    return jsonify(msg="this is about function")

@app.route('/path_param/<int:id>', methods = ['GET'])
def pathparam_view(id):
    return jsonify(msg=f'path param is {id}')

@app.route('/query_param', methods = ['GET'])
def qparam():
    # name = request.args.get("name")
    # age =  request.args.get("age")                          first - single, we know key name and only once is present
    # return jsonify(msg = f'query params are {name}, {age}')
    # age =  request.args.get("age")
    # name = request.args.getlist("name")     second - if we have more than one key name, with multiple values, then we will get list of names
    # return jsonify(msg=f'query params are {name}, {age}')

    data = request.args.to_dict(flat=False)# third - if we dont know the key name and have duplicates in keys, then we will get all values in list
    return data                             # or it will give only one key value, flat = false , so that it will take all duplicates

@app.route('/insert_data', methods = ['POST'])
def idata():
    data = request.get_json(silent=True)
    # return " from http post"
    if not data:
        return jsonify(msg="please provide the details")
    fer_obj = Ferry(name=data.get("name"), age=data.get("age"))
    db.session.add(fer_obj)
    db.session.commit()   # while inserting the data, updating, deleting, we have to commit
    return jsonify(name=fer_obj.name, age=fer_obj.age), 201

@app.route('/redirect', methods = ['GET'])
def red_fun():
    return redirect(url_for("home_view"))

@app.route('/template', methods = ['GET'])
def temp_view():
    user_data = {"name" : "ram", "age" : 23}
    return render_template("demo.html", user=user_data)





if __name__ == "__main__":
    app.run(debug=True)






