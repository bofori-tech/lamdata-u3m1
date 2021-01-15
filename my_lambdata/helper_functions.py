import pandas as pd

def null_count(df):
    df = pd.DataFrame({'a':[1,2,np.nan], 'b':[np.nan,1,np.nan]})
    null_count(df)
    print(null_count(df))
    
def train_test_split(df, frac)
    df = pd.DataFrame({'column 0':[0,3,6], 'column 1':[1,4,7], 'column 2':[2,5,8]})
    train_test_split(df, frac=0.2)



