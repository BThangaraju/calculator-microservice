from flask import Flask, request, jsonify
app = Flask(name)
@app.route('/add', methods=['GET']) def add(): a = int(request.args.get('a', 0)) b = int(request.args.get('b', 0)) return jsonify({"result": a + b})
@app.route('/subtract', methods=['GET']) def subtract(): a = int(request.args.get('a', 0)) b = int(request.args.get('b', 0)) return jsonify({"result": a - b})
if name == 'main': app.run(host='0.0.0.0', port=5000)
