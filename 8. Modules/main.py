import datetime, bday_messages
if __name__ == "__main__":

    today = datetime.date.today()
    next_birthday = datetime.date(2026, 2, 4)

    days_away = next_birthday - today

    if today == next_birthday:
        print(bday_messages.random_message)
    else:
        print("My next birthday is " + str(days_away) + " away")
    
