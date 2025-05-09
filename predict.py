import json
import os


def accuracy(price_real, price_pred):
    n = len(price_real)
    errors = [ (pr_real - pr_pred) for pr_real, pr_pred in (price_real, price_pred) ]
    mse = (sum(errors) ** 2) / n
    return mse

def loadThetas(path="params.json"):
    theta0 = 0
    theta1 = 0
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                data = json.load(f)
                theta0 = data.get("theta0", 0)
                theta1 = data.get("theta1", 0)
        except (json.JSONDecodeError, KeyError):
            pass
    return theta0, theta1


def getUserMilage():
    while True:
        userMilage = int(input("Enter car milage: "))
        if userMilage < 0:
            print("Error: Mileage cannot be negative !!!")
            continue
        return userMilage

def predict(userMilage):
    theta0, theta1 = loadThetas()
    # if theta0 == 0 and theta1 == 0:
    #     raise ValueError("Error: Model is not trained yet. Please run train.py first!")
    predicted_price = theta0 + theta1 * userMilage
    if predicted_price < 0:
        print(f"Your car is a trash, think about changing it")
    else:
        print(f"The predicted price for a car with milage {userMilage} is {predicted_price:.2f}")

def main():
    try :
        userMilage = getUserMilage()
        predict(userMilage)
    except Exception as e:
        print(f"Error: {e}")

if  __name__ == "__main__":
    main()