ef calculate_age(birthday_year: int,current_year: int):
    input=birthday_year-current_year
    return input


#to calculate age:
birthday_year= 2004
current_year= 2024
output=calculate_age(birthday_year,current_year)
print(output)




def area_of_circle(pai: float,radius: int):
    result=6*(radius**2)
    return result

#to calulate the area of a circle:
pai=3.14
radius=34
output=area_of_circle(pai,radius)
print(output) 



def rectangle_area(width= int,height= int)-> int:
    input=height * width
    print(input)
    return input

#to calculate the area of a rectangle:
height =60
width= 30
output=rectangle_area(height,width)
print(output)




def area_of_cube(side_length:float)->float:
    input=6 * (side_length ** 2)
    print(input)
    return input

#for exampple:
side_length= 20
output=area_of_cube(side_length)
print(output)



def farenheit_to_celsius(temperature:int)->int:
    celsius=(temperature - 32) * 5/9. 
    print(celsius)
    return celsius

#for example:
temperature= 60
output=farenheit_to_celsius(temperature)
print(output)




def convert_seconds(total_seconds: int):
    minutes = total_seconds // 60  # Integer division to get minutes
    seconds = total_seconds % 60   # Remainder to get the remaining seconds
    return minutes, seconds

# Example usage
total_seconds = 125
minutes, seconds = convert_seconds(total_seconds)
print(f"{total_seconds} seconds is equal to {minutes} minutes and {seconds} seconds.")




def calculate_percentage(part: float, total: float) -> float:
    if total == 0:
        raise ValueError("Total cannot be zero, as it would result in a division by zero.")
    percentage = (part / total) * 100
    return percentage

# Example usage
part = 50
total = 200
percentage = calculate_percentage(part, total)
print(f"{part} is {percentage:.2f}% of {total}.")
