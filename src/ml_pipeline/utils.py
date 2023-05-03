import pandas as pd

#Function to read the data
def read_csv_data(file_path, **kwargs):
    try:
        raw_data=pd.read_csv(file_path  ,**kwargs)
    except Exception as e:
        raise(e)
    else:
        return raw_data
    
# Function to split our dataframe in a training and production dataset:
def split_dataframe(data):
    try:
        train = data[data['offer']!='No Offer']
        production = data[data['offer']=='No Offer']
    except Exception as e:
        raise(e)
    else:    
        return train, production    