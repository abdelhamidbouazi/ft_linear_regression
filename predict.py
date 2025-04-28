import json

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
            userMilage = float(input("Enter car milage: "))
            if userMilage < 0:
                print("Error: Mileage cannot be negative !!!")
                continue
        except (ValueError, KeyboardInterrupt) as e:
            print("Error: Check Value Entred")
        return userMilage

def predict():
    theta0 = 0
    theta1 = 0
    try:
        theta0, theta1 = loadThetas()
        if theta0 == 0 and theta1 == 0:
            raise ValueError("Error: Model is not trained yet. Please run train.py first!")
        userMilage = getUserMilage()
        predicted_price = theta1 + theta0 * userMilage
    except:
        return

    else:
        print(f"The predicted price for a car with milage {userMilage} is {predicted_price:.2f}")

def main():
    predict()

if  __name__ == "__main__":
    main()