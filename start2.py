user_name = input(" Enter your Password: ")
length = len(user_name)
if length <= 3:
    print(" Your password is too weak")
    print(" try again")
elif (length>3 and length<10) :
    print(" Your password is Good and long")
elif (length > 10 ) :
    print (" Your password is strong")

