def normlizer(dataset):
    mean = sum(dataset) / len(dataset)
    diffs        = [x - mean for x in dataset]
    variance     = sum(d**2 for d in diffs) / len(dataset)
    std_deviation = variance**0.5

    dataset_norm = [(x - mean) / std_deviation for x in dataset]
    return (mean, std_deviation, dataset_norm)