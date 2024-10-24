from widgets import *
from tkinter import messagebox
from functions import generate_password


class AddWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nav_bar.add_nav_menu(
            label="Add",
            action=lambda: self.controller.show_window("AddWindow"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            label="Retrieve",
            action=lambda: self.controller.show_window("RetrieveWindow"),
        )
        self.nav_bar.add_nav_menu(
            label="Logout",
            action=lambda: self.logout(),
        )

        self.password_saved_successfully = False

        self.website_name = StringVar()
        self.website_url = StringVar()
        self.username = StringVar()
        self.password = StringVar()

        self.add_pages(PageOne)

    def logout(self):
        """Logout the user"""

        # Take user confirmation
        user_response = messagebox.askyesno(
            title="Confirm Logout",
            message="DO YOU WANT TO LOG OUT OF YOUR ACCOUNT?"
        )

        # If the user confirmed logout, then log him out of the account
        if user_response:
            self.controller.logout_of_the_account()


class PageOne(Body):

    def __init__(self, parent, controller, **kw):
        super().__init__(parent, controller, **kw)

        self.config(pady=110, padx=70)

        self.website_name_entry = SingleRowInputBox(
            self,
            label="Website / Application name:",
            var=self.parent_window.website_name
        )
        self.website_url_entry = SingleRowInputBox(
            self,
            label="Website URL (optional):",
            var=self.parent_window.website_url
        )
        self.username_entry = SingleRowInputBox(
            self,
            label="Username:",
            var=self.parent_window.username
        )
        self.password_entry = SingleRowInputBox(
            self,
            label="Password:",
            var=self.parent_window.password
        )

        self.add_inputs(
            [self.website_name_entry, self.website_url_entry, self.username_entry, self.password_entry],
            from_row=1
        )

        self.website_name_entry.entry.config(width=48)
        self.website_url_entry.entry.config(width=52)
        self.username_entry.entry.config(width=64)
        self.password_entry.entry.config(width=47)

        self.generate_password_btn = ttk.Button(
            self,
            text="Generate password",
            command=lambda: self.show_random_password(),
        )
        self.generate_password_btn.config(width=20, style="ToggleButton")
        self.generate_password_btn.grid(row=4, column=1, pady=(2, 0), sticky=E)

        self.add_btn = MyButton(
            self,
            text="Save Password",
            command=lambda: self.save_password(),
        )
        self.add_btn.grid(row=5, column=0, columnspan=2, pady=(15, 30))
        self.add_btn.config(width=20)

        self.website_name_entry.entry.bind("<Return>", lambda e: self.website_url_entry.entry.focus_set())
        self.website_url_entry.entry.bind("<Return>", lambda e: self.username_entry.entry.focus_set())
        self.username_entry.entry.bind("<Return>", lambda e: self.password_entry.entry.focus_set())
        self.password_entry.entry.bind("<Return>", lambda e: self.save_password())

    def show_random_password(self):
        """Shows a random password"""
        random_password = generate_password()
        self.parent_window.password.set(random_password)

    def save_password(self):
        """Saves the password"""

        user_email = self.root_controller.currently_logged_in_account.get()
        web_name = self.parent_window.website_name.get()
        web_url = self.parent_window.website_url.get()
        username = self.parent_window.username.get()
        password = self.parent_window.password.get()

        if user_email is None:
            messagebox.showerror(
                title="Error",
                message="SOME FISHY LOGIN ACTIVITY DETECTED!\nLOGOUT FROM YOUR ACCOUNT AND LOGIN AGAIN TO CONTINUE"
                        "SAVING PASSWORDS!"
            )
            return

        if web_name.strip() == "" or username.strip() == "" or password.strip() == "":
            messagebox.showerror(
                title="Error!",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        self.root_controller.add_new_password(
            for_user=user_email, web_name=web_name, web_url=web_url, username=username, password=password
        )

        # If the user saved a password successfully
        if self.parent_window.password_saved_successfully:

            self.parent_window.website_name.set("")
            self.parent_window.website_url.set("")
            self.parent_window.username.set(user_email)
            self.parent_window.password.set("")

        # Resetting the variable
        self.parent_window.password_saved_successfully = False
