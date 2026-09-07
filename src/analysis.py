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

  
  