# Create a class called PasswordManager.
# Encapsulation: In __init__, save a private attribute called self.__master_password.
# Static Method: Create a @staticmethod called is_strong_password(password).
# If the length of the password is greater than 8 characters, return True,
# otherwise return False.
# Abstraction: Create a public method called unlock_vault(entered_password).
# Inside it, check if entered_password == self.__master_password. If it matches,
# call a hidden private method called __load_encrypted_data()
# which simply prints "Decrypted data loaded successfully!".
# This combines your private attributes (__), a utility tool (@staticmethod), and
# hidden implementation details (__load_encrypted_data).




class PasswordManager:
    def __init__(self, master_password):
        if self.is_strong_password(master_password):
            self.__master_password = master_password
        else:
            print("Password did not saved. Use default password")
            self.__master_password = "DefaultStrongPassword123!"




    @staticmethod
    def is_strong_password(master_password):
        if len(master_password) < 8:
            print("Weak Password")
            return False
        else:
            print("Password Saved")
            return True


    def get_password(self):
        return self.__master_password


    def unlock_vault(self, entered_password):
        if entered_password == self.get_password():
            self.__load_encrypted_data()
            return True
        else:
            print("Incorrect Password")
            return False

    def __load_encrypted_data(self):
        # self.get_password()
        print("Decrypted data loaded successfully!")


s1= PasswordManager("1234")

print(s1.unlock_vault(input("Enter your password: ")))
# print(s1.get_password())
