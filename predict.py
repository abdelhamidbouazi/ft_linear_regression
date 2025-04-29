import json
from display import displayPlots

def loadThetas(path="params.json"):
    try:
        with open(path, "r") as f:
            data = json.load(f)
            theta0 = data["theta0"]
            theta1 = data["theta1"]
        return theta0, theta1
    except (json.JSONDecodeError, FileNotFoundError, TypeError):
            print("Error: Model is not trained yet. Please run train.py first!")


def getUserMilage():
    while True:
        try:
            userMilage = int(input("Enter car milage: "))
            if userMilage < 0:
                print("Error: Mileage cannot be negative !!!")
                continue
        except (ValueError, KeyboardInterrupt) as e:
            print("Error: Check Value Entred")
        return userMilage

def predict():
    try:
        theta0 = 0
        theta1 = 0
        theta0, theta1 = loadThetas()
        if theta0 == 0 and theta1 == 0:
            raise ValueError("Error: Model is not trained yet. Please run train.py first!")
        userMilage = getUserMilage()
        predicted_price = theta0 + theta1 * userMilage
        print(f"The predicted price for a car with milage {userMilage} is {predicted_price:.2f}")
    except:
        print("Error !")

def main():
    predict()

if  __name__ == "__main__":
    main()