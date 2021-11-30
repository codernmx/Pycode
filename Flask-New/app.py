from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/index',methods=['POST','GET'])
def hello_world():
    print('请求方式为------->', request.method)
    args = request.values.get("form")
    return jsonify(args=args)

    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)