#private attributes
class user:
    __password = 'globe1691'
    def __init__(self,username,email,name):
        self.username = username
        self.email = email
        self.name = name
    def getpass(self):
        return self.__password
    def setnew(self):
        old = input("Enter old password")
        if old == self.__password:
            new = input("What would you like new passowrd to be?")
            self.__password = new
        else:
            print("Incorrect password!")
login = user("admin","admin@outlook.com","Aarav")
print(login.username)
print(login.email)
print(login.name)
print(login.getpass())
login.setnew()