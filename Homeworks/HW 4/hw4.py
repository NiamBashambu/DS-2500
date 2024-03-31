


import json
import requests
import pandas as pd
import numpy as np
import json
import scipy.spatial.distance as ssd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA

from sklearn.cluster import KMeans


API_KEY = "48828f97cb2547a484a46134f02ba5b5"

URL = "https://newsapi.org/v2/everything?q=fortnite&apiKey=48828f97cb2547a484a46134f02ba5b5"

#getting the data and normalizing the dataframe
response = requests.get(URL)
data = response.json()
articles = data["articles"]
df = pd.json_normalize(articles)

#doing TD.IDF and PCA to get the PCA values needed
vectorizer = TfidfVectorizer(stop_words = "english")
vecotrized = vectorizer.fit_transform(df["title"])
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(vecotrized.toarray())
df[["pca1","pca2"]] = reduced_data

#found the optimal number using elbow method as seen below
K = 3
#assigning the centroids using the function created in class and creating the plot that will showcase this
def assign_centroids(df, centroids, x , y):
    centroid_assignments = []
    
    for i in range(len(df)):
        curr_point = df.iloc[i][[x, y]]
        min_dist = float("inf")
        min_centroid = -1
        
        for j in range(len(centroids)):
            curr_centroid = centroids[j]
            dist = ssd.euclidean(curr_point, curr_centroid)
            if dist < min_dist: 
                min_dist = dist
                min_centroid = j
        centroid_assignments.append(min_centroid)
    
    return centroid_assignments

centroids = df.sample(n = K)
centroids = [(df.iloc[i]["pca1"], df.iloc[i]["pca2"]) for i in range(len(centroids))]
assignments = assign_centroids(df, centroids, x = "pca1", y = "pca2")
df["cluster"] = assignments
df["color"] = np.select([df["cluster"] == 0, df["cluster"] == 1, df["cluster"] == 2],
                           ["orange", "dodgerblue", "firebrick"])
df.plot(kind = "scatter", x = "pca1", y = "pca2", c = "color")


#plt.show()

#using the elbow method on a graph to determine the optimal value for K
k_values = range(1, 11)
inertias = []

for k in k_values:
    model = KMeans(n_clusters=k, random_state=42)
    model.fit(df[["pca1","pca2"]])
    inertias.append(model.inertia_)

# Plotting the elbow plot
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertias, '-o')
plt.title('Elbow Method For Optimal k')
plt.xlabel('Number of clusters, k')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.grid(True)
plt.show()

#printing the cluster counts for each article
cluster_counts = df['cluster'].value_counts()
print(cluster_counts)