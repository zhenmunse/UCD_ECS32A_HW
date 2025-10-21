# Homework 3 Part III (dog.py)
# Coder: Zonglin Han
# This program provides dog walking advice.

# Initialization
weather = input("Enter weather condition (rainy/sunny/snowy/cloudy):")

# Provide dog walking advice based on weather and temperature
if weather == "rainy":
    print("Instructions for the walk:")
    print("The dog should be taken for a short walk with an umbrella.")
elif weather == "sunny":
    temperature = int(input("Enter temperature:"))
    print("Instructions for the walk:")
    if 80 < temperature <= 114:
        print("The dog should be taken for a walk in the shade and given water.")
    elif 45 < temperature <= 80:
        print("The dog can enjoy a regular walk.")
    elif -14 < temperature <= 45:
        print("Dress the dog warmly for a walk.")
    else:
        print("Invalid weather condition.")
elif weather == "snowy":
    print("Instructions for the walk:")
    print("Take the dog for a short walk and ensure they stay warm.")
elif weather == "cloudy":
    print("Instructions for the walk:")
    print("Enjoy a regular walk with your dog.")
else:
    print("Instructions for the walk:")
    print("Invalid weather condition.")
