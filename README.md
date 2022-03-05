# bentoml_sklearn
BenoML Service for ML Hosting using a dummy model + data from Scikit Learn.
<br>
The repo contains:
* `client.py` - A simple python file for sending a request and getting a response.
* `model_loader.py` - A python file which uses bentoml model storage and loads a model, alongside sending a dummy predict method.
* `model_trainer_saver.py` - A python file which trains a classification model (C-Support Vector Classification), and saves it in bentoml storage.
* `requirements.txt` - self explanatory


Installation tutorial:
* clone project
* install requirements with `pip install -r requirements.txt`
* Build using `bentoml serve iris_cls:latest --production`. Note: there might be a bug [here](https://github.com/bentoml/BentoML/issues/2313), per March 5th, 2022.
