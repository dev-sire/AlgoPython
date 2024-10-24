from widgets import *
from tkinter import messagebox
from functions import valid_email


class ResetWindow(Window):
    """Reset window for resetting the master password"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nav_bar.add_nav_menu(
            label="Back to Login",
            action=lambda: self.interrupt_reset_process()
        )

        self.account_email = StringVar()
        self.otp = StringVar()
        self.new_password = StringVar()
        self.confirm_new_password = StringVar()

        self.add_pages(PageOne, PageTwo, PageThree)
        self.show_page("PageOne")

    def interrupt_reset_process(self):
        """Interrupts the reset process"""
        self.account_email.set("")
        self.otp.set("")
        self.new_password.set("")
        self.confirm_new_password.set("")
        self.controller.show_window("LoginWindow")

    def reset_master_password(self):
        """Resets the master password for the user"""
        new_password = self.new_password.get()

        if new_password != self.confirm_new_password.get():
            messagebox.showerror(
                title="Error",
                message="PASSWORDS DIDN'T MATCHED\nPLEASE ENTER THE PASSWORD CAREFULLY."
            )
            return

        self.controller.reset_master_password(self.account_email.get(), new_password)


class PageOne(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["reset_window"]["page_one"])

        self.email_entry = TwoRowsInputBox(
            self.right_frame,
            label="Enter your email:",
            var=self.parent_window.account_email,
        )
        self.email_entry.entry.bind("<Return>", lambda: self.proceed_to_second_page())

        self.add_inputs([self.email_entry])

        self.proceed_btn = MyButton(
            self.right_frame,
            text="Proceed",
            command=lambda: self.proceed_to_second_page()
        )
        self.proceed_btn.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        self.right_frame.config(pady=140)

    def proceed_to_second_page(self):
        """Checks the email and proceeds to the second page"""
        email = self.parent_window.account_email.get()

        if not valid_email(email):
            messagebox.showerror(
                title="Error",
                message=f"PLEASE ENTER A VALID EMAIL ADDRESS!"
            )
            return

        if email not in self.root_controller.registered_users():
            messagebox.showerror(
                title="Error",
                message="USER ACCOUNT NOT FOUND. PLEASE ENTERED THE EMAIL YOU REGISTERED FOR THE APPLICATION"
            )
            return

        self.parent_window.show_page("PageTwo")
        self.root_controller.send_otp(email)


class PageTwo(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["reset_window"]["page_two"])
        self.left_frame.config(pady=45)

        self.otp_entry = TwoRowsInputBox(
            self.right_frame,
            label="Enter the OTP:",
            var=self.parent_window.otp,
        )
        self.otp_entry.entry.bind("<Return>", lambda: self.proceed_to_third_page())

        self.add_inputs([self.otp_entry])

        self.confirm_otp_btn = MyButton(
            self.right_frame,
            text="Confirm",
            command=lambda: self.proceed_to_third_page()
        )
        self.confirm_otp_btn.grid(row=1, column=0, columnspan=2, pady=(20, 0))

        self.right_frame.config(pady=140)

    def proceed_to_third_page(self):
        """Proceeds to the third page"""
        actual_otp = self.root_controller.otp.get()
        user_entered_otp = self.otp_entry.entry.get()

        if actual_otp == 0:
            messagebox.showerror(
                title="Error",
                message="SESSION EXPIRED!\nPLEASE TRY AGAIN."
            )
            self.parent_window.interrupt_reset_process()
            return

        if str(user_entered_otp) != str(actual_otp):
            messagebox.showerror(
                title="Invalid Credentials",
                message="INVALID OTP\n\nPLEASE ENTER THE OTP CORRECTLY"
            )
            return

        self.parent_window.show_page("PageThree")


class PageThree(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["reset_window"]["page_three"])
        self.left_frame.config(pady=110)

        self.password_entry = TwoRowsInputBox(
            self.right_frame,
            label="Enter new password:",
            var=self.parent_window.new_password,
        )
        self.cnf_password_entry = TwoRowsInputBox(
            self.right_frame,
            label="Confirm new password:",
            var=self.parent_window.confirm_new_password,
        )
        self.password_entry.entry.config(show="*")

        self.add_inputs([self.password_entry, self.cnf_password_entry])

        self.confirm_otp_btn = MyButton(
            self.right_frame,
            text="Change Password",
            command=lambda: self.parent_window.reset_master_password()
        )
        self.confirm_otp_btn.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        self.right_frame.config(pady=110)
