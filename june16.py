a= int(input(" Enter 1st number:"))
b = int(input(" Enter 2nd number: "))
print(" for subtraction press 1: ")
print(" for multipklication press 2:")
print (" for division press 3: ")
choice= int(input(" enter your choice: "))
if choice == 1:
    def sub(num1 , num2):
        my_sub = num2 - num1
        print( my_sub)
    sub(a,b) 
elif choice == 2:
    def mult( no1, no2):
        my_mult = no1 * no2
        print (my_mult)   
    mult( a, b)
elif choice == 3:
    def div( n1, n2) :
        my_divi = n1/n2
        print(my_divi)
    div(a, b)                    