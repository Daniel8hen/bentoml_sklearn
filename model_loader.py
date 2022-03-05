import bentoml
import numpy as np

# Load model
iris_clf_runner = bentoml.sklearn.load_runner("iris_clf:latest")

# Predict method
iris_clf_runner.run(np.array([5.9, 3. , 5.1, 1.8]))