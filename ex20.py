user_list=[]
while True:
   input_user=int(input(print("Enter a number:")))
   if input_user!=0:
      user_list.append(input_user)
      print(f"current list: {user_list}")
      print(f"sorted list: {sorted(user_list)}")
   else:
      break