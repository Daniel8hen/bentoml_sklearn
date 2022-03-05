import bentoml

from sklearn import svm, datasets

# Load predefined training set to build an example model
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Model Training
clf = svm.SVC(gamma='scale')
clf.fit(X, y)

# Call to bentoml.<FRAMEWORK>.save(<MODEL_NAME>, model)
# In order to save to BentoML's standard format in a local model store
bentoml.sklearn.save("iris_clf", clf)
