import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_validate
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
import seaborn as sns
import matplotlib.pyplot as plt



election_data = pd.read_csv('/Users/niambashambu/Desktop/DS 2500/Homeworks/HW 3/data/1976-2020-president.tab', delimiter='\t')
demographic_data = pd.read_csv('/Users/niambashambu/Desktop/DS 2500/Homeworks/HW 3/data/demographics.csv')


#remake the state column to make them the same for both
demographic_data["state"] = demographic_data["STNAME"].str.upper()
print(demographic_data)



#filter the years for the two
election_data_2000 = election_data[election_data['year'] == 2000]
election_data_2004 = election_data[election_data['year'] == 2004]


# find the winners in the two elections
election_data_2000['winner'] = election_data_2000.groupby('state')['candidatevotes'].transform(max) == election_data_2000['candidatevotes']
election_data_2004['winner'] = election_data_2004.groupby('state')['candidatevotes'].transform(max) == election_data_2004['candidatevotes']
election_data_2000_winners = election_data_2000[election_data_2000['winner']][['state', 'party_detailed']]
election_data_2004_winners = election_data_2004[election_data_2004['winner']][['state', 'party_detailed']]

#find the percentages like it said in the document
demographic_data['percent_male'] = demographic_data['TOT_MALE'] / demographic_data['TOT_POP'] * 100
demographic_data['percent_female'] = demographic_data['TOT_FEMALE'] / demographic_data['TOT_POP'] * 100
demographic_data['percent_white'] = (demographic_data['WA_MALE'] + demographic_data['WA_FEMALE']) / demographic_data['TOT_POP'] * 100
demographic_data['percent_black'] = demographic_data['Black'] / demographic_data['TOT_POP'] * 100
demographic_data['percent_hispanic'] = demographic_data['Hispanic'] / demographic_data['TOT_POP'] * 100

# pick the relevant columns according to what he assignment said
demographic_features = demographic_data[['state', 'percent_male', 'percent_female', 'percent_white', 'percent_black', 'percent_hispanic']]



#merge the data
merged_data_2000 = pd.merge(election_data_2000_winners, demographic_features, on='state')
merged_data_2004 = pd.merge(election_data_2004_winners, demographic_features, on='state')
merged_data_2000 = merged_data_2000.sort_values(by='state')
merged_data_2004 = merged_data_2004.sort_values(by='state')

print(merged_data_2000)
#creating label for the knn classifier from the party_detailed column for both 2000 and 2004
label_encoder = LabelEncoder()
merged_data_2000['party_encoded'] = label_encoder.fit_transform(merged_data_2000['party_detailed'])

# Prepare features and target variable
X_2000 = merged_data_2000[['percent_male', 'percent_female', 'percent_white', 'percent_black', 'percent_hispanic']]
y_2000 = merged_data_2000['party_encoded']

merged_data_2004['party_encoded'] = label_encoder.transform(merged_data_2004['party_detailed'])
# Prepare features and target variable for 2004 data
X_2004 = merged_data_2004[['percent_male', 'percent_female', 'percent_white', 'percent_black', 'percent_hispanic']]
y_2004 = merged_data_2004['party_encoded']


optimal_k_recall = None
optimal_k_precision = None
highest_recall = 0
lowest_recall = np.inf
highest_precision = 0
lowest_precision = np.inf

recall_scores = []
precision_scores = []
# Loop through potential k values #used stack overflow to help me through the part as well as the provided documentation 
#this is for the year 2000
for k in range(4, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_results = cross_validate(knn, X_2000, y_2000, cv=KFold(n_splits=5, random_state=0, shuffle=True), scoring=['recall_macro', 'precision_macro'])
    
    mean_recall = np.mean(cv_results['test_recall_macro'])
    mean_precision = np.mean(cv_results['test_precision_macro'])


    recall_scores.append(mean_recall)
    precision_scores.append(mean_precision)

    
    # Update optimal k for recall
    if mean_recall > highest_recall:
        highest_recall = mean_recall
        optimal_k_recall = k
    if mean_recall < lowest_recall:
        lowest_recall = mean_recall
    
    # Update optimal k for precision
    if mean_precision > highest_precision:
        highest_precision = mean_precision
        optimal_k_precision = k
    if mean_precision < lowest_precision:
        lowest_precision = mean_precision

# Output the optimal k values and the lowest scores for recall and highest score for precision
print(f"Optimal k for recall: {optimal_k_recall}, Lowest mean recall: {lowest_recall}")
print(f"Optimal k for precision: {optimal_k_precision}, Highest mean precision: {highest_precision}")


X_train, X_test, y_train, y_test = train_test_split(X_2004, y_2004, random_state=0)

k_optimal = 5#number found optimal for precision
knn = KNeighborsClassifier(n_neighbors=k_optimal)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)
f1 = metrics.f1_score(y_test, y_pred, pos_label=1) #republician is 1
print("F1 Score for Republican label:", f1)

predicted_republican = (y_pred == 1).sum()
print("States predicted to vote Republican:", predicted_republican)

ohio_prediction = knn.predict(X_test)
ohio=ohio_prediction.sum()
vote = False
if ohio>=1:
    vote=True
print("Ohio's predicted vote:", vote)

# Confusion Matrix Heatmap
conf_matrix = metrics.confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix Heatmap')
plt.show()
#precision and recall plot
k_values = range(4, 11)
plt.figure(figsize=(8, 6))
plt.plot(k_values, recall_scores, marker='o', linestyle='-', color='blue', label='Recall')
plt.plot(k_values, precision_scores, marker='o', linestyle='-', color='green', label='Precision')
plt.title('Precision and Recall vs. K Value')
plt.xlabel('K Value')
plt.ylabel('Score')
plt.legend()
plt.grid(True)
plt.show()