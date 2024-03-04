def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    
    Formula: BMI = weight / (height * height)
    
    Args:
    weight_kg (float): Weight in kilograms.
    height_m (float): Height in meters.
    
    Returns:
    float: Calculated BMI value.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    """
    Interpret the BMI value and provide a corresponding message.
    
    Args:
    bmi (float): Body Mass Index (BMI) value.
    
    Returns:
    str: Interpretation message.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    bmi = calculate_bmi(weight, height)
    interpretation = interpret_bmi(bmi)
    
    print(f"Your BMI is {bmi:.2f}. You are {interpretation}.")

if __name__ == "__main__":
    main()
