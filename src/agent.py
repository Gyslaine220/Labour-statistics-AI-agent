from analysis import (
    load_data,
    calculate_lfpr,
    calculate_unemployment_rate,
    calculate_employment_rate
)
def ask_agent(question):
    if (
        "labour force participation rate" in question.lower()
        or "lfpr" in question.lower()
    ):
        df = load_data("Data/RW_LFS2024.dta")

        working_age_population = df.loc[
            df["wap16"] == 1, "weight2"
        ].sum()

        employed = df.loc[
            df["status1"] == "Employed", "weight2"
        ].sum()

        unemployed = df.loc[
            df["status1"] == "Unemployed", "weight2"
        ].sum()

        labour_force = employed + unemployed

        lfpr = calculate_lfpr(
            labour_force,
            working_age_population
        )

        return f"The Labour Force Participation Rate is {lfpr:.2f}%."
print(ask_agent("What is the LFPR?"))
        
    
