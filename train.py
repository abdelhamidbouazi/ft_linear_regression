import sys
from checkPathFormat import checkPathNdFormat
from load_csv import load

learning_rate = 0.01
epochs = 1000



def normlizer(mileages, m):
    mean_mileage = sum(mileages) / m
    diffs        = [x - mean_mileage for x in mileages]
    variance     = sum(d**2 for d in diffs) / m
    std_deviation = variance**0.5

    km_norm = [(x - mean_mileage) / std_deviation for x in mileages]
    return (mean_mileage, std_deviation, km_norm)


def train(path: str):
    theta0 = 0
    theta1 = 0

    # 1) compute mean and standard deviation

    try:
        checkPathNdFormat(path)
        data = load(path)
        mileages = data["km"].to_list()
        prices = data["price"].to_list()
        m = len(mileages)

        mean_mileage, std_deviation, km_norm = normlizer(mileages, m)



        for i in range(epochs):
            estimatePrice = [theta0 + theta1 * km for km in km_norm]
            # print(estimatePrice)
            tempt0 = learning_rate * sum(es - pr for es, pr in zip(estimatePrice, prices)) / m
            tempt1 = learning_rate * sum((es - pr) * km_norm for es, pr, km_norm in zip(estimatePrice, prices, km_norm)) / m
            theta0 = theta0 - tempt0
            theta1 = theta1 - tempt1

        real_theta0 = theta0 - (theta1 * mean_mileage) / std_deviation
        real_theta1 = theta1 / std_deviation
        kmEs = 22899
        esPrice = real_theta0 + real_theta1 * kmEs
        print(f"prince is -> {esPrice}")


    except (AssertionError, FileNotFoundError, StopIteration, KeyError) as e:
        print(f"Error during operations : {e}")

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1])
        train(sys.argv[1])
    else:
        print("Please respect arguments")
        return

if __name__ == "__main__":
    main()