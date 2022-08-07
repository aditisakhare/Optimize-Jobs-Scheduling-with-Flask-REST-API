from flask import Flask, jsonify, request
from spaceship_rental import SpaceshipRental
  
app = Flask(__name__)
  
@app.route('/spaceship/optimize/', methods = ['POST'])
def calculate_income():
    """
    Accepts the input payload and returns the json output
    """
    if(request.method == 'POST'):

        input = request.get_json()

        input_payload = input.get('input_payload', [])

        names, start, end, price = [], [], [], []

        for dict in input_payload:
            names.append(dict.get('name'))
            start.append(dict.get('start'))
            end.append(dict.get('start')+dict.get('duration'))
            price.append(dict.get('price'))

        rental = SpaceshipRental()
        total_profit, path = rental.spaceship_scheduling(names, start, end, price)


        return jsonify({'income': total_profit, 'path': path})
    
    return 'Use post request and provide the payload', 400

if __name__ == '__main__':
  
    app.run(host='127.0.0.1',port=8000, debug=True)