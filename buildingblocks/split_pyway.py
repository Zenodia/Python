#python way of spliting training and validation set
import random
def split(df):
    random.shuffle(df)
    return df[:len(df)/2], df[len(df)/2:]
    train = []
    validate = []
    for row in df:
        random.choice([train, validate]).append(row)
    return train, validate
