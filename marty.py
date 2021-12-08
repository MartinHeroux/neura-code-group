def normalise_to_100(data):
    max_data = max(data)
    return (data/max_data) * 100

