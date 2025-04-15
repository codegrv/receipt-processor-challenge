from flask import Flask, request, jsonify
from receipts import process_receipt, get_points

app = Flask(__name__)
receipt_store = {}

@app.route("/receipts/process", methods=["POST"])
def process():
    receipt = request.get_json()
    receipt_id, points = process_receipt(receipt)
    receipt_store[receipt_id] = points
    return jsonify({"id": receipt_id})

@app.route("/receipts/<string:receipt_id>/points", methods=["GET"])
def get_receipt_points(receipt_id):
    points = receipt_store.get(receipt_id)
    if points is None:
        return jsonify({"error": "Receipt ID not found"}), 404
    return jsonify({"points": points})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)