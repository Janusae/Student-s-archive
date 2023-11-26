def student_marks():
    marks = {}
    while True:
        ask_name = input("Inter student's name: ")
        ask_mark = input("Inter student's mark: ")
        if ask_name == "" or ask_mark == "":
            ask_name = input("Inter student's name: ")
            ask_mark = input("Inter student's mark: ")
            if ask_name != "" and ask_mark != "" :
                marks[ask_name] = ask_mark
        else:
            marks[ask_name] = ask_mark
        ask_done = input("Finish? y or n: ")
        if ask_done.title() == "Y":
            break
    show = input("Do you want to see studen's archive?(y or n):  ")

    if show.title() == "Y":
        for i in marks:
            print(F"{i} : {marks[i]}")
    else:
        print("Have a good time!")

student_marks()