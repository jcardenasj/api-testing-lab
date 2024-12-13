from flask import Flask, jsonify, request
from api.service import search_flights

app = Flask(__name__)

@app.route('/search_flights', methods=['GET'])
def search_flights_handler():
    origen = request.args.get('origen')
    destino = request.args.get('destino')
    fecha = request.args.get('fecha')
    
    if not origen or not destino or not fecha:
        return jsonify({"error": "Missing required query parameters"}), 400
    
    flights = search_flights(origen, destino, fecha)
    return jsonify(flights), 200

if __name__ == '__main__':
    app.run(debug=True)

    