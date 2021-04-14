This repository is for testing the deployment of ML models. For example use and my own personal use, I will be using an ML model and data from my phishing project.

### Quick start:
To install the required libraries, simply run: 'pip install -r requirements.txt' while in your desired virtual environment

Model fitting:
Within fit-model.ipynb, specify the data for the model pipeline to be fit on as X and y, then split the data using train-test-split and fit using the pipe.fit command.
You can pickle your fit model using the pickle command in the second to last cell

Using model test file:
To test on the pickled model save the desired number of rows to be fed into the model from the data as a list in the variable 'newdata'.
Use the cell containing the json.dump() to save the selected rows as 'newdata.json'
With the data saved, from a shell, navigate to the directory containing the .py files and run 'python test_pickled_model.py'

Starting the Flask Server:
Open a shell to the directory where the repository is saved.
Run the following command to set Flask to run the ML app: 'export FLASK_APP=app.py'
Then use the following command to start the server: 'flask run'

Feeding the JSON data into the server to recieve predictions using test_flask.py:
In a shell from the project directory, simply enter the command: 'python test_flask.py'
