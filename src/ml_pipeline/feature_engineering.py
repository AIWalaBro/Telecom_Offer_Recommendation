from sklearn.preprocessing import LabelEncoder
from projectpro import data_pipeline
data_pipeline('fcTel3')

# Now we need to transform the features of the feature store.
def encode_categorical_features(train_df,prod_df):
    try:
        # Get a list of all categorical columns
        cat_columns = train_df.select_dtypes(include=['object', 'category']).columns.tolist()

        # Encode each categorical column
        for col in cat_columns:
            try:
                le = LabelEncoder()
                train_df[col] = le.fit_transform(train_df[col])
                prod_df[col]= le.transform(prod_df[col])
            except Exception as e:
                raise(e)
    except Exception as e:
        raise(e)
    else:            
        return train_df, prod_df