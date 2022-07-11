def add(num1,num2):
    while(num2 != 0):
        carry = num1 & num2
        num1 = num1 ^ num2
        num2 = carry << 1
    
    print(num1)
    return num1

add(2,3)
add(5,5)
add(20,100)
