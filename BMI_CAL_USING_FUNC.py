Height = float(input("Enter your height in meters: "))
Weight = float(input("Enter your weight in kilograms: "))
def bmi(height,weight):
    compute = weight / height ** 2
    return compute

def calc(Weight):
    compute = Weight * 30
    return compute

result = calc(Weight)
print("Your Calorie Intake every day: ", result)

compute = bmi(Height,Weight)
print("Your BMI: ", compute)

if compute >= 40:
        print("Obesity Class III")
        print("\n------Suggested Calorie intake per day------\n")
        print ("You need to Decrease your Calorie intake by 1000 per day")
        print(result - 1000 , "Calories Per Day")
elif compute >= 35:
    print("Obesity Class II")
    print("\n------Suggested Calorie intake per day------\n")
    print("You need to Decrease your Calorie intake by 750 per day")
    print(result - 750 , "Calories Per Day")

elif compute >= 30:
    print("Obesity Class I")
    print("\n------Suggested Calorie intake per day------\n")
    print("You need to Decrease your Calorie intake by 500 per day")
    print(result - 500 , "Calories Per Day")

elif compute >= 25:
    print("Overweight")
    print("\n------Suggested Calorie intake per day------\n")
    print("You need to Decrease your Calorie intake by 250 per day")
    print(result - 250, "Calories Per Day")

elif compute >= 18:
    print("Normal weight")
    print("\n------Suggested Calorie intake per day------\n")
    print(f"Just Maintain the,{result} calories")

else:
    print("Underweight")
    print("\n------Suggested Calorie intake per day------\n")
    print("You need to Increse your Calorie intake by 300 per day")
    print(result + 300 , "Calories Per Day")


