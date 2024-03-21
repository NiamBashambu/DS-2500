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

# pick the relevant columns
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

# Loop through potential k values #used stack overflow to help me through the part as well as the provided documentation
for k in range(4, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    cv_results = cross_validate(knn, X_2000, y_2000, cv=KFold(n_splits=5, random_state=0, shuffle=True), scoring=['recall_macro', 'precision_macro'])
    
    mean_recall = np.mean(cv_results['test_recall_macro'])
    mean_precision = np.mean(cv_results['test_precision_macro'])
    
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


