import os 

os.system ("ls | grep password > result.txt")
with open("result.txt", "r") as file:
     res = file.read()

if len(res) > 0:
   os.system("zenity --info \--text = 'Password was found'")