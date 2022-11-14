"""
Name: display_game
Purpose: formats questions, answers, and asking for user input and displays it. Once user input is taken, this function records whether the user got the answer 
right or wrong for later use.
Parameters: list: where format_file() will be used when this function gets called to access the list.
Return: returns the number of answers the user got right and wrong.
"""
def display_game(list):
  count = 1
  right = 0
  wrong = 0
  enter_answer = "Enter your answer (A, B, C or D): "
  for i in range(0, len(list), 6):
    print("Question {num}: {question}".format(num=count,question=list[i]))
    print("{A}. {choice}".format(A="A", choice=list[i+1]))
    print("{B}. {choice}".format(B="B", choice=list[i+2]))
    print("{C}. {choice}".format(C="C", choice=list[i+3]))
    print("{D}. {choice}".format(D="D", choice=list[i+4]))
    user_input = input(enter_answer)
    while not user_input.lower() in 'abcd' and len(user_input) != 1:
      user_input = input(enter_answer)
    if user_input.lower() == list[i+5]:
      right += 1
    else:
      wrong += 1
    count += 1
  return right, wrong


"""
Name: format_file
Purpose: open 'qa.txt' and format the file in a way where it gets rid of extra space and append each line to the list, 'list'
Parameters: None
Return: returns a list with all the questions and answers from 'qa.txt' called 'list'.
"""
def format_file():
  list = []
  with open("qa.txt", "rt") as file_object:
    list = file_object.readlines()
    for i in range(len(list)):
      list[i] = list[i].rstrip()
    file_object.close()
  return list

  
#trivia game execution
corr, miss = display_game(format_file())
print("\nYou got " + str(corr) + " questions correct and missed " + str(miss) + " questions.")
