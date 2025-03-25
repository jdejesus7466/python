if __name__ == "__main__":

    sent_message = 'Hey there! This is a secret message.'

    with open('sent_message.txt', 'w') as file:
        file.write(sent_message)
    
    with open('sent_message.txt', 'r+') as file:
        original_message = file.read()
        print("Original Message:", original_message)  

        file.seek(0)
        file.truncate(0)

    unsent_message = 'This message has been unsent.'

    with open('sent_message.txt', 'w') as file:
        file.write(unsent_message)

    with open('sent_message.txt', 'r+') as file:
        new_message = file.read()
        print("New Message:", new_message)

    