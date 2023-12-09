import random
# the additions to the password you can select from
symbols = ["13451","2476126","34@$%!4515","FGw3525","ggihwohg@FSFSGH%@","235f@@4f5w@$%Ttgwj",")(*&%@%Tgerge","ghfe[oghioqeqetp9ih$@%@"]
# connects the rockyou.txt file to this programe
rockyou = open("rockyou.txt", "rb")
# asks for the password
userpass = input("input password → ")

# starts the line count
line = 0
additon = random.randint(1,100000000000000000000)

# starts to search
for x in rockyou.readlines():
  # keeps track of the lines
  line += 1
  if(userpass in x.decode()):
    #stop searching and tell the user that there pass is in rockyou
    break
  # keep looking
  else:
    
    print(f"password not found, {x}")
# tells the user the password and the line witch it is on
print(f"password found {userpass}, line {line}")





# In Dev

# this is to improve the password

# the pass word has been found
# passfound = True
# https://www.youtube.com/watch?v=CJkWS4t4l0k
# https://www.youtube.com/watch?v=1JDbMkwoolo

# if(passfound == True):
# gets the old password and gets it preped for the additon
#   newpass = userpass

  
#   for newpass in x:
#     # checks if the new password is not the old password
#     if(newpass != userpass):
#       print(newpass) 
#     #adds some sybols to the end
#     else:
#       newpass += additon
#       print("new password → ")
# else:
#   print("all good to go! remember to practese good securety")
    