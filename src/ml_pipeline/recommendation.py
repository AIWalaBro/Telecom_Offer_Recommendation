import pandas as pd
from ml_pipeline.model import *
from projectpro import model_snapshot
model_snapshot("fcTel3")

def production_model (df,train, production,distance_func,n):
  frame = pd.DataFrame()
  # For each customer in each month
  for customer in list(df['Customer ID'].unique()):
    for month in list(df[df['Customer ID']==customer]['Month'].unique()):
      #This part of the code adds the line we want to get offers to the training set, so we can use the distance formula
      data = pd.DataFrame()
      data = train.append(production[(production['Customer ID']==customer)&(production['Month']==month)])
      data= data.reset_index()
      data_id=data[['Customer ID', 'Month', 'Month of Joining','Churn Value']]
      results = get_recommended_offers(data,data_id,customer,month,distance_func,n,minimal_threshold=0.10,max_offers_to_return=3)
      data = {'Customer ID': [customer],
              'Month': [month],
              'offers': [results]}
      frame1 =  pd.DataFrame(data)
      frame = frame.append(frame1)
  return frame


def production_model_bootstrap (df,train,production,distance_funcs,n_values):

  frame = pd.DataFrame()
  for customer in list(df['Customer ID'].unique()):
    for month in list(df[df['Customer ID']==customer]['Month'].unique()):
      #This part of the code adds the line we want to get offers to to the training set, so we can use the distance formula
      data = pd.DataFrame()
      data = train.append(production[(production['Customer ID']==customer)&(production['Month']==month)])
      data= data.reset_index()
      data_id=data[['Customer ID', 'Month', 'Month of Joining','Churn Value']]
      results = find_similar_customers_multiple(data,data_id,customer,month,distance_funcs=distance_funcs,n_values=n_values,minimal_threshold=0.10,max_offers_to_return=3)
      data = {'Customer ID': [customer],
              'Month': [month],
              'offers': [results]}
      frame1 =  pd.DataFrame(data)
      frame = frame.append(frame1)
  return frame   