from widgets import *
from tkinter import messagebox


class LoginWindow(Window):
    """Login window of the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Creating the navigation bar menus
        self.nav_bar.add_nav_menu(
            "SignUp",
            action=lambda: self.controller.show_window("SignupWindow"),
        )
        self.nav_bar.add_nav_menu(
            "Login",
            action=lambda: self.controller.show_window("LoginWindow"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_window("AboutWindow"),
        )

        # Variables to store inputs
        self.email = StringVar()
        self.password = StringVar()

        # Adding the page to the body
        self.add_pages(PageOne)

        self.show_page("PageOne")

    def login_to_account(self):
        """Log in to the account"""

        # Getting the entered email and password
        email = self.email.get()
        password = self.password.get()

        if email.strip() == "" or password.strip() == "":
            messagebox.showerror(
                title="Login Error",
                message=f"FIELDS CANNOT BE EMPTY!"
            )
            return

        # Logging in the user
        self.controller.login_to_account(email, password)

        # Resetting the input fields
        logged_in_account = self.controller.currently_logged_in_account.get()
        if logged_in_account != NONE:
            self.email.set("")

        self.password.set("")


class PageOne(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["login_window"]["page_one"])

        self.email_input = TwoRowsInputBox(
            self.right_frame,
            label="Enter your email: ",
            var=self.parent_window.email
        )
        self.password_input = TwoRowsInputBox(
            self.right_frame,
            label="Enter your password: ",
            var=self.parent_window.password
        )
        self.password_input.entry.config(show="*")

        self.add_inputs([self.email_input, self.password_input])

        self.show_pass_var = IntVar()
        show_password = ttk.Checkbutton(
            self.right_frame,
            text="Show Password",
            variable=self.show_pass_var,
            command=lambda: self.toggle_password_visibility()
        )
        show_password.grid(row=2, column=0, pady=(20, 0), sticky=W)

        self.forgot_password_btn = Button(
            self.right_frame,
            text="Forgot Password?",
            command=lambda: self.root_controller.show_window("ResetWindow"),
            bg=BODY_COLOR,
            fg=COLORS["pink"],
            font=(MASTER_FONT, 10),
            highlightthickness=0,
            borderwidth=0,
            cursor="circle",
            activebackground=COLORS["pink"],
            activeforeground=TEXT_COLOR,
        )
        self.forgot_password_btn.grid(row=2, column=1, pady=(20, 0), sticky=E)

        self.login_btn = MyButton(
            self.right_frame,
            text="Login",
            command=lambda: self.parent_window.login_to_account()
        )
        self.login_btn.grid(row=3, column=0, columnspan=2, pady=(30, 0))

        self.right_frame.config(pady=80)

        self.email_input.entry.bind("<Return>", lambda e: self.password_input.entry.focus_set())
        self.password_input.entry.bind("<Return>", lambda e: self.parent_window.login_to_account())

    def toggle_password_visibility(self):
        """Toggles the visibility of the password input"""
        value = self.show_pass_var.get()
        if value == 1:
            self.password_input.entry.config(show="")
        else:
            self.password_input.entry.config(show="*")
