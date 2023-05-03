from ML_Pipeline import utils
from ML_Pipeline import feature_engineering
from ML_Pipeline import recommendation
from ML_Pipeline import config
import pandas as pd
from projectpro import data_pipeline, model_snapshot

#read processed data which we stored after data preprocessing in the notebook
df=utils.read_csv_data(file_path=config.processed_data_path)

# splitting the dataframe into train and production set
train, production = utils.split_dataframe(df)

id_variables=config.id_variables
selected_variables= config.selected_variables

train_id=train[id_variables]
train_feat=train[selected_variables]

prod_id=production[id_variables]
prod_feat=production[selected_variables]

#creating new feature tenure
train_feat['tenure'] = train_feat['Month']- train_feat['Month of Joining']
prod_feat['tenure'] = prod_feat['Month']- prod_feat['Month of Joining']

train_label_data=train_feat[train_feat.columns.difference(['Customer ID','Month','Month of Joining'])]
prod_label_data=prod_feat[prod_feat.columns.difference(['Customer ID','Month','Month of Joining'])]
train_feat_enc, prod_feat_enc = feature_engineering.encode_categorical_features(train_label_data,prod_label_data)
data_pipeline("fcTel3")

##bringing back the customer ids keys
train_feat_enc['Customer ID'] = train_feat['Customer ID'] #bringing back the customer id
train_feat_enc['Month'] = train_feat['Month'] #bringing back the Month
train_feat_enc['Month of Joining'] = train_feat['Month of Joining'] #bringing back the Month of joining

prod_feat_enc['Customer ID'] = prod_feat['Customer ID'] #bringing back the customer id
prod_feat_enc['Month'] = prod_feat['Month'] #bringing back the Month
prod_feat_enc['Month of Joining'] = prod_feat['Month of Joining'] #bringing back the Month of joining

train = pd.merge(train_feat_enc,train_id[['Customer ID','Month','Month of Joining','Churn Value','offer']],how = 'inner',on=['Customer ID','Month','Month of Joining'])
production = pd.merge(prod_feat_enc,prod_id[['Customer ID','Month','Month of Joining','Churn Value','offer']],how = 'inner',on=['Customer ID','Month','Month of Joining'])

#if you want to recommend for entire production data then change the production.head(100) to production
model_snapshot("fcTel3")
frame_production_100_samples = recommendation.production_model (production.head(100),train=train,production=production,distance_func = config.distance_measure,n = config.n)
frame_production_100_samples.to_csv('../data/output/offer_recommendation_without_bootstap.csv',index=False)

frame_production_100_samples_bootstrap = recommendation.production_model_bootstrap (production.head(100),train=train,production=production,distance_funcs=config.distance_function_list,n_values=config.n_value_list)
frame_production_100_samples_bootstrap.to_csv('../data/output/offer_recommendation_bootstrap.csv',index=False)

print('Output Recommendation Saved...')




