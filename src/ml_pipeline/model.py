import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity, euclidean_distances, manhattan_distances


def get_recommended_offers (df:pd.DataFrame, df_id:pd.DataFrame,customer_id:str,month:int,distance_func:str,n,minimal_threshold:float,max_offers_to_return:int):
    """
    This function takes as parameters:
    1. the dataframe where we'll be getting our data
    2. the customer identifiers Customer Id and the Month we want to make an offer for
    3. the distance function we want to use to calculate similaries between customers (see explanation below on how to chose it)
    4. The number of other customers we want to base our recommendations on
    5. The minimal threshold of prevalence of a given offer, in the similar group of customers, for it to be considered for recommendation (see explanation below on how to chose it)
    
    It returns:
    An array with the list of offers that we could recommend to this customer
    """

    # extract the feature vectors of all customers
    features = list(df.columns.difference(['Customer ID','Month','Month of Joining','offer']))
    X = df[features].values

    # extract the feature vector of the given customer
    index = df[(df['Customer ID'] == customer_id) & (df['Month']==month)].index[0]
    x = X[index]

    # compute the distances between the feature vectors
    if distance_func == 'euclidean':
      distances = euclidean_distances(X, x.reshape(1, -1)).flatten()
    elif distance_func == 'manhattan':
      distances = manhattan_distances(X, x.reshape(1, -1)).flatten()
    elif distance_func == 'cosine':
      distances = 1 - cosine_similarity(X, x.reshape(1, -1)).flatten()
    else:
      raise ValueError('Invalid distance function specified.')

    # find the indices of the n customers with lowest distance
    most_similar_indices = distances.argsort()[:n]
            
    # extract the customer data for the most similar customers
    similar_customers = df.iloc[most_similar_indices]

    # merge with the id dataframe to select only the customers who did not churn
    similar_customers = pd.merge(similar_customers,df_id[['Customer ID','Month of Joining','Month','Churn Value']],on=['Customer ID','Month of Joining','Month','Churn Value'])

    # select the customers that did not churn
    similar_customers = similar_customers[similar_customers['Churn Value']==0]

    #count the top offers of the non-churned customers
    top_offers = similar_customers[['Customer ID','offer']].groupby(['offer']).agg({'Customer ID':'count'}).reset_index().sort_values(by = 'Customer ID', ascending = False)
    top_offers['perc_total'] = top_offers['Customer ID']/top_offers['Customer ID'].sum()
    top_offers_min = top_offers[top_offers['perc_total']>minimal_threshold].head(max_offers_to_return)
        
    return top_offers_min['offer'].unique()

def find_similar_customers_multiple(df:pd.DataFrame, df_id:pd.DataFrame,customer_id:str,month:int,distance_funcs:list,n_values,minimal_threshold:float,max_offers_to_return:int):
    """
    Given a dataframe, a customer_id, n values, and distance functions,
    run multiple iterations of the find_similar_customers function with different parameter combinations,
    and return the top 3 most common answers among those.
    """
    results = []
    for n in n_values:
      for distance_func in distance_funcs:
          result = get_recommended_offers (df,df_id ,customer_id,month,distance_func,n,minimal_threshold,max_offers_to_return)
          results.append(result)
          # concatenate the arrays together
          concatenated_array = np.concatenate(results)
          # convert the concatenated array to a Python list
          result_list = list(concatenated_array)
          result_list
    if len(results) == 0:
        return None
    else:
        result_counts = pd.Series(result_list).value_counts()
        most_common_result = [result_counts.index[0],result_counts.index[1],result_counts.index[2]]
        return most_common_result