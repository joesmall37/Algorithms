while True:
    answer = input("Which floor would you like to go to?")
    if answer == "out":
        print("exitiing")
        break
    else:
        answer_floor = int(answer)
        if answer_floor > 0 and answer_floor <= 20:
            print(" you are on floor ", answer)
        else:
            print('I cannot take you to floor', answer_floor)
