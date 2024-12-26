def countdown(i):
    if i <= 0:
        print("To the MOON!")
    else:
        print(i)
        countdown(i-1)   

countdown(5)