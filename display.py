# %%
import sys
import matplotlib.pyplot as plt
import numpy as np
from checkPathFormat import checkPathNdFormat
from load_csv import load
import json
# from predict import getUserMilage

# to run display plots you have to train the modal first, run train.

def loadThetas(path="params.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            theta0 = data["theta0"]
            theta1 = data["theta1"]
        return theta0, theta1
    except (json.JSONDecodeError, FileNotFoundError, TypeError):
            print("Error: Model is not trained yet. Please run train.py first!")


def displayPlots(dataPath):
    try:
        checkPathNdFormat(dataPath)
        data = load(dataPath)
        mileages = data["km"].to_list()
        prices = data["price"].to_list()

        xpoints = np.array(mileages)
        ypoints = np.array(prices)
        theta0, theta1 = loadThetas()
        if theta0 == 0 and theta1 == 0:
            raise ValueError("Error: Model is not trained yet. Please run train.py first!")
        values = [0, 50000, 10000, 150000, 200000, 250000]
        y_line = [(theta1 * mi) + theta0 for mi in values]

        fig, ax = plt.subplots()
        ax.plot(y_line, values)
        ax.scatter(ypoints, xpoints,label='Cars prices')
        ax.legend()
        ax.set_xlabel('price')
        ax.set_ylabel('mileage')
        ax.title('Cars prices prediction')
        # ax.
        # plt.show()
    except Exception as e:
        print ("Error plotting data! ", e)



def main():
    if len(sys.argv) == 2:
        displayPlots(sys.argv[1])
    displayPlots("data.csv")
    
    # else:
    #     print("Please respect arguments")
    #     return

if __name__ == "__main__":
    main()
# %%
