from pystyle import *
import webbrowser

print(Box.Lines('Welcome To Br4deData To LogIn for A New Account'))

Write.Print('This Data for Login page \n', Colors.blue_to_purple, interval = 0.1)
Write.Print('Please Enter Username And Password \n\n', Colors.blue_to_purple, interval = 0.1 )

print(Box.DoubleCube('UserName : ***** \nPassWord : *****'))

while True:
    Username = input('Enter The User Name : ')

    Password = input('Enter The Password : ')

    if Username == "Rabah" and Password == "karim12":
        Write.Print('Welcome to our Data', Colors.blue_to_green, interval = 0.1)

        webbrowser.open('https://www.instagram.com/jalal_web3')
        break



    else:
        Write.Print('Wrong Username or Password', Colors.red, interval = 0.1)
        break