
import pandas as pd
import os
print(os.getcwd())

def load_data(filepath):
    if filepath.endswith(".dta"):
        return pd.read_stata(filepath)
    elif filepath.endswith(".csv"):
        return pd.read_csv(filepath)
    else:
        raise ValueError("Unsupported file format")


def prepare_data(df):
    return df[df["wap16"] == 1]

def calculate_rate(numerator, denominator):
    return (numerator / denominator) * 100


# Function to calculate the unemployment rate
def calculate_unemployment_rate(unemployed, labour_force):
    if labour_force <= 0:
        return None

    if unemployed < 0 or unemployed > labour_force:
        return None

    return calculate_rate(unemployed, labour_force)


# Function to calculate the labour force participation rate (LFPR)    
def calculate_lfpr(labour_force, working_age_population):
    if working_age_population <= 0:
        return None

    if labour_force < 0 or labour_force > working_age_population:
        return None

    return calculate_rate(labour_force, working_age_population)


# Function to calculate the employment rate
def calculate_employment_rate(employed, working_age_population):
    if working_age_population <= 0:
        return None

    if employed < 0 or employed > working_age_population:
        return None

    return calculate_rate(employed, working_age_population)
#Data Validation Function
def validate_data(df):
    required_columns = ["status1", "wap16"]

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
           f"Missing required columns: {missing_columns}"
        )

    return df


if __name__ == "__main__":
    df = load_data("Data/RW_LFS2024.dta")
    print("STATUS1:")
    print(df["status1"].value_counts(dropna=False).to_string())
    #df = prepare_data(df)
   # df = validate_data(df)
   
    working_age_population = (df["wap16"] == 1).sum()
    labour_force = (
        (df["status1"] == "Employed").sum()
        + (df["status1"] == "Unemployed").sum()
    )

    employed = (df["status1"] == "Employed").sum()
    unemployed = (df["status1"] == "Unemployed").sum()
    working_age_population = (df["wap16"] == 1).sum() if "wap16" in df.columns else len(df)

    unemployment_rate = calculate_unemployment_rate(unemployed, labour_force)
    lfpr = calculate_lfpr(labour_force, working_age_population)
    employment_rate = calculate_employment_rate(employed, working_age_population)

    print("Unemployment Rate:", unemployment_rate, "%")
    print("Labour Force Participation Rate:", lfpr, "%")
    print("Employment Rate:", employment_rate, "%")
    
   
  
  


