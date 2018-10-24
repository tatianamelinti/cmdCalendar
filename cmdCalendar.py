from time import sleep, strftime
#from time import strftime
USER_FIRST_NAME = "Tatiana"
calendar = {}
def welcome():
  print ("Welcome, " + USER_FIRST_NAME + "!")
  print ("Calendar starting...")
  sleep(1)
  print ("Taday is: " + strftime("%A %B %d, %Y"))
  print ("The current time is: " + strftime("%H:%M:%S"))
  sleep(1)
  print ("What would you like to do?")
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = input("Enter: A to Add, U to Update, V to View, D to Delete, X to Exit:")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print ("The calendar is empty.")
      else: 
        print (calendar)
    elif user_choice == 'U':
      date = input("What date? ")
      update = input("Enter the update: ")
      calendar[date] = update
      print ("Successful updated!")
      print (calendar)
    elif user_choice == 'A':
      event = input("Enter event: ")
      date = input("Enter date (MM/DD/YYYY): ")
      if(len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print ("An invalid date was entered!")
        try_again = input("Try Again? Y for Yes, N for No: ")
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print ("The event was successfully added!")
        print (calendar)
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print ("The calendar is empty.")
      else:
        event = input("What event?")
        for date in calendar.keys():
          if event == calendar[date]:
            del calendar[date]
            print ("The event was deleted")
            print (calendar)
          else:
            print ("An incorrect event was specified.")
    elif user_choice == 'X':
        start = False
    else:
        print ("Was entered an invalid command")
start_calendar()