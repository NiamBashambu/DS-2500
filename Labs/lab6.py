#lab6.py

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

wine = load_wine()


print(wine.feature_names)


X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, random_state=0)

knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(X_train, y_train)



wine_index = 89
wine_prediction = knn.predict([wine.data[ wine_index]])
wine_correct =  wine_prediction == wine.target[ wine_index]
print( wine_prediction)

all_pred = knn.predict(X_test)
accuracy = np.mean(all_pred == y_test)
incorrect_pred = np.sum(all_pred != y_test)

number_of_training_samples = X_train.shape[0]
print( wine_correct, number_of_training_samples, incorrect_pred, accuracy)

knn_2_features = KNeighborsClassifier(n_neighbors=6)
X_train_2_features = X_train[:, :2]
X_test_2_features = X_test[:, :2]
knn_2_features.fit(X_train_2_features, y_train)


pred_2_features = knn_2_features.predict(X_test_2_features)
plt.figure(figsize=(10, 6))
scatter = plt.scatter(X_test_2_features[:, 0], X_test_2_features[:, 1], c= pred_2_features)
plt.xlabel(wine.feature_names[0])
plt.ylabel(wine.feature_names[1])
plt.title('Scatter Plot of Test Data')
plt.legend(*scatter.legend_elements(), title="Classes")
plt.show()

