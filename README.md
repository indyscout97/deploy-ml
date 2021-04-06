This repository is for testing the deployment of ML models.

Quick start:
To install the required libraries, simply run: 'pip install -r requirements.txt' while in your desired virtual environment

Model fitting:
Within fit-model.ipynb, specify the data for the model pipeline to be fit on as X and y, then split the data using train-test-split and fit using the pipe.fit command.
You can pickle your fit model using the pickle command in the second to last cell

Using model test file:
To test on the pickled model, create a new file called newdata.py. Within this file, save the desired number of rows from the data as a list in the variable 'newdata'.
With the data saved, from a shell, navigate to the directory containing the .py files and run 'python test_pickled_model.py'
