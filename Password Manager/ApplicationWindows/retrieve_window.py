from widgets import *
from tkinter import messagebox


class RetrieveWindow(Window):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.nav_bar.add_nav_menu(
            label="Add",
            action=lambda: self.controller.show_window("AddWindow"),
        )
        self.nav_bar.add_nav_menu(
            label="Retrieve",
            action=lambda: self.controller.show_window("RetrieveWindow"),
            is_active=True
        )
        self.nav_bar.add_nav_menu(
            label="Logout",
            action=lambda: self.logout(),
        )

        self.website_name = StringVar()
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

    def retrieve_password(self):
        """Retrieves password"""
        website = self.website_name.get().title()
        user_account = self.controller.currently_logged_in_account.get()

        if website.strip() == "":
            messagebox.showerror(
                title="Error",
                message="FIELDS CANNOT BE EMPTY!"
            )
            return

        passwords = self.controller.retrieve_password(user_account, website)
        if passwords is None:
            return

        self.body.children_frames[PageOne].website_label.config(
            text=f"Showing password for: {website.title()}"
        )
        self.body.children_frames[PageOne].show_passwords(passwords)


class PageOne(Body):

    def __init__(self, parent, controller, **kw):
        super().__init__(parent, controller, **kw)

        self.heading_label = MyLabel(
            self,
            text="Enter the name of the website:",
            background=BODY_COLOR
        )
        self.heading_label.grid(row=0, column=0, pady=(30, 5), sticky=W)

        self.search_frame = Frame(self, bg=BODY_COLOR)
        self.search_frame.grid(row=1, column=0, pady=(10, 30))

        self.search_box = MyEntry(
            self.search_frame,
            textvar=self.parent_window.website_name
        )
        self.search_box.grid(row=1, column=0, sticky=E)
        self.search_box.config(width=66)

        self.search_btn = MyButton(
            self.search_frame,
            text="Search",
            command=lambda: self.parent_window.retrieve_password(),
            width=14,
        )
        self.search_btn.grid(row=1, column=1, padx=(10, 0), sticky=W)

        self.website_label = MyLabel(self, text="Showing password for: ", font=(MASTER_FONT, 14, "bold"))
        self.website_label.grid(row=2, column=0, sticky=W)

        self._create_password_frame()

    def _create_password_frame(self):
        """Creates the passwords frame"""
        self.passwords_frame = Frame(self, bg=BODY_COLOR, width=500)
        self.passwords_frame.grid(row=3, column=0, pady=(30, 500), sticky=EW)

        self.account_label = MyLabel(self.passwords_frame, text="Account", background=BODY_COLOR)
        self.password_label = MyLabel(self.passwords_frame, text="Password", background=BODY_COLOR)

        self.account_label.grid(row=0, column=0, sticky=W, padx=(0, 350), pady=(0, 20))
        self.password_label.grid(row=0, column=1, sticky=W, pady=(0, 20))

    def show_passwords(self, passwords):
        """Shows all the passwords in the passwords frame"""
        # Destroying the previous password frame
        self.passwords_frame.destroy()

        # Creating the passwords frame again
        self._create_password_frame()

        # Placing all the passwords
        row = 1
        for account, password in passwords:
            account_label = MyLabel(self.passwords_frame, text=account)
            password_label = MyLabel(self.passwords_frame, text=password)

            account_label.grid(row=row, column=0, sticky=W, pady=(5, 5))
            password_label.grid(row=row, column=1, sticky=W, pady=(5, 5))
            row += 1
