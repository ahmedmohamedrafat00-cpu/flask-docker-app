from flask import Flask, request, jsonify

app = Flask(__name__)

# Route رئيسي
@app.route("/", methods=["GET"])
def home():
    return "<h1>Hello from Flask App!</h1>"

# مثال على API يعيد JSON
@app.route("/api/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    # host="0.0.0.0" مهم عشان يتم الاتصال من خارج الكونتينر أو من شبكة أخرى
    app.run(host="0.0.0.0", port=5000)
