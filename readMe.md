Steps to run the Project:
1. Create a virtual environment & activate it
    For Mac:
        conda create --name qrt
        conda config --add channels conda-forge
        conda config --set channel_priority strict
        conda activate minimal_ds
    For Windows:
        python3 -m venv qrt
        .\qrt\Scripts\activate

2. Run requirements.txt
    For Mac:
        conda install --yes --file requirements.txt
    For Windows:
        pip install -r requirements.txt

3. Run server.py file to start the flask application
    python server.py

4. Run app.py file to send a sample post request ro the server
    python app.py

5. Run Unit Tests
    python -m unittest tests/test_server.py
    python -m unittest tests/test_spaceship_rental.py

Description:
server.py -> Flask Application which runs on host='127.0.0.1' & port=8000
             Route /spaceship/optimize/ takes "input_payload" as input & returns the {'income': total_profit, 'path': path}
spaceship_rental.py -> Contains class SpaceshipRental & function spaceship_scheduling to calculaate the maximum profit

