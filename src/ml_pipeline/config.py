processed_data_path='../data/processed/processed_telecom_offer_data.csv'

#This help us identify the customer and the business outcomes
id_variables = ['Customer ID', 'Month','Month of Joining','offer','Churn Category',
       'Churn Reason', 'Customer Status', 'Churn Value']


#This helps us identify the different profiles of customers
selected_variables = ['Customer ID', 'Month', 'Month of Joining', 'Gender', 'Age',
                      'Married', 'Number of Dependents', 'area_codes','roam_ic', 'roam_og',
                      'loc_og_t2t','loc_og_t2m', 'loc_og_t2f', 'loc_og_t2c', 'std_og_t2t', 'std_og_t2m',
                      'std_og_t2f', 'std_og_t2c', 'isd_og', 'spl_og', 'og_others',
                      'loc_ic_t2t', 'loc_ic_t2m', 'loc_ic_t2f', 'std_ic_t2t', 'std_ic_t2m',
                      'std_ic_t2f', 'std_ic_t2o', 'spl_ic', 'isd_ic', 'ic_others',
                      'total_rech_amt', 'total_rech_data', 'vol_4g', 'vol_5g', 'arpu_5g',
                      'arpu_4g', 'arpu', 'aug_vbc_5g','Number of Referrals', 'Phone Service',
                      'Multiple Lines', 'Internet Service', 'Internet Type',
                      'Streaming Data Consumption', 'Online Security', 'Online Backup',
                      'Device Protection Plan', 'Premium Tech Support', 'Streaming TV',
                      'Streaming Movies', 'Streaming Music', 'Unlimited Data',
                      'Payment Method']

# for recommendation withoput bootstraping
distance_measure='euclidean'
n=250

# distance measure for bootstraping
distance_function_list=['euclidean', 'manhattan', 'cosine']

#total bootstrap customers
n_value_list=[250,500,1000]