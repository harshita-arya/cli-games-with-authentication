'''The main application'''
from utils.driver_functions import clear, get_user_choice
from app.auth.login import try_login
from app.auth.signup import try_register
from app.auth.otp_verification import otp_verification

def app():
    while True:
        clear()
        print("Welcome to guessing game\n1 Login\n2 Sign up\n3 Verify Otp\n")

        choice = get_user_choice()
        clear()

        if choice == 1:
            user = try_login()
            break

        elif choice == 2:
            user = try_register()
            break
        
        elif choice == 3:
            otp_verification()
            break

        else:
            break
