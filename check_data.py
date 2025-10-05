import os 
import pandas as pd

DATA_PATH = "data"
TRAIN_PATH = os.path.join(DATA_PATH, "train.csv")
TEST_PATH = os.path.join(DATA_PATH, "test.csv")


def check_data(df: pd.DataFrame, name: str) -> None:
    print(f"Checking {name} data")
    print("-" * 100)
    print("Head: \n", df.head())
    print("Describe: \n", df.describe())
    print("Is null: \n", df.isnull().sum())
    print("Is duplicated: \n", df.duplicated().sum())
    print("Nunique: \n", df.nunique())
    print("Value counts: \n", df.value_counts())

    print("Is unique ids: ", df["id"].nunique() == df.shape[0])
    print("Sample: \n", df.sample(5).to_string())
    print("-" * 100, "\n\n")

    # TODO: 
    # 1. Check if categorical data is better to be one-hot encoded or label 
    # 2. Check categorical data distribution 
    # 3. Check target data distribution 
    # 4. Check dataset on outliers



def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    # TODO: 
    # 1. Replace categorical data with numerical 
    # 2. Process num_lanes, speed_limit,  - as categorical data 
    # 3. Normalize num_reported_accidents
    # 4. Remove outliers 

    return df


if __name__ == "__main__":
    train_df = pd.read_csv(TRAIN_PATH)
    test_df = pd.read_csv(TEST_PATH)

    check_data(train_df, "train")
    check_data(test_df, "test")

