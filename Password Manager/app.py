import os
import os.path
import json
import smtplib
import socket
from tkinter import *
from tkinter import ttk, messagebox
from theme import *
from ApplicationWindows import *
from functions import *

DATA_FOLDER = os.path.join(os.getcwd(), "Data")
USERS_FOLDER = os.path.join(DATA_FOLDER, "Users")

class PasswordManager(Tk):
    """Root of the application"""

    def __init__(self):
        Tk.__init__(self)

        # Setting width and height of the application
        app_width, app_height = (850, 570)

        # This will give us the screen width and screen height.
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        # This will display the application in the center of the screen.
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.maxsize(width=app_width, height=app_height)

        # Setting title, logo, and background color
        self.title("Password Manager Made By Aman Shahid")
        self.wm_iconbitmap("Assets/Logo/padlock.ico")
        self.config(bg=BODY_COLOR)

        # Setting the style(theme) of the application
        self.style = ttk.Style(self)
        self.call("source", "Assets/Theme/proxttk-dark.tcl")
        self.style.theme_use("proxttk-dark")

        # Now we will create a container(frame) for all of the windows.
        container = Frame(self, width=app_width, height=app_height, bg=BODY_COLOR)
        container.pack(side=TOP, fill=BOTH, expand=TRUE)

        container.grid_rowconfigure(index=0, weight=1)
        container.grid_columnconfigure(index=0, weight=1)

        # Creating all the image elements
        self.images = {
            "nav_bar_logo": PhotoImage(file="Assets/Logo/nav_bar_logo.png"),
            "login_window": {
                "page_one": PhotoImage(file="Assets/Images/login_image.png"),
            },
            "signup_window": {
                "page_one": PhotoImage(file="Assets/Images/login_image.png"),
                "page_two": PhotoImage(file="Assets/Images/login_image.png"),
            },
            "add_window": {
                "page_one": PhotoImage(file="Assets/Images/login_image.png"),
            },
            "retrieve_window": {
                "page_one": PhotoImage(file="Assets/Images/login_image.png"),
                "page_two": PhotoImage(file="Assets/Images/login_image.png"),
            },
            "reset_window": {
                "page_one": PhotoImage(file="Assets/Images/signup_image.png"),
                "page_two": PhotoImage(file="Assets/Images/otp_image.png"),
                "page_three": PhotoImage(file="Assets/Images/reset_image.png")
            },
            "about_window": {
                "page_one": PhotoImage(file="Assets/Images/login_image.png"),
            },
        }

        # Now we will create a list of all the windows for our application.
        self.windows = [
            LoginWindow, SignupWindow, AboutWindow, RetrieveWindow, ResetWindow, AddWindow
        ]
        self.frames = {}

        # All the windows for our application would be a class inherited from the Frame class, which will take two
        # arguments - parent and controller. The class PasswordManager itself is the controller so we will pass "self"
        # as the controller for all our windows.
        for F in self.windows:
            frame = F(parent=container, controller=self)
            # In the above line we passed parent as the container and self as the controller.
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky=NSEW)

        self.frames["LoginWindow"].email.set("ag308669@gmail.com")
        self.frames["LoginWindow"].password.set("abc@12345")
        self.show_window("LoginWindow")

        self.otp = IntVar()
        self.currently_logged_in_account = StringVar()
        self.currently_logged_in_account.set(NONE)

    def show_window(self, window):
        """This function will display the window we want."""
        frame = self.frames[window]
        frame.tkraise()

        # Always show the first page in the case of reset window
        if window == "ResetWindow":
            self.frames["ResetWindow"].show_page("PageOne")

    @staticmethod
    def create_new_account(first_name: str, last_name: str, email: str, password: str):
        """Creates a new user account"""

        # If the user is using the application for the first time, we will make sure all the data folder exists
        if "Data" not in os.listdir(os.getcwd()):
            os.mkdir(DATA_FOLDER)
            os.mkdir(USERS_FOLDER)

        if "Users" not in os.listdir(DATA_FOLDER):
            os.mkdir(USERS_FOLDER)

        # Checking if the email entered is a valid email address.
        if not valid_email(email):
            messagebox.showerror(
                title="Login Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        # If the user already exists we will display the message and return from the function
        if email in os.listdir(USERS_FOLDER):
            messagebox.showinfo(
                title="USER ALREADY EXISTS!",
                message=f"THE USER :  '{email}'  IS ALREADY REGISTERED\n\n"
                        f"GO TO THE LOGIN PAGE TO LOGIN TO YOUR ACCOUNT."
            )
            return
        # Else we will make the new folder for the user
        else:
            os.mkdir(f"{USERS_FOLDER}/{email}")

        # Path for the key file and the data file for the user.
        data_file_path = os.path.join(USERS_FOLDER, email, "data.json")
        key_file_path = os.path.join(USERS_FOLDER, email, "key.key")

        # Generating the new key for the user
        user_key = generate_new_key()

        # Adding the key into the key file of the user
        with open(key_file_path, "wb") as key_file:
            key_file.write(user_key)

        # Encrypting the master password of the user
        encrypted_master_password = encrypt_password(password, user_key)

        new_data = {
            "user_details": {
                "first_name": first_name.title(),
                "last_name": last_name.title(),
                "full_name": f"{first_name} {last_name}".title(),
                "email": email,
                "master_password": encrypted_master_password,
            }
        }

        # Adding the new data into the data file of the user
        with open(data_file_path, "w") as data_file:
            json.dump(new_data, data_file, indent=4)

        # Displaying the success message to the user.
        messagebox.showinfo(
            title="Sign Up Successful",
            message=("YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY.\n\n\n"
                     "YOU MUST REMEMBER YOUR MASTER PASSWORD YOU JUST CREATED TO LOGIN TO YOUR ACCOUNT. "
                     "IN CASE YOU FORGET IT, YOU CANNOT RETRIEVE YOUR PASSWORDS.")
        )

    @staticmethod
    def get_user_data(user_email):
        """Returns the user's data"""
        try:
            with open(os.path.join(USERS_FOLDER, user_email, "data.json"), "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            return None
        else:
            return data

    @staticmethod
    def get_user_key(user_email):
        """Returns the user's key"""
        try:
            with open(os.path.join(USERS_FOLDER, user_email, "key.key"), "rb") as key_file:
                key = key_file.read()
        except FileNotFoundError:
            return None
        else:
            return key

    def login_to_account(self, email, password):
        """Login to the user's account"""

        # Checking if the user entered a valid email address
        if not valid_email(email):
            messagebox.showerror(
                title="Login Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        # Checking if there exists the data and the users folder
        if "Data" not in os.listdir(os.getcwd()):
            messagebox.showwarning(
                title="Login Error",
                message="THERE ARE NO USERS IN OUR DATABASE.\n"
                        "PLEASE CREATE AN ACCOUNT BY SIGNING UP, TO USE THE APPLICATION"
            )
            self.show_window("SignupWindow")
            return
        if "Users" not in os.listdir(DATA_FOLDER):
            messagebox.showwarning(
                title="Login Error",
                message="THERE ARE NO USERS IN OUR DATABASE.\n\n"
                        "PLEASE CREATE AN ACCOUNT BY SIGNING UP, TO USE THE APPLICATION"
            )
            self.show_window("SignupWindow")
            return

        # Checking if the user is a registered user.
        if email.lower() not in os.listdir(USERS_FOLDER):
            messagebox.showerror(
                title="Login Error",
                message=f"THE USER : '{email}' DOES NOT EXISTS. PLEASE SIGNUP TO CREATE AN ACCOUNT!"
            )
            return

        # Getting the actual master password and the key of the user
        user_data = self.get_user_data(email)
        user_key = self.get_user_key(email)

        encrypted_password = user_data["user_details"]["master_password"]

        # Decrypting the actual password
        actual_password = decrypt_password(encrypted_password, user_key)

        # Checking if the user entered the correct password
        if password != actual_password:
            messagebox.showerror(
                title="Login Error",
                message=f"INVALID PASSWORD FOR THE USER : {email}!"
            )
            return

        # If everything is correct login to the user's account
        self.currently_logged_in_account.set(email)
        self.show_window("AddWindow")
        self.frames["AddWindow"].username.set(email)

    def logout_of_the_account(self):
        """Logs the user out of the account"""
        self.currently_logged_in_account.set(NONE)
        self.show_window("LoginWindow")

    def add_new_password(self, for_user: str, web_name: str, web_url: str, username: str, password: str):
        """Saves a new password in the user's account"""

        if web_name.strip() == "" or username.strip() == "" or password.strip() == "":
            messagebox.showerror(
                title="Error!",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        web_name = web_name.title()

        account_email = for_user.lower()

        user_data_file = os.path.join(USERS_FOLDER, account_email, "data.json")

        data = self.get_user_data(account_email)
        user_key = self.get_user_key(account_email)

        encrypted_password = encrypt_password(password, user_key)

        # If the user has never saved a password before
        if "passwords" not in data.keys():
            data["passwords"] = {}

        if web_name in data["passwords"].keys():
            # If the website url is not present we will add it
            if "website_url" not in data["passwords"][web_name].keys():
                data["passwords"][web_name]["website_url"] = web_url
            else:
                previous_url = data["passwords"][web_name]["website_url"]
                if previous_url.strip() == "":
                    data["passwords"][web_name]["website_url"] = web_url
                else:
                    if web_url != previous_url and web_url.strip() != "":
                        user_res_to_change_url = messagebox.askyesno(
                            title="URL Conflict",
                            message=f"YOU HAVE PREVIOUSLY SAVED THE URL FOR '{web_name.capitalize()}' as "
                                    f"'{previous_url}\nDO YOU WANT TO CHANGE IT TO '{web_url}'"
                        )
                        if user_res_to_change_url:
                            data["passwords"][web_name]["website_url"] = web_url

            # If no password is saved for the given website
            if "accounts" not in data["passwords"][web_name].keys():
                data["passwords"][web_name]["accounts"] = {}

            if username in data["passwords"][web_name]["accounts"].keys():
                user_wants_to_update_password = messagebox.askyesno(
                    title="Confirm Update",
                    message=f"PASSWORD FOR '{web_name.upper()}',\nUSERNAME: {username} ALREADY EXISTS!\n"
                            f"DO YOU WANT TO UPDATE IT?"
                )
                if not user_wants_to_update_password:
                    return

            data["passwords"][web_name]["accounts"][username] = encrypted_password

        else:
            data["passwords"][web_name] = {
                "website_url": web_url,
                "accounts": {
                    username: encrypted_password,
                }
            }

        user_confirmation = messagebox.askyesnocancel(
            title="Confirm Details",
            message="PLEASE CONFIRM THE FOLLOWING DETAILS:\n\n"
                    f"WEBSITE: {web_name}\n"
                    f"URL: {web_url}\n"
                    f"USERNAME: {username}\n"
                    f"PASSWORD: {password}\n\n"
                    f"DO YOU WANT TO SAVE IT?"
        )

        if user_confirmation:
            with open(user_data_file, "w") as data_file:
                json.dump(data, data_file, indent=4)

            messagebox.showinfo(
                title="Success",
                message="PASSWORD SAVED SUCCESSFULLY!"
            )
            self.frames["AddWindow"].password_saved_successfully = True

    def retrieve_password(self, for_email, website):
        """Retrieves the password of the given website"""

        if not valid_email(for_email):
            messagebox.showerror(
                title="Login Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        data = self.get_user_data(for_email)
        user_key = self.get_user_key(for_email)

        if (data is None) or (user_key is None):
            messagebox.showerror(
                title="Error",
                message="USER ACCOUNT NOT FOUND!"
            )
            return
        else:
            try:
                website_data = data["passwords"][website]
            except KeyError:
                messagebox.showerror(
                    title="Error",
                    message=f"NO DATA FOUND FOR THE WEBSITE: '{website}'"
                )
                return
            else:
                user_passwords = website_data["accounts"]
                decrypted_data = [
                    (account, decrypt_password(password, user_key)) for account, password in user_passwords.items()
                ]
                return decrypted_data

    def retrieve_all_passwords(self, email):
        """Retrieves all the passwordS"""
        data = self.get_user_data(email)
        if data is not None:
            return data.get("passwords", None)
        return None

    @staticmethod
    def registered_users():
        return os.listdir(USERS_FOLDER)

    @staticmethod
    def send_email(to_email, message):
        """Sends an email to the email address"""
        # Generate a random OTP
        my_email = os.environ.get("MyEmail")
        my_password = os.environ.get("MyPassword")

        # Sending the email to the user
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_email,
                msg=message
            )

    def send_otp(self, email):
        """Sends the OTP to the user for resetting the master password"""
        # Generate an OTP
        otp = random.randint(100000, 999999)
        self.otp.set(otp)
        print(self.otp.get())

        message = f"Subject:Reset MyPass Master Password\n\nThe OTP for resetting your master password for " \
                  f"MyPass Password Manager is:\n\n{otp}\n\nPlease do not share this otp. This OTP is valid " \
                  f"only for 10 minutes."

        # Sending the OTP to the user
        try:
            self.send_email(email, message)

        # If the user is not connected to the internet
        except socket.gaierror:
            messagebox.showerror(
                title="Network Error",
                message="OOPS! YOUR DEVICE IS NOT CONNECTED TO THE INTERNET, PLEASE CONNECT TO THE INTERNET."
            )
            return

        # If any other error occurred
        except smtplib.SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error
            print(error_code, error_message)
            messagebox.showerror(
                title="Error",
                message="SORRY! WE CAN'T SEND YOU AN EMAIL AT THE MOMENT PLEASE CHECK YOUR INTERNET CONNECTION OR"
                        "TRY AGAIN LATER."
            )
            return

        else:
            # This will make sure that the OTP is only valid for 10 minutes.
            self.after(600000, lambda: self.otp.set(0))

    def reset_master_password(self, email, new_password):
        """Resets the master password of the user"""
        if not valid_email(email):
            messagebox.showerror(
                title="Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        if email not in self.registered_users():
            messagebox.showerror(
                title="Error",
                message=f"USER ACCOUNT NOT FOUND!"
            )
            return

        data_file_path = os.path.join(USERS_FOLDER, email, f"user_data.json")

        # Reading the user's data and the key
        data = self.get_user_data(email)
        user_key = self.get_user_key(email)

        # Adding the new password
        data["user_details"]["master_password"] = encrypt_password(new_password, user_key)

        # Writing the new data to the file
        with open(data_file_path, "w") as data_file:
            json.dump(data, data_file, indent=4)

        messagebox.showinfo(
            title="Success",
            message="YOUR MASTER PASSWORD HAS BEEN CHANGED SUCCESSFULLY!"
        )
        self.show_window("LoginWindow")

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    app = PasswordManager()
    app.run()
