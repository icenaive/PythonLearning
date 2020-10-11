while 1:
    first_num = input("inpurt num q is exit: ")
    if(first_num == "q"):
         break
    second_num = input("inpurt num q is exit: ") 
    if(second_num == 'q'):
        break
    try:
        num = int(first_num) + int(second_num)
    except ValueError:
        print("bu yao dao luan")
    else:
        print("num = %d" % num)

