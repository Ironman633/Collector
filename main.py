import re
import json
import hashlib
import firebase_admin
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.uix.image import Image
from kivymd.uix.card import MDCard
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivymd.uix.progressbar import MDProgressBar
from firebase_admin import credentials, db
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFillRoundFlatIconButton, MDRectangleFlatButton, MDFlatButton


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "collect-62f2a",
  "private_key_id": "2559697d478b6e48d943d7244a8985244788ac6f",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC7R1rFBNto0MgH\nM+aJ5x6NEXgvJ2Sg2nh/9YXy8tzXr8w3sVZUwxzuMI0Sd5BjWERaBVbMSBOmLv8o\nXpo2apvZi/+Z88KQb/LkaIOHbNnkxvDE/hztQRc0La4PLhFM/NPyHQOfLg2par1p\n+b4UuW1RROGQI5WqE9sz/9NSwNiLA/ipiIt8YQwk92Q9TwVa0/9Hvp7RVNEGgl05\nLI/Uvpij1ghfntDuCyBu7l9T4UrDorvlwlvY1zDS1t9b0ix5VyHtY3gvq8jqbE7S\n1QbkJO/RUc6QkfxNzFsrCGwcRyj1vbwwwWSEiUi/UdulyG9buoIDsIswst00gJ9Q\nl72NOTXxAgMBAAECggEAB3QOSn+IPOpsP48i+nOKjXo3woaqlFVFjPAoUdQ1Eldy\nhPfnk+2E+fzQLH86LZ3+cGe8fdpTf95odMKZGBfTlouiE042fNmbvNfk/i+Il3iM\nbgaf/5hC1GaKAhwm/52jUMQzV/M1A3xWSACyvi/oCB856+riordyFqZ0kltO8u9W\n19iRuIZ9xnSi585w4xsKjdabwYJIfov1qP0e/SsJtJj0jIaXuBYXiZ0B2gPdoJPF\n5ubaFXIu/TiW/ddO02+PmprX0H2x3XqEFEvXdoq17ynt/Ft6c4llP1hHxI5L+1/u\nB8tH4s+nVBbpbBAPQOuHEZJTRB0UC9hq0nkL6PM9kQKBgQDgWyogPg1h8jjWEBzd\nYBNovIHC1GdABAQHjlYzs5tqdcICXt916qqSKiU2hfonECDrRpwQfSatrBXvvctx\nRZbh6keXl8V9JqCem1FN8Vmbw1SM7f81CmGkx8uqkMBGH8yDZ/AeuxuCvG+ySAIM\np2Aqf0D8BRn5h/Vk5Tkc8uJvWQKBgQDVsW93SDgarvZE6cHgxFwRElNNSnAt61vv\n8JgvGWfMumrGFaO6DdL8kbsm42Bdiq+6B63XUMTDGwRYISAceDJ+LIiP202jOV3a\nSugtnHqNm4KziNyOlIdFUdZmImCUTH3hVdQgNfqa7I4k2plgkl2IaS9cSRUCTef8\n9rTjZPSAWQKBgAz+us3rSjMmKIydmk5oRjeG061JSEG4+dLGN8/+0z2zXG1uuVrH\nIOIedtFVqUuh74YxLND3rsnYcdzVDXeeJEMposPxEotRNXR6Ypc1J4+SHM+c6W9V\nDprQx8c1Yy2sodfqqUneZJWJ/J5C9XtuJm/Ptx/h28NMULZrYIeAugThAoGAXQKO\n3p87dDnFDPeloFw3KmMMiO6mZwYzDPtuccmgCVb2VGNk0P1lYPNZPzLmZbCQjer7\numT4T2d5+5XncRzL9WkSw3KTl0DH3dSOvBOIsAwI1nXycciqG/zj0a6S1Nl6TNLb\nsm1sN3RQ5i+TZJowRchqicNxdoBMQilrUDJHzXkCgYAxqIixihOFGLtE1I8HG06M\nFiFy92PbQ7pTEHSJDJm9MDk2pHU4P6MrVaTTvAM8cFtheVFdoQ5cJs4gdKBBsZZW\nV0++o3WAIalm2tMummkKGHgt/ObNvvDFWZvqUg5lBF6b6SIKxpGJKgNxkggsMF0S\n9iHhMo/cdSf4Rw3ZzWI8Jg==\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-6odu7@collect-62f2a.iam.gserviceaccount.com",
  "client_id": "108220296849664319898",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-6odu7%40collect-62f2a.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://collect-62f2a-default-rtdb.asia-southeast1.firebasedatabase.app/ '
})

def hash_password(password):
    """Hash the password for secure storage."""
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_email(email):
    """Validate the email format."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.credentials_file = "credentials.json"
        self.logged_in_email = "logged_in.json"

        self.result_card = MDCard(
            size_hint=(None, None),
            size=("280dp", "140dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            padding="16dp",
            orientation="vertical",
            ripple_behavior=True,
            md_bg_color=(0.1, 0.6, 0.6, 1),
            opacity=0,
        )
        self.card_label = MDLabel(
            text="Character: None\nPoints: 0",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
        )
        self.result_card.add_widget(self.card_label)
        self.add_widget(self.result_card)

        self.email_input = MDTextField(
            hint_text="Enter your email",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint=(0.8, None),
            height="40dp",
        )
        self.add_widget(self.email_input)

        password_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(0.8, None),
            height="40dp",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
        )

        self.password_input = MDTextField(
            hint_text="Enter your password",
            password=True,
            size_hint=(0.85, None),
            pos_hint={"center_x":0.5, "center_y":0.2},
            max_text_length=6
        )
        password_layout.add_widget(self.password_input)

        self.eye_icon_button = MDIconButton(
            icon="eye-off",
            size_hint=(None, None),
            size=("40dp", "40dp"),
            pos_hint={"center_y": 0.1},
        )
        self.eye_icon_button.bind(on_release=self.toggle_password_visibility)
        password_layout.add_widget(self.eye_icon_button)

        self.add_widget(password_layout)

        self.login_button = MDRaisedButton(
            text="Login",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.login_button.bind(on_release=self.handle_login)
        self.add_widget(self.login_button)

        self.create_account_button = MDRaisedButton(
            text="Create Account",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
        )
        self.create_account_button.bind(on_release=self.handle_create_account)
        self.add_widget(self.create_account_button)

    def load_logged_in_email(self):
        """Load the logged-in email from the file."""
        try:
            with open(self.logged_in_email, "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except (FileNotFoundError, KeyError):
            return None


    def toggle_password_visibility(self, instance):
        """Toggle password visibility."""
        if self.password_input.password:
            self.password_input.password = False
            self.eye_icon_button.icon = "eye"
        else:
            self.password_input.password = True
            self.eye_icon_button.icon = "eye-off"

    def handle_login(self, instance):
        """Handle login logic."""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if not email or not password:
            self.show_message("Please enter email and password!")
            return

        hashed_password = hash_password(password)
        ref = db.reference("users")
        user_data = ref.child(email.replace(".", ",")).get()

        if user_data and user_data.get("password") == hashed_password:
            self.save_logged_in_email(email)
            self.manager.current = "game"
            self.manager.transition.direction = 'left'
            self.manager.get_screen("account").update_email_label(email)  
            self.manager.get_screen("game").redeem_code_input.text=''
            self.manager.get_screen("game").result_card.opacity=0
            self.result_card.opacity=0
            self.email_input.text = ''
            self.password_input.text = ''
            self.eye_icon_button.icon = "eye-off"
        else:
            self.show_message("Invalid email or password!")

    def handle_create_account(self, instance):
        """Handle account creation logic."""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()
        user_name = "Not set"
        user_age = "Not set"
        user_id = "Not set"


        if not email or not password:
            self.show_message("Please enter email and password!")
            return

        hashed_password = hash_password(password)
        ref = db.reference("users")
        email_key = email.replace(".", ",")

        if ref.child(email_key).get():
            self.show_message("Account already exists!")
        else:
            ref.child(email_key).set({
            "password": hashed_password,
            "user_name": user_name,
            "user_age": user_age,
            "user_id": user_id,
            "points": 0,
            "used_codes": {}
        })
            self.save_logged_in_email(email)
            self.manager.current = "game"
            self.manager.transition.direction = 'left'
            self.manager.get_screen("account").update_email_label(email) 
            self.manager.get_screen("game").result_card.opacity=0
            self.result_card.opacity=0
            self.email_input.text = ''
            self.password_input.text = ''
            self.eye_icon_button.icon = "eye-off"

    def load_credentials(self):
        """Load credentials from the file line by line."""
        credentials = {}
        try:
            with open(self.credentials_file, "r") as file:
                for line in file:
                    entry = json.loads(line.strip())
                    credentials.update(entry)
        except FileNotFoundError:
            pass
        return credentials

    def save_credentials(self, credentials):
        """Save each email and hashed password on a new line."""
        with open(self.credentials_file, "w") as file:
            for email, password in credentials.items():
                json.dump({email: password}, file)
                file.write("\n")


    def save_logged_in_email(self, email):
        """Persist logged-in email."""
        with open("logged_in.json", "w") as file:
            json.dump({"email": email}, file)


    def show_message(self, message):
        self.card_label.text = message
        anim = Animation(opacity=1, d=0.5)
        anim.start(self.result_card)



class redeemCodeGame(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data_file = "user_data.json"
        self.logged_in_email = None
        self.load_user_data()

        self.points_label = MDLabel(
            text="Points: 0",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.93},
            theme_text_color="Primary",
            font_style="H6",
        )
        self.add_widget(self.points_label)

        self.redeem_code_input = MDTextField(
            hint_text="Enter redeem code",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint=(0.8, None),
            height="40dp",
        )
        self.add_widget(self.redeem_code_input)

        self.submit_button = MDRaisedButton(
            text="Submit",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
        )
        self.submit_button.bind(on_release=self.check_redeem_code)
        self.add_widget(self.submit_button)


        self.account_button = MDIconButton(
            icon="account-circle",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.9, "center_y": 0.05},
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.account_button.bind(on_release=self.go_account)
        self.add_widget(self.account_button)

        self.team_button = MDIconButton(
            icon="cards",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.5, "center_y": 0.05},
            md_bg_color=(90/255, 84/255, 255/255, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.team_button.bind(on_release=self.go_team)
        self.add_widget(self.team_button)

        self.redeem_button = MDIconButton(
            icon="gift-outline",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.1, "center_y": 0.07},
            md_bg_color=(0,150/255, 136/255, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.add_widget(self.redeem_button)

        self.result_card = MDCard(
            size_hint=(None, None),
            size=("280dp", "140dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            padding="16dp",
            orientation="vertical",
            ripple_behavior=True,
            md_bg_color=(0.1, 0.6, 0.6, 1),
            opacity=0,
        )
        self.card_label = MDLabel(
            text="Character: None\nPoints: 0",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
        )
        self.result_card.add_widget(self.card_label)
        self.add_widget(self.result_card)

    def on_enter(self):
        """Load logged-in user email and update points."""
        login_screen = self.manager.get_screen("login")
        self.logged_in_email = login_screen.load_logged_in_email()

        if self.logged_in_email:
            email_key = self.logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if user_data:
                points = user_data.get("points", 0)
                self.update_points_label(points)
            else:
                self.update_points_label(0)
        else:
            self.update_points_label(0)



    def load_user_data(self):
        try:
            with open(self.user_data_file, "r") as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}

    def save_user_data(self):
        with open(self.user_data_file, "w") as file:
            json.dump(self.user_data, file, indent=4)

    def update_points_label(self, new_points):
        """Update the points label with the latest points."""
        self.points_label.text = f"Points: {new_points}"


    def check_redeem_code(self, instance):
        """Check the redeem code and update points."""
        redeem_code = self.redeem_code_input.text.strip()

        if not self.logged_in_email:
            self.show_message("No user logged in!")
            return

        email_key = self.logged_in_email.replace(".", ",")
        ref = db.reference("users")
        user_data = ref.child(email_key).get()

        if not user_data:
            self.show_message("User data not found!")
            return

        if "used_codes" not in user_data:
            user_data["used_codes"] = {}

        if redeem_code in user_data["used_codes"]:
            self.show_message("Code already used!")
            return

        predefined_codes = {
            "Iron3000": {"character": "Iron Man\n (End Game)", "points": 3000},
            "Cap": {"character": "Captain America\n (The Avenger)", "points": 1000},
            "Thorlove": {"character": "Thor\n (Thor Love and Thunder)", "points": 1500},
            "Hulk": {"character": "Hulk\n (The Avenger)", "points": 2000},
            "Widow": {"character": "Black Widow\n (Black Widow)", "points": 2000},
            "CapMarvel": {"character": " Captain Marvel\n (The Captain Marvel)", "points": 1000},
            "Spidy": {"character": "Spiderman\n (Far From Home)", "points": 3000},
            "Panther": {"character": "Black Panther\n (Black Panther)", "points": 2000},
            "Strange": {"character": "Doctor Strange\n (Infinty War)", "points": 3000},
            "Wanda": {"character": "Scarlet Witch\n (Wanda Vision)", "points": 1000},
            "Vision": {"character": "Vision\n (Age of Ultorn)", "points": 1000},
            "Ant": {"character": "Antman\n (Antman)", "points": 1500},
            "Falcon": {"character": "Falcon\n (Civil War)", "points": 1500},
            "Bucky": {"character": "Winter Soldier\n (Captain America the Winter Soldier)", "points": 1500},
            "Loki": {"character": "Loki\n (Loki)", "points": 10000},
            "Stark": {"character": "Tony Stark\n (The Avenger)", "points": 2000},
            "Fury": {"character": "Nick Fury\n (The Avenger)", "points": 300},
            "Hawk": {"character": "Hawkeye\n (The Avenger)", "points": 500},
            "Villain": {"character": "Thanos\n (Infinity War)", "points": 10000},
            "Ultron": {"character": "Ultron\n (Age of Ultron)", "points": 1000},
            "Red": {"character": "Red Skull\n (Captain America)", "points": 1000},
            "Hela": {"character": "Hela\n (Thor Ragnarok)", "points": 2000},
            "Kill": {"character": "Killmonger\n (Black Panther)", "points": 1500},
            "No Death": {"character": "Deadpool\n (Deadpool and Wolverine)", "points": 9000},
            "Wolverine": {"character": "Wolverine\n (Deadpool and Wolverine)", "points": 6000},
            "she": {"character": "She-Hulk\n (She-Hulk)", "points": 100},
            "Venom3": {"character": "Venom\n (Venom The Last Dance)", "points": 2000},
            "Groot": {"character": "Groot\n (Guardians of the Galaxy)", "points": 500},
            "Rocket": {"character": "Rocket\n (Guardians of the Galaxy)", "points": 1500},
            "Gamora": {"character": "Gamora\n (Guardians of the Galaxy)", "points": 500},
            "Star": {"character": "Star Lord\n (Guardians of the Galaxy)", "points": 1500},
            "Drax": {"character": "Drax\n (Guardians of the Galaxy)", "points": 100},
            "Mantis": {"character": "Mantis\n (Guardians of the Galaxy)", "points": 400},
            "Nebula": {"character": "Nebula\n (Guardians of the Galaxy)", "points": 100},
            "Marvel's Flash": {"character": "Makkari\n (Eternals)", "points": 2000},
        }

        if redeem_code in predefined_codes:
            character = predefined_codes[redeem_code]["character"]
            points = predefined_codes[redeem_code]["points"]

            user_data["used_codes"][redeem_code] = {"character": character, "points": points}
            new_points = user_data.get("points", 0) + points

            ref.child(email_key).update({
                "points": new_points,
                "used_codes": user_data["used_codes"]
            })

            self.update_points_label(new_points)
            self.show_message(f"Character: {character}\nPoints: {points}")
        else:
            self.show_message("Invalid redeem code!")




    def show_message(self, message):
        """Display a message in the result card and automatically hide it after a few seconds."""
        self.card_label.text = message
        anim = Animation(opacity=1, d=0.5)
        anim.start(self.result_card)

        Clock.schedule_once(self.hide_message, 3)

    def hide_message(self, *args):
        """Hide the result card."""
        anim = Animation(opacity=0, d=0.5)
        anim.start(self.result_card)

    def go_account(self, instance):
        self.manager.current="account"
        self.manager.transition.direction = 'left'

    def go_team(self, instance):
        self.manager.current="team"
        self.manager.transition.direction = 'left'
        


class teamscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.logged_in_email = self.load_logged_in_email()
        self.user_data_file = "user_data.json"

        # Team Label
        self.team_label = MDLabel(
            text="YOUR TEAM",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            text_color=(90/255, 84/255, 255/255, 1),
            theme_text_color="Custom",
            font_style="H4",
            bold=True,
            underline=True,
        )
        self.add_widget(self.team_label)

        # Add a progress bar
        self.progress_bar = MDProgressBar(
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint=(0.8, None),
            height="15dp",
        )
        self.add_widget(self.progress_bar)

        # Scrollable Grid Layout for Collected Cards
        self.scroll_view = ScrollView(size_hint=(1, 0.8), pos_hint={"center_x": 0.5, "center_y": 0.35})
        self.grid_layout = GridLayout(cols=1, spacing=dp(10), size_hint_y=None, padding=15)
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.scroll_view.add_widget(self.grid_layout)
        self.add_widget(self.scroll_view)

        # Navigation Buttons
        self.account_button = MDIconButton(
            icon="account-circle",
            size_hint=(0.15, None),
            pos_hint={"center_x": 0.9, "center_y": 0.05},
            md_bg_color=(0.5, 0.5, 0.5, 1),
            text_color=(1, 1, 1, 1),
            theme_text_color='Custom',
        )
        self.account_button.bind(on_release=self.go_account)
        self.add_widget(self.account_button)

        self.redeem_button = MDIconButton(
            icon="gift-outline",
            size_hint=(0.15, None),
            pos_hint={"center_x": 0.1, "center_y": 0.05},
            md_bg_color=(0, 150/255, 136/255, 1),
            text_color=(1, 1, 1, 1),
            theme_text_color='Custom',
        )
        self.redeem_button.bind(on_release=self.change_to_redeem)
        self.add_widget(self.redeem_button)

    def load_logged_in_email(self):
        """Load the logged-in email from the file."""
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except (FileNotFoundError, KeyError):
            return None

    def on_enter(self):
        """Load and display collected cards when the screen is entered."""
        self.grid_layout.clear_widgets()  # Clear existing cards
        self.logged_in_email = self.load_logged_in_email()  # Reload logged-in email
        if self.logged_in_email:
            email_key = self.logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if user_data:
                total_points = user_data.get("points", 0)
                progress_value = (total_points/75000)*100 # Example: Track progress towards 10,00,000 points
                self.progress_bar.value = progress_value

            if user_data and "used_codes" in user_data:
                for idx, (code, details) in enumerate(user_data["used_codes"].items()):
                    character = details.get("character", "Unknown")
                    points = details.get("points", 0)

                    # Create a card for each collected character
                    card = MDCard(
                        size_hint=(None, None),
                        size=("280dp", "140dp"),
                        orientation="vertical",
                        padding=dp(10),
                        spacing=dp(10),
                        md_bg_color=(0.1, 0.6, 0.6, 1),
                        opacity=0,  # Start with opacity 0 for animation
                    )
                    card.add_widget(MDLabel(
                        text=f"Character: {character}",
                        halign="center",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        font_style="H6",
                    ))
                    card.add_widget(MDLabel(
                        text=f"Points: {points}",
                        halign="center",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        font_style="H6",
                    ))
                    self.grid_layout.add_widget(card)

                    # Add animation to the card
                    anim = Animation(opacity=1, duration=0.5, transition="in_out_quad")
                    anim.start(card)

    def go_account(self, instance):
        self.manager.current = "account"
        self.manager.transition.direction = 'left'

    def change_to_redeem(self, instance):
        self.manager.current = "game"
        self.manager.transition.direction = 'right'

class accountscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.logged_in_email = self.load_logged_in_email()
        self.user_data_file = "user_data.json"

        self.account_icon = Image(
            source="account-circle.png",
            size_hint=(None, None),
            size=("150dp", "150dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.85},
        )
        self.add_widget(self.account_icon)

        email_card = MDCard(
            size_hint=(0.95, None),
            height="50dp",
            pos_hint={"center_x": 0.5, "center_y": 0.7},
            md_bg_color=(0.2, 0.6, 0.8, 1),
            radius=[10, 10, 10, 10],
        )

        entry_card = MDCard(
            size_hint=(0.95, None),
            height="120dp",
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            md_bg_color=(0.9, 0.9, 0.9, 1),
            radius=[10, 10, 10, 10],
        )

        self.email_label = MDLabel(
            text=self.logged_in_email if self.logged_in_email else "No user logged in",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
        )
        email_card.add_widget(self.email_label)
        self.add_widget(email_card)

        self.entry = MDLabel(
            text=f"User Name:   \n \nAge:   \n \nUser ID:   ",
            size=("50px", "50px"),
            bold=True,
            padding="10px",
        )
        entry_card.add_widget(self.entry)
        self.add_widget(entry_card)


        self.edit_button=MDIconButton(
            icon='account-edit',
            md_bg_color=(0.5,0.5,0.5,1),
            pos_hint={"center_x" : 0.9, "center_y":0.3},
            icon_color=(1,1,1,1),
            theme_icon_color='Custom',
        )
        self.edit_button.bind(on_release=self.change_to_edit)
        self.add_widget(self.edit_button)

        self.logout_button = MDFlatButton(
            text="Logout",
            pos_hint={"center_x": 0.1, "center_y": 0.25},
            theme_text_color='Custom',
            text_color='red'
        )
        self.logout_button.bind(on_release=self.handle_logout)
        self.add_widget(self.logout_button)

        self.account_button = MDIconButton(
            icon="account-circle",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.9, "center_y": 0.07},
            md_bg_color=(0.4, 0.4, 0.4, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.add_widget(self.account_button)

        self.redeem_button = MDIconButton(
            icon="gift-outline",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.1, "center_y": 0.05},
            md_bg_color=(0, 150/255, 136/255, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.redeem_button.bind(on_release=self.change_to_redeem)
        self.add_widget(self.redeem_button)


    def load_logged_in_email(self):
        """Load the logged-in email from the file."""
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except (FileNotFoundError, KeyError):
            return None

    def update_email_label(self, email):
        """Update the email label with the logged-in email."""
        self.email_label.text = f"{email}"

    def handle_logout(self, instance):
        """Handle user logout."""
        try:
             # Clear logged-in email from file
            with open("logged_in.json", "w") as file:
                json.dump({"email": None}, file)
                
        except Exception as e:
            print(f"Error clearing logged-in user: {e}")

        self.manager.current = "login"
        self.manager.transition.direction = 'right'


    def change_to_edit(self, instance):
        self.manager.current = "edit"
        self.manager.transition.direction = 'left'

    def change_to_redeem(self, instance):
        self.manager.current = "game"
        self.manager.transition.direction = 'right'

    def on_enter(self):
        """Load user data when the account screen is entered."""
        login_screen = self.manager.get_screen("login")
        self.logged_in_email = login_screen.load_logged_in_email()

        if self.logged_in_email:
            email_key = self.logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if user_data:
                username = user_data.get("user_name", "Not set")
                age = user_data.get("user_age", "Not set")
                user_id = user_data.get("user_id", "Not set")
                points = user_data.get("points", 0)
                self.entry.text = (
                    f"User Name: {username}\n \n"
                    f"Age: {age}\n \n"
                    f"User ID: {user_id}"
                )
            else:
                self.entry.text = "User data not found."
        else:
            self.entry.text = "No user logged in."

class editscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.user_data_file = "user_data.json"

        self.message_card = MDCard(
            size_hint=(None, None),
            size=("280dp", "30dp"),
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            padding="16dp",
            orientation="vertical",
            ripple_behavior=True,
            md_bg_color=(1, 0, 0, 1),
            opacity=0,
        )
        self.message_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
        )
        self.message_card.add_widget(self.message_label)
        self.add_widget(self.message_card)

        self.back_to_account=MDIconButton(
            icon="arrow-left",
            pos_hint={"center_x":0.1, "center_y":0.95},
        )
        self.back_to_account.bind(on_release=self.to_account)
        self.add_widget(self.back_to_account)

        self.user_name_input=MDTextField(
            hint_text="Enter User Name",
            pos_hint={"center_x": 0.5, "center_y": 0.8},
            size_hint=(0.8, None),
            height="40dp",
            mode='rectangle',
        )
        self.add_widget(self.user_name_input)


        self.age=MDTextField(
            hint_text='Enter Your Age',
            pos_hint={'center_x': 0.5, 'center_y': 0.65},
            size_hint=(0.8, None),
            height='40dp',
            mode='rectangle',
            input_filter='int',
            max_text_length=3,
        )
        self.add_widget(self.age)

        self.user_id_input=MDTextField(
            hint_text="Enter User ID",
            pos_hint={'center_x':0.5, 'center_y': 0.5},
            size_hint=(0.8, None),
            height='40dp',
            mode='rectangle',
        )
        self.add_widget(self.user_id_input)


        self.save_button=MDRaisedButton(
            text="Save",
            pos_hint={"center_x": 0.5, "center_y": 0.2},
            size_hint=(0.3, 0.05)
        )
        self.save_button.bind(on_release=self.save_user_name)
        self.add_widget(self.save_button)

    def to_account(self, instance):
        self.manager.current="account"
        self.manager.transition.direction = 'right'
        
    def save_user_name(self, instance):
        """Save user data to Firebase."""
        username = self.user_name_input.text.strip()
        user_id = self.user_id_input.text.strip()
        age = self.age.text.strip()

        if not username or not user_id or not age:
            self.show_message("Please fill in all fields!")
            return

        try:
            age = int(age)
        except ValueError:
            self.show_message("Age must be a number!")
            return

        login_screen = self.manager.get_screen("login")
        logged_in_email = login_screen.load_logged_in_email()

        if logged_in_email:
            email_key = logged_in_email.replace(".", ",")
            ref = db.reference("users")
            ref.child(email_key).update({
                "user_name": username,
                "user_age": age,
                "user_id": user_id
            })

            account_screen = self.manager.get_screen("account")
            account_screen.on_enter()

            self.manager.current = "account"
            self.show_message("Details saved successfully!")
            self.user_name_input.text = ''
            self.age.text = ''
            self.user_id_input.text = ''
        else:
            self.show_message("No user logged in!")


    def show_message(self, message):
        self.message_label.text = message
        anim = Animation(opacity=1, d=0.5)
        anim.start(self.message_card)

        Clock.schedule_once(self.hide_message, 3)

    def hide_message(self, *args):
        """Hide the result card."""
        anim = Animation(opacity=0, d=0.5)
        anim.start(self.message_card)



class Collecteber(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        sm = ScreenManager()

        login_screen = LoginScreen(name="login")
        sm.add_widget(login_screen)
        sm.add_widget(redeemCodeGame(name="game"))
        sm.add_widget(teamscreen(name="team"))
        sm.add_widget(accountscreen(name="account"))
        sm.add_widget(editscreen(name="edit"))

        logged_in_email = login_screen.load_logged_in_email()
        if logged_in_email:
            sm.current = "game"
        else:
            sm.current = "login"

        return sm



if __name__ == "__main__":
    Collecteber().run()