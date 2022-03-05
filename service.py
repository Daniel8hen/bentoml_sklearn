# service.py
import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

latest_iris_classifier = "iris_clf:latest"
# Load the runner for the latest ScikitLearn model we just saved
iris_clf_runner = bentoml.sklearn.load_runner(latest_iris_classifier)

# Create the iris_classifier service with the ScikitLearn runner
# Multiple runners may be specified if needed in the runners array
# When packaged as a bento, the runners here will included
svc = bentoml.Service(latest_iris_classifier.split(':')[0], runners=[iris_clf_runner])

# Create API function with pre- and post- processing logic with your new "svc" annotation
@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    # Define pre-processing logic
    result = iris_clf_runner.run(input_series)
    # Define post-processing logic
    return result