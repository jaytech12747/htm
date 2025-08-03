correct_pin = "1234"
attempt = 0
max_attempt = 3

while attempt < max_attempt:
    entered_pin = int(input("enter your pin"))
    if entered_pin == correct_pin:
        print("access granted ")
        break
    else:
        attempt += 1
        print(f"incorrect pin.attempt:{max_attempt - attempt}")
 

if attempt == max_attempt:
    print("car blocked.too much attemps")   
    
    
    
    