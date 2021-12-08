def normalise_to_100(data):
    "Normalize to between 0 and 100"
    max_data = max(data)
    return (data/max_data) * 100

