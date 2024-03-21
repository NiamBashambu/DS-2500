import pandas as pd
from sklearn.model_selection import train_test_split, KFold, cross_val_score
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
