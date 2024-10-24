from widgets import *


class AboutWindow(Window):
    """About window of the application"""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        # Creating the navigation bar menus
        self.nav_bar.add_nav_menu(
            "SignUp",
            action=lambda: self.controller.show_window("SignupWindow")
        )
        self.nav_bar.add_nav_menu(
            "Login",
            action=lambda: self.controller.show_window("LoginWindow")
        )
        self.nav_bar.add_nav_menu(
            "About",
            action=lambda: self.controller.show_window("AboutWindow"),
            is_active=True
        )

        # Adding the page to the body
        self.add_pages(PageOne)

        self.body.show_frame(PageOne)


class PageOne(TwoColumnBody):

    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        self.add_image(self.root_controller.images["reset_window"]["page_one"])
        self.left_frame.config(pady=45)
