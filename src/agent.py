from analysis import (
    calculate_lfpr,
    calculate_unemployment_rate,
    calculate_employment_rate
)
def ask_agent(question):
    if (
        "labour force participation rate" in question.lower()
        or "lfpr" in question.lower()
    ):
        return "LFPR"

    return "I don't know how to answer that yet."
print(ask_agent("What is the LFPR?"))
print(ask_agent("What is the Labour Force Participation Rate?"))
print(ask_agent("WHAT IS LFPR?"))

 
 
