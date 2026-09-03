def calculate_rate(enumerator, denominator):
    return (enumerator / denominator) * 100

def calculate_unemployment_rate(unemployed, labour_force):
    if labour_force <= 0:
        return None

    if unemployed < 0 or unemployed > labour_force:
        return None

    return calculate_rate(unemployed, labour_force)