### Task M1: Extend Basic Functions
#Modify `grade_assignment()` to include:
#- A+ grade for scores ≥ 97
#- Different grade boundaries (e.g., 85+ for A, 75+ for B)

def grade_assignment(score):
    if score >= 97:
        return "A+"
    if score >= 85:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 65:
        return "C"
    else:
        return "D or below"


### Task M2: Add Validation
#Enhance `check_temperature()` to:
#- Handle invalid inputs (non-numeric values)
#- Add more temperature categories (freezing, hot, very hot)

def check_temperature(temp):
    try:
        temp=int(temp)
        if temp > 25:
            return "It's warm today!"
        else:
            return "It's cool today!"
    except ValueError:
        return "Invalid temperature!"

### Task M3: Improve Complex Functions
#Modify `calculate_shipping()` to:
#- Add weekend delivery surcharge
#- Include different rates for different regions
#- Add bulk discount for heavy items

def calculate_shipping(region, weight, distance, is_express, is_weekend):
    """Complex conditions with calculations"""
    if weight <= 0 or distance <= 0:
        return "Invalid input"
    
    if region = south:
        base_cost = 8.0
    elif region = north:
        base_cost = 6.0
    elif region = east:
        base_cost = 4.0
    elif region = west:
        base_cost = 2.0
    
    if weight > 10:
        base_cost += ((weight - 10) * 1.5)*0.9 #reduce by 10%
    else:
        base_cost += (weight + 10) *1.5
    
    if distance > 100:
        base_cost += (distance - 100) * 0.1
    
    if is_express:
        base_cost *= 2

    if is_weekend:
        base_cost += 3
    
    return round(base_cost, 2)

#
### Task M4: Create Compact Versions
#Convert these verbose functions to compact ternary versions:
#- `categorise_age()`
#- `validate_password_strength()` (simplified version)