class chatbook():
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to chatbook!! How would you like to proceed?
              1. press 1 to sign up
              2. press 2 to sign in
              3. press 3 to write a post
              4. press 4 to message a friend
              5. press any other key to exit!
                           
                --->""")
        if user_input == '1':
            self.signup()
        elif user_input == '2':
            self.signin()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.sendmsg()
        else:
            exit()

    def signup(self):
        email = input("Enter the username:")
        pwd = input("Enter the password:")
        self.username = email
        self.password = pwd
        print("you have signed up successfully!!")
        self.menu()
        print("\n")

    def signin(self):
        if self.username == "" and self.password == "":
            print("you need to sign up before sign in!!")
        else:
            uname = input("Enter the username/email:")
            pwd = input("Enter the password:")
            if self.username == uname and self.password == pwd:
                print("you have signed in successfully")
                self.loggedin = True
            else:
                print("please enter the correct credentials")
        print("\n")
        self.menu()

    def my_post(self):
        if self.loggedin == True:
            txt = input("Enter the post here:")
            print(f"you have posted: {txt}")
        else:
            print("you need to sign in first in order to post anything!!")
        print("\n")
        self.menu()

    def sendmsg(self):
        if self.loggedin == True:
            msg = input("Enter your message here:")
            friend = input("whom to send:")
            print("Your message has been sent")
        else:
            print("you need to sign in before sending the message.") 

obj = chatbook()