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
from kivy.graphics import Color, Rectangle, Line, Ellipse, RoundedRectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout


cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "collect-62f2a",
  "private_key_id": "c1be4c00b8dbc96f5500f38038074726a0a0a03e",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQC/CTaxL+kPn351\nbXXvyf7e72zhS+p1u1OUZHDFv1EnVIjfrrT46jGknR8EAhsmjvq/huRHicE2Wdx+\nqehi8K+slL5a4VaxoPXTVxwbUlI7W71pZ9ydsu2rH16MUz3+2/4QU2IVRVyEVpqD\novjplZp1UzD8Y8v7jkDI9sqtJHPR5ZLUULIAB32VPiP7xLnrbLl6J+TDghnGrSAw\nT5RRrIiwMMsGUGIitMGMftUs7SosrF4BVEcNxwxn09mNcmtYrURGw/Pq3LB/Siuf\nCU1d1xbXny12+JYOeXLHGvEIAsP3KeYdieO1SRoaSK/NO0E2IBiIWStDVjqxxCDg\nTezLVRfdAgMBAAECggEAB2HGlM5oJH1oG0z9Et6+K1waxIau6yR1VG+gbzx9E1DQ\nHeyjtcsEw+NjJPo720KUbEj3Hizt6cSRLRwyDJLje1BlNTfQ1MtvN0eJoJimB+m2\nEcC8sIDJQWqOoQYRtsLSCal2eFwh4bf9LinuS92BQLsw3giZ7HViT61XgOLtQs9T\n1xkpcea4Mh3CjWnVKwWmYi8pex42BLsOHw4cbTsFMdO/RRktc4mmcs6booJ+ZF5D\n+m6fuoNBM+MCBKec/ed+EkQZz5P7ofBovIZXOvYLOY0xKfC3pvSE8zVGpbQ0cL8k\noEoLSXC9rmDcSKkuttJe+oLeT+rYLnw8f1iAYC4wdQKBgQD3xM7FWk2ZByPAQDkg\nE0ph6yV/lZDhGCXOcNwXOdsmltE5cLtjvrL32/h7V0/ay9KpIYsiFQiadxRrMzzB\nXTDiMNWDdXnCkLHMm5/zUIK0F7gIw6zmqJbS3eL7hX8ZNM8LCpaxfQizxKyuKr9a\ni2EXbkhmjynk77cx+dQz9PdGwwKBgQDFYemDDzoI3LePLsrVD0EpDCfqC3KGvugT\nQVyx+Su0FAo49IgZmlOm4zXB+siMfGrqiU3Wg4ejbB4o671ZqEA9CdkJpebdRQVe\nBwr6n1GJV3lTmdMJbTz178aP+6jvd4vRavUKS9dk44S+ke6Wpqqa0nlgD3xJDUzb\n8CSrzTh83wKBgE0pc6Ound/8gzvKRIAiwdWA3+q976LKXGvQZhqtn/yCl6Il45YK\nu73JObdf17SyKWcW1TfGCSnhz/Aawt8NYL3wq24HVeYsHdM03DlwZ2QixuOj3OLw\nuhftllTynESDV79+irO31s/1fjm3gmR2Z8ReShn2l/t+VDUyMs4Dikb1AoGAP36B\nuZE6YANwYPTydptToLqyVE2eZ84dpaQPB4laD7GqoCu5ZFMKudK5Rk9AGEElu5Cz\no1/oUB/Fi/BZlu/Syk/Sq5HctC0xzs+BLqH1frLO6p+/DXdAdvTM8SBJdc8FATbg\n4JEJFwFBgHQ9ReUTWH6AYPBaUL2gjdewVDvOAg0CgYAF3hJ3XEnoX1OkT/bY0h++\nM7poH6R9cGRWKMqVn6LCA4RLAYiwNYrGa5PfjRbuAo+amXeOjwerCp9ZmD4H50Yc\n61dBNfaBhu36pKM5yW3ziOayAr0k+cv/m4L+EMgIgr7OSy4ESYp5SYgcDLIxxYgM\nOT0YweO+EdDgNeo50p4cQQ==\n-----END PRIVATE KEY-----\n",
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
    'databaseURL':'https://collect-62f2a-default-rtdb.asia-southeast1.firebasedatabase.app/'
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

    predefined_codes = {
            "Iron3000": {"character": "Iron Man\n (End Game)", "points": 3000, "iq": 1000, "power": 1000},
            "Cap": {"character": "Captain America\n (The Avenger)", "points": 1000, "iq": 140, "power": 70},
            "Thorlove": {"character": "Thor\n (Thor Love and Thunder)", "points": 1500, "iq": 175, "power": 95},
            "Hulk": {"character": "Hulk\n (The Avenger)", "points": 2000, "iq": 185, "power": 100},
            "Widow": {"character": "Black Widow\n (Black Widow)", "points": 2000, "iq": 150, "power": 65},
            "CapMarvel": {"character": " Captain Marvel\n (The Captain Marvel)", "points": 1000, "iq": 160, "power": 90},
            "Spidy": {"character": "Spiderman\n (Far From Home)", "points": 3000, "iq": 500, "power": 80},
            "Panther": {"character": "Black Panther\n (Black Panther)", "points": 2000, "iq": 200, "power": 75},
            "Strange": {"character": "Doctor Strange\n (Infinty War)", "points": 3000, "iq": 280, "power": 90},
            "Wanda": {"character": "Scarlet Witch\n (Wanda Vision)", "points": 1000, "iq": 180, "power": 95},
            "Vision": {"character": "Vision\n (Age of Ultorn)", "points": 1000, "iq": 300, "power": 85},
            "Ant": {"character": "Antman\n (Antman)", "points": 1500, "iq": 160, "power": 60},
            "Falcon": {"character": "Falcon\n (Civil War)", "points": 1500, "iq": 130, "power": 65},
            "Soldier": {"character": "Bucky\n (The Winter Soldier)", "points": 1500, "iq": 135, "power": 75},
            "Loki": {"character": "Loki\n (Loki)", "points": 10000, "iq": 250, "power": 999},
            "Stark": {"character": "Tony Stark\n (The Avenger)", "points": 2000, "iq": 270, "power": 30},
            "Fury": {"character": "Nick Fury\n (The Avenger)", "points": 300, "iq": 160, "power": 40},
            "Hawk": {"character": "Hawkeye\n (The Avenger)", "points": 500, "iq": 140, "power": 50},
            "Villain": {"character": "Thanos\n (Infinity War)", "points": 10000, "iq": 240, "power": 100},
            "Ultron": {"character": "Ultron\n (Age of Ultron)", "points": 1000, "iq": 260, "power": 90},
            "Red": {"character": "Red Skull\n (Captain America)", "points": 1000, "iq": 180, "power": 70},
            "Hela": {"character": "Hela\n (Thor Ragnarok)", "points": 2000, "iq": 190, "power": 95},
            "Kill": {"character": "Killmonger\n (Black Panther)", "points": 1500, "iq": 170, "power": 75},
            "No Death": {"character": "Deadpool\n (Deadpool and Wolverine)", "points": 9000, "iq": 130, "power": 85},
            "Wolverine": {"character": "Wolverine\n (Deadpool and Wolverine)", "points": 6000, "iq": 125, "power": 90},
            "she": {"character": "She-Hulk\n (She-Hulk)", "points": 100, "iq": 150, "power": 85},
            "Venom3": {"character": "Venom\n (Venom The Last Dance)", "points": 2000, "iq": 120, "power": 80},
            "Groot": {"character": "Groot\n (Guardians of the Galaxy)", "points": 500, "iq": 90, "power": 70},
            "Rocket": {"character": "Rocket\n (Guardians of the Galaxy)", "points": 1500, "iq": 220, "power": 60},
            "Gamora": {"character": "Gamora\n (Guardians of the Galaxy)", "points": 500, "iq": 150, "power": 75},
            "Star": {"character": "Star Lord\n (Guardians of the Galaxy)", "points": 1500, "iq": 140, "power": 65},
            "Drax": {"character": "Drax\n (Guardians of the Galaxy)", "points": 100, "iq": 0, "power": 85},
            "Mantis": {"character": "Mantis\n (Guardians of the Galaxy)", "points": 400, "iq": 110, "power": 60},
            "Nebula": {"character": "Nebula\n (Guardians of the Galaxy)", "points": 100, "iq": 150, "power": 75},
            "Marvel's Flash": {"character": "Makkari\n (Eternals)", "points": 2000, "iq": 160, "power": 80},
}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data_file = "user_data.json"
        self.logged_in_email = None
        self.load_user_data()

        self.points_button = MDFillRoundFlatIconButton(
            text="0",  # Default points
            icon="star",  # You can change the icon
            pos_hint={"center_x": 0.5, "center_y": 0.93},
            size_hint=(None, None),
            md_bg_color=(1, 1, 1, 1),  # White color
            text_color=(0, 0, 0, 1), # Black color  
            icon_color=(1, 0.84, 0, 1),  # Gold color
            icon_size="30px",
        )
        self.add_widget(self.points_button)

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
            size_hint=(0.9, None),
            height=dp(320),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            padding=dp(5),
            spacing=dp(5),
            orientation="vertical",
            ripple_behavior=True,
            md_bg_color=(0.12, 0.12, 0.2, 1),
            radius=[25],
            elevation=0,
            opacity=0,
        )
        # Add a label to the card for displaying messages
        self.card_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
            size_hint=(0.4, None),
            valign='top',
        )
        # This makes the label adjust its height based on content
        #self.card_label.bind(
        #    width=lambda *x: self.card_label.setter('text_size')(self.card_label, (self.card_label.width, None)),
        #    texture_size=lambda *x: self.card_label.setter('height')(self.card_label, self.card_label.texture_size[1])
        #)
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
        """Update the button text to show points."""
        self.points_button.text = str(new_points)
        

        

    def check_redeem_code(self, instance):
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
    
        # Check if code already used
        if redeem_code in user_data["used_codes"]:
            self.show_message("Code already used!")
            return
    
        # Check if code exists in predefined codes
        if redeem_code not in self.predefined_codes:
            self.show_message("Invalid redeem code!")
            return
    
        # Code is valid and new - process it
        code_data = self.predefined_codes[redeem_code]
        character = code_data["character"]
        points = code_data["points"]
        iq = code_data["iq"]
        power = code_data["power"]
    
        # Save to Firebase
        user_data["used_codes"][redeem_code] = {
            "character": character,
            "points": points,
            "iq": iq,
            "power": power
        }
        
        ref.child(email_key).update({
            "points": user_data.get("points", 0) + points,
            "used_codes": user_data["used_codes"]
        })
    
        self.update_points_label(user_data.get("points", 0) + points)
        self.show_message(f"Character: {character}\nPoints: {points}\nIQ: {iq}\nPower: {power}")
        
        # Refresh team screen
        if self.manager.has_screen("team"):
            self.manager.get_screen("team").on_enter()

    def show_message(self, message):
        
        """Display messages with proper formatting matching team screen cards"""
        # Clear existing card content
        self.result_card.clear_widgets()
    
        # Set card styling to match team screen exactly
        self.result_card.md_bg_color = (0.12, 0.12, 0.2, 1)
        self.result_card.radius = [25]
        self.result_card.elevation = 0
        self.result_card.size_hint = (0.9, None)
        self.result_card.padding = dp(5)
        self.result_card.spacing = dp(5)
    
        # Handle different message types
        if message == "Invalid redeem code!" or message == "Code already used!":
            # Simple error message format
            self.result_card.height = dp(100)
            error_label = MDLabel(
                text=message,
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                font_style="H6",
                bold=True
            )
            self.result_card.add_widget(error_label)
        else:
            # Parse character details
            lines = [line.strip() for line in message.split("\n") if line.strip()]
    
            # Initialize values
            full_character = ""
            points = ""
            iq = ""
            power = ""
    
            # Extract values from lines
            for line in lines:
                if line.startswith("Character:"):
                    full_character = line.replace("Character:", "").strip()
                elif line.startswith("Points:"):
                    points = line.replace("Points:", "").strip()
                elif line.startswith("IQ:"):
                    iq = line.replace("IQ:", "").strip()
                elif line.startswith("Power:"):
                    power = line.replace("Power:", "").strip()
    
            # Split character and movie name
            if '(' in full_character and ')' in full_character:
                character_name = full_character[:full_character.find("(")].strip()
                movie_name = full_character[full_character.find("(")+1:full_character.find(")")].strip()
            else:
                character_name = full_character
                movie_name = "Unknown Movie"
    
            # === CHARACTER NAME & MOVIE SECTION ===
            name_container = BoxLayout(
                orientation='vertical',
                size_hint=(1, None),
                height=dp(100),
                padding=[0, 0, 0, 5]
            )
    
            # Character name with highlight (UPPERCASE)
            name_label = MDLabel(
                text=character_name.upper(),
                halign="center",
                theme_text_color="Custom",
                text_color=(1, 1, 1.5, 1),
                font_style="H4",
                bold=True,
                size_hint_y=None,
                height=dp(70),
            )
    
            # Movie name in brackets
            movie_label = MDLabel(
                text=f"({movie_name})",
                halign="center",
                theme_text_color="Custom",
                text_color=(0.8, 0.8, 1, 1),
                font_style="H6",
                italic=True,
                size_hint_y=None,
                height=dp(25),
            )
    
            name_container.add_widget(name_label)
            name_container.add_widget(movie_label)
            self.result_card.add_widget(name_container)
    
            # === STATS DISPLAY ===
            stats_box = GridLayout(
                cols=1,
                spacing=dp(15),
                size_hint=(1, None),
                padding=[dp(20), dp(10), dp(20), dp(10)],
                height=dp(150)
            )
    
            def create_stat_row(icon, value, color, stat_name):
                row = BoxLayout(
                    orientation='horizontal',
                    spacing=dp(10),
                    size_hint=(1, None),
                    height=dp(40)
                )
    
                # Icon with consistent size
                icon_widget = MDIcon(
                    icon=icon,
                    size_hint=(None, None),
                    size=(dp(32), dp(32)),
                    theme_text_color="Custom",
                    text_color=color,
                    pos_hint={"center_y": 0.5}
                )
    
                # Stat name
                name_label = MDLabel(
                    text=stat_name,
                    theme_text_color="Custom",
                    text_color=(0.8, 0.8, 0.8, 1),
                    font_style="Subtitle1",
                    halign="left",
                    size_hint_x=0.5
                )
    
                # Value with emphasis
                value_label = MDLabel(
                    text=str(value),
                    theme_text_color="Custom",
                    text_color=color,
                    font_style="H5",
                    bold=True,
                    halign="right"
                )
    
                row.add_widget(icon_widget)
                row.add_widget(name_label)
                row.add_widget(value_label)
                return row
    
            # Add stats in order: IQ -> Power -> Points
            stats_box.add_widget(create_stat_row(
                "brain", iq, (0.2, 0.9, 0.9, 1), "IQ"
            ))
            stats_box.add_widget(create_stat_row(
                "arm-flex", power, (0.9, 0.2, 0.2, 1), "POWER"
            ))
            stats_box.add_widget(create_stat_row(
                "star", points, (1, 0.84, 0, 1), "POINTS"
            ))
    
            self.result_card.add_widget(stats_box)
    
            # Set card height
            self.result_card.height = dp(320)
    
        # Show the card with animation
        anim = Animation(opacity=1, d=0.5)
        anim.start(self.result_card)
        Clock.schedule_once(self.hide_message, 5)  # Hide after 5 seconds


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

        self.points_button = MDFillRoundFlatIconButton(
            text="0",  # Default points
            icon="star",  # You can change the icon
            pos_hint={"center_x": 0.8, "center_y": 0.95},
            size_hint=(None, None),
            md_bg_color=(227/255, 227/255, 227/255, 1),  # White color
            text_color=(0, 0, 0, 1), # Black color  
            icon_color=(1, 0.84, 0, 1),  # Gold color
            icon_size="30px",
            padding=dp(10),
        )
        self.add_widget(self.points_button)

        # Team Label with better styling
        self.team_label = MDLabel(
            text="YOUR TEAM",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.85},
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),
            font_style="H3",
            bold=True,
            underline=True,
        )
        self.add_widget(self.team_label)

        # Progress bar with better styling
        self.progress_bar = MDProgressBar(
            pos_hint={"center_x": 0.5, "center_y": 0.78},
            size_hint=(0.8, None),
            height="10dp",
            color=(90/255, 84/255, 255/255, 1),
            max=100,  # Percentage based
            value=0,  # Start at 0
        )
        self.add_widget(self.progress_bar)


        # Scrollable Grid Layout for Collected Cards
        self.scroll_view = ScrollView(
            size_hint=(1, 0.7), 
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            bar_width=dp(4),
            bar_color=(90/255, 84/255, 255/255, 1)
        )
        
        self.grid_layout = GridLayout(
            cols=2, 
            spacing=dp(15), 
            padding=dp(20),
            size_hint_y=None
        )
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

        self.team_button = MDIconButton(
            icon="cards",
            size_hint= (0.15,None), 
            pos_hint={"center_x": 0.5, "center_y": 0.065},
            md_bg_color=(90/255, 84/255, 255/255, 1),
            text_color=(1,1,1,1),
            theme_text_color='Custom',
        )
        self.add_widget(self.team_button)

    def create_character_card(self, character_data, points, iq, power):
        """Create a premium character card with movie name and single column layout"""
        # Split character and movie name if available
        if '(' in character_data and ')' in character_data:
            character, movie = character_data.split('(', 1)
            movie = movie.rstrip(')')
        else:
            character = character_data
            movie = "Unknown Movie"
        
        card = MDCard(
            size_hint=(0.9, None),  # 90% width for nice margins
            height="320dp",  # Increased height for more content
            orientation="vertical",
            padding=dp(5),
            spacing=dp(5),
            md_bg_color=(0.12, 0.12, 0.2, 1),
            elevation=0,
            radius=[25],
            ripple_behavior=True,
        )
    
        # === CHARACTER NAME & MOVIE SECTION ===
        name_container = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height="100dp",  # More space for name and movie
            padding=[0, 0, 0, 5]
        )
        
        # Character name with highlight
        name_label = MDLabel(
            text=character.strip().upper(),
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1.5, 1),  # Bright text
            font_style="H4",
            bold=True,
            size_hint_y=None,
            height="70dp",
        )
        
        # Movie name in brackets
        movie_label = MDLabel(
            text=f"({movie.strip()})",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.8, 0.8, 1, 1),  # Lighter color
            font_style="H6",
            italic=True,
            size_hint_y=None,
            height="25dp",
        )
        
        name_container.add_widget(name_label)
        name_container.add_widget(movie_label)
        card.add_widget(name_container)
    
        # === STATS DISPLAY ===
        stats_box = GridLayout(
            cols=1,
            spacing=dp(15),
            size_hint=(1, 1),
            padding=[20, 10, 20, 10]
        )
        
        def create_stat_row(icon, value, color, stat_name):
            row = BoxLayout(
                orientation='horizontal',
                spacing=dp(10),
                size_hint=(1, None),
                height="40dp"
            )
            
            # Icon with consistent size
            icon_widget = MDIcon(
                icon=icon,
                size_hint=(None, None),
                size=("32dp", "32dp"),
                theme_text_color="Custom",
                text_color=color,
                pos_hint={"center_y": 0.5}  # Center vertically
            )
            
            # Stat name
            name_label = MDLabel(
                text=stat_name,
                theme_text_color="Custom",
                text_color=(0.8, 0.8, 0.8, 1),
                font_style="Subtitle1",
                halign="left",
                size_hint_x=0.5
            )
            
            # Value with emphasis
            value_label = MDLabel(
                text=str(value),
                theme_text_color="Custom",
                text_color=color,
                font_style="H5",
                bold=True,
                halign="right"
            )
            
            row.add_widget(icon_widget)
            row.add_widget(name_label)
            row.add_widget(value_label)
            return row
        
        # Add stats in order: IQ -> Power -> Points
        stats_box.add_widget(create_stat_row(
            "brain", iq, (0.2, 0.9, 0.9, 1), "IQ"
        ))
        stats_box.add_widget(create_stat_row(
            "arm-flex", power, (0.9, 0.2, 0.2, 1), "POWER"
        ))
        stats_box.add_widget(create_stat_row(
            "star", points, (1, 0.84, 0, 1), "POINTS"
        ))
    
        card.add_widget(stats_box)
        
        return card
    
    def on_enter(self):
        """Load and display cards in single column"""
        self.grid_layout.clear_widgets()
        self.grid_layout.cols = 1  # Force single column layout

        if self.logged_in_email:
            email_key = self.logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if user_data:
                # Update points label
                points = user_data.get("points", 0)
                self.points_button.text = f"{points}"

                # Update progress bar
                max_points = 75000
                progress = min(points / max_points, 1.0)
                self.progress_bar.value = progress * 100

                if "used_codes" in user_data:
                    # Sort by points descending
                    sorted_codes = sorted(
                        user_data["used_codes"].items(),
                        key=lambda x: x[1].get("points", 0),
                        reverse=True
                    )

                    for code, details in sorted_codes:
                        card = self.create_character_card(
                            details.get("character", "Unknown"),
                            details.get("points", 0),
                            details.get("iq", 0),
                            details.get("power", 0)
                        )
                        self.grid_layout.add_widget(card)

                        # Fade-in animation
                        card.opacity = 0
                        Animation(opacity=1, duration=0.5).start(card)

    def load_logged_in_email(self):
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except (FileNotFoundError, KeyError):
            return None

    def refresh_data(self):
        """Refresh the team data from Firebase"""
        self.grid_layout.clear_widgets()
        self.on_enter()  # Call on_enter to reload data

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