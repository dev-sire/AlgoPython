from widgets import *
from tkinter import messagebox


class SignupWindow(Window):
    """Signup window for the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Creating the navigation bar menus
        self.nav_bar.add_nav_menu(
            "SignUp",
            action=lambda: self.controller.show_window("SignupWindow"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            "Login",
            action=lambda: self.controller.show_window("LoginWindow")
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_window("AboutWindow")
        )

        # Variables to store inputs
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.email = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        # Adding the page to the body
        self.add_pages(PageOne, PageTwo)

        self.body.show_frame(PageOne)

    def signup_user(self):
        """Sign up a new user"""

        # Getting all the user inputs
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        email = self.email.get()
        password = self.password.get()

        if password.strip() == "" or self.confirm_password.get().strip() == "":
            messagebox.showerror(
                title="Signup Error!",
                message="PASSWORD CANNOT BE EMPTY!"
            )
            return

        if password != self.confirm_password.get():
            messagebox.showerror(
                title="Signup Error!",
                message="PASSWORD DIDN'T MATCHED!\nENTER THE PASSWORD CAREFULLY."
            )
            return

        self.controller.create_new_account(
            first_name=first_name, last_name=last_name, email=email, password=password
        )

        self.first_name.set("")
        self.last_name.set("")
        self.email.set("")
        self.password.set("")
        self.confirm_password.set("")

        self.show_page("PageOne")
        self.controller.show_window("LoginWindow")


class PageOne(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["signup_window"]["page_one"])

        self.first_name_input = TwoRowsInputBox(
            self.right_frame,
            label="Enter your first name: ",
            var=self.parent_window.first_name
        )
        self.last_name_input = TwoRowsInputBox(
            self.right_frame,
            label="Enter your last name: ",
            var=self.parent_window.last_name
        )
        self.email_input = TwoRowsInputBox(
            self.right_frame,
            label="Enter your email: ",
            var=self.parent_window.email
        )

        self.add_inputs([self.first_name_input, self.last_name_input, self.email_input])

        self.proceed_btn = MyButton(
            self.right_frame,
            text="Proceed",
            command=lambda: self.proceed_to_page_two()
        )
        self.proceed_btn.grid(row=3, column=0, columnspan=2, pady=(30, 0))

        self.right_frame.config(pady=55)

        self.first_name_input.entry.bind("<Return>", lambda e: self.last_name_input.entry.focus_set())
        self.last_name_input.entry.bind("<Return>", lambda e: self.email_input.entry.focus_set())
        self.email_input.entry.bind("<Return>", lambda e: self.proceed_to_page_two())

    def proceed_to_page_two(self):
        """Proceeds to the second page"""

        first_name = self.first_name_input.entry.get()
        last_name = self.last_name_input.entry.get()
        email = self.email_input.entry.get()

        if first_name.strip() == "" or last_name.strip() == "" or email.strip() == "":
            messagebox.showerror(
                title="Signup Error!",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        self.parent_window.show_page("PageTwo")


class PageTwo(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["signup_window"]["page_two"])

        self.password_input = TwoRowsInputBox(
            self.right_frame,
            label="Create a password: ",
            var=self.parent_window.password
        )
        self.cnf_pass_input = TwoRowsInputBox(
            self.right_frame,
            label="Confirm password: ",
            var=self.parent_window.confirm_password
        )

        self.password_input.entry.config(show="*")

        self.add_inputs([self.password_input, self.cnf_pass_input])

        self.previous_btn = ttk.Button(
            self.right_frame,
            text="Go back",
            width=12,
            command=lambda: self.controller.show_frame("PageOne")
        )
        self.previous_btn.grid(row=2, column=0, columnspan=1, sticky=W, pady=(30, 0))
        self.previous_btn.config(style=None)

        self.signup_btn = MyButton(
            self.right_frame,
            text="Create account",
            width=25,
            command=lambda: self.parent_window.signup_user()
        )
        self.signup_btn.grid(row=2, column=1, columnspan=1, sticky=E, pady=(30, 0))

        self.right_frame.config(pady=90)

        self.password_input.entry.bind("<Return>", lambda e: self.cnf_pass_input.entry.focus_set())
        self.cnf_pass_input.entry.bind("<Return>", lambda e: self.parent_window.signup_user())
