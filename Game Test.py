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
import random
from kivy.uix.modalview import ModalView
from kivy.properties import StringProperty
from kivymd.uix.dialog import MDDialog
import time
import os
import datetime
from kivy.core.audio import SoundLoader



# Set mobile-friendly window size for testing
Window.size = (360, 640)  # Common mobile phone size

cred = credentials.Certificate({
  "type": "service_account",
  "project_id": "collect-62f2a",
  "private_key_id": "a02a38f949c3d289790ab5020b387c81d63a64ed",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCk7NDUs3UsejdL\nT28A2MxJFvd/vBjDRjGzhrejVw/PxMB19ujNUgSmWS+MD8OwyAfN0hHkhoCilmvX\npvjT6AemwijV0aC++2b70jwDawXDQIuug+YqsjYA3hf+6tzc47x94mI+sCxTk+wG\ncGgfo5ks3qLcwWPeF+9reXwbXZ20uVge2lvgOk4v4LcK0um6RsqZs9EncUet9+VA\nP7HKys+nVEyQzaONVddtKLq3ZbT+/coK3u8uY7Uyxf3OjWi9eMs7L575gozcZT4T\nlcc3oKxVMhdhZSu7qIWnqisU2DoWFM0n8A5KxoitR2boeDsnp46ZfNpft3Sk7gg3\n8JDZBxAlAgMBAAECggEABG/GcmJdfZPQFvuNDeXHIRQ4FjyWIfKqdZzjJca6yykM\n0F+TBar2Kw9tIwRtjDzlUNkc2BvyK+2F+ygnu3ObeRXyCUZ5X4ndzFpseN8RKZ57\n43by4yUmJMHUvWvOAzcxI+XKJMuSdbEeAVJWyrsY7McUdIHTUO8t5qM+/nF3Q5xJ\nvT1uNZWAoWK8QHwdgh/VKsVL/zybArsZQRTN11vFG1LKZgPqvpVn+87U/wUrAw2e\nEab1q8S4jitXC0RbDOzsKQPTLuFH8SDJwp799DKuzkBFsahO008BReqDdfi1mbd4\nlXT+WDl1y95FUnxGmQH+sOERUD8vtC06fgHPdn0z4QKBgQDVwWuzpE0TmT3u0qs0\n1p0lf8aoNf8mRDBUpHVekM3TzHPjRgO2cjftc3N420ioaHx1vyE6GBYxCOBxPAAZ\nG5hwsxKPvpWYQrAjPKPCdaGfDFnew34icVZQpEwQvpWBO8JJ6MOrwyP7I+/7WQOy\nHG3HIibJVFtFuo7/XWrKM97cuQKBgQDFhOdneDq9ACX06UEea4bl69QSpiQeUKSS\neFnyNGGwn8rQ2lpL/6ad2xibeVlOMHp8n8/PsxHKBjDhbjE0JbpxMW1UiWpLhSCT\nAvqlw8qhshvAGuzrbvAbnQcRswXxRsgWNOzQISWr+3bnBZEhCND7wkxPSuNg0GOV\nhmdcBQrQzQKBgEfPiCA8xUwdQko2aiABLaAIcjPWmBZB+D6nVWrkmNFbsV8cCWlE\nq/dQvu1ONfWlzJI+GKqMpv/oLIa+EoZc1/ScpFK4Q0d4t/XOjHFq1VY6bwLAiGKH\n0uiamZdSf6V/7wCnevz8PN1FMH0vZWdz14l7tq4ScetWBm5R8utlS6y5AoGATfo/\nJPEpN05krcCcbbcDpaeprMccgT9TCWQsFlupqYIcHsHlXhWKoM1LdK2+nQi0gpjR\nAO1v+3LgP08ya6TtaxyZTgOGDFR9XKyTaXfXemiHXhsDJ5s/fZdLoCguE2ffPC0e\nxLghWDlJYsEm34TMhGfbmn41MBZ1CiXqjkCLWY0CgYBervJs7xK/T43OCxhKoaIH\nhtflkBb8nvattT1OYi0ET7u04fP4HH7afLHlVO5cagzowts60TgyxFR/vJJQOYHc\nwL2+xNV/NBuVB3qMXi/rfM4MVWO4XnLjto2Rc8FzbvyP8oKdNzNhqp2u2aimcCQ5\nJirQoEqNVjjBbXCQvUh37w==\n-----END PRIVATE KEY-----\n",
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
        
        # Background
        with self.canvas.before:
            self.bg = Rectangle(source='bg.jpg', size=Window.size)
        
        # Result card for messages
        self.result_card = MDCard(
            size_hint=(0.9, None),
            height=dp(120),
            pos_hint={"center_x": 0.5, "center_y": 0.15},
            padding=dp(15),
            spacing=dp(10),
            orientation="vertical",
            md_bg_color=(0.1, 0.6, 0.6, 0.9),
            radius=[15],
            elevation=0,
            opacity=0,
        )
        self.card_label = MDLabel(
            text="",
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
            size_hint_y=None,
            height=dp(90),
        )
        self.result_card.add_widget(self.card_label)
        self.add_widget(self.result_card)

        # App title/logo
        self.title_label = MDLabel(
            text="MARVEL COLLECTOR",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.9},
            theme_text_color="Custom",
            text_color=(0.1, 0.6, 0.6, 0.9),
            font_style="H3",
            bold=True,
            size_hint_y=None,
            height=dp(50),
        )
        self.add_widget(self.title_label)

        # Email input
        self.email_input = MDTextField(
            hint_text="Enter your email",
            pos_hint={"center_x": 0.5, "center_y": 0.67},
            size_hint=(0.8, None),
            height=dp(50),
            font_size=dp(16),
            mode="rectangle",
            helper_text_mode="on_error",
        )
        self.add_widget(self.email_input)

        # Password input with eye toggle
        password_layout = BoxLayout(
            orientation="horizontal",
            size_hint=(0.8, None),
            height=dp(50),
            pos_hint={"center_x": 0.5, "center_y": 0.55},
            spacing=dp(10),
        )
        
        self.password_input = MDTextField(
            hint_text="Enter your password",
            password=True,
            size_hint=(0.85, 1),
            font_size=dp(16),
            mode="rectangle",
            max_text_length=20,
        )
        
        self.eye_icon_button = MDIconButton(
            icon="eye-off",
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
        )
        self.eye_icon_button.bind(on_release=self.toggle_password_visibility)
        
        password_layout.add_widget(self.password_input)
        password_layout.add_widget(self.eye_icon_button)
        self.add_widget(password_layout)

        # Login button
        self.login_button = MDRaisedButton(
            text="LOGIN",
            pos_hint={"center_x": 0.5, "center_y": 0.42},
            size_hint=(0.6, None),
            height=dp(50),
            font_size=dp(18),
            md_bg_color=(0.9, 0.1, 0.1, 1),  # Red color
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.login_button.bind(on_release=self.handle_login)
        self.add_widget(self.login_button)

        # Create account button
        self.create_account_button = MDRaisedButton(
            text="CREATE ACCOUNT",
            pos_hint={"center_x": 0.5, "center_y": 0.32},
            size_hint=(0.6, None),
            height=dp(50),
            font_size=dp(18),
            md_bg_color=(0.1, 0.5, 0.8, 1),  # Blue color
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
        )
        self.create_account_button.bind(on_release=self.handle_create_account)
        self.add_widget(self.create_account_button)

    def toggle_password_visibility(self, instance):
        """Toggle password visibility."""
        self.password_input.password = not self.password_input.password
        self.eye_icon_button.icon = "eye" if self.password_input.password else "eye-off"

    def handle_login(self, instance):
        """Handle login logic."""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if not email or not password:
            self.show_message("Please enter email and password!")
            return

        if not is_valid_email(email):
            self.show_message("Invalid email format!")
            return

        hashed_password = hash_password(password)
        ref = db.reference("users")
        user_data = ref.child(email.replace(".", ",")).get()

        if user_data and user_data.get("password") == hashed_password:
            self.save_logged_in_email(email)
            self.manager.current = "game"
            self.manager.transition.direction = 'left'
            self.clear_inputs()
        else:
            self.show_message("Invalid email or password!")

    def handle_create_account(self, instance):
        """Handle account creation logic."""
        email = self.email_input.text.strip()
        password = self.password_input.text.strip()

        if not email or not password:
            self.show_message("Please enter email and password!")
            return

        if not is_valid_email(email):
            self.show_message("Invalid email format!")
            return

        hashed_password = hash_password(password)
        ref = db.reference("users")
        email_key = email.replace(".", ",")

        if ref.child(email_key).get():
            self.show_message("Account already exists!")
        else:
            ref.child(email_key).set({
                "password": hashed_password,
                "user_name": "Not set",
                "user_age": "Not set",
                "user_id": "Not set",
                "points": 0,
                "used_codes": {},
                "level": 0  # ✅ NEW LINE
            })
            self.save_logged_in_email(email)
            self.manager.current = "game"
            self.manager.transition.direction = 'left'
            self.clear_inputs()

    def clear_inputs(self):
        """Clear all input fields."""
        self.email_input.text = ''
        self.password_input.text = ''
        self.eye_icon_button.icon = "eye-off"
        self.password_input.password = True
        self.result_card.opacity = 0

    def show_message(self, message):
        """Show a message in the result card."""
        self.card_label.text = message
        anim = Animation(opacity=1, d=0.3) + Animation(opacity=1, d=3) + Animation(opacity=0, d=0.3)
        anim.start(self.result_card)

    def save_logged_in_email(self, email):
        """Persist logged-in email."""
        with open("logged_in.json", "w") as file:
            json.dump({"email": email}, file)

    def load_logged_in_email(self):
        """Load the logged-in email from the file."""
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except (FileNotFoundError, KeyError):
            return None



class redeemCodeGame(Screen):

    predefined_codes = {
        # Level 1
        "Iron3000": {"character": "Iron Man\n (End Game)", "points": 3000, "iq": 1000, "power": 1000, "level": 1},
        "Cap": {"character": "Captain America\n (The Avenger)", "points": 1000, "iq": 140, "power": 70, "level": 1},
        "Thorlove": {"character": "Thor\n (Thor Love and Thunder)", "points": 1500, "iq": 175, "power": 95, "level": 1},
    
        # Level 2
        "Hulk": {"character": "Hulk\n (The Avenger)", "points": 2000, "iq": 185, "power": 100, "level": 2},
        "Widow": {"character": "Black Widow\n (Black Widow)", "points": 2000, "iq": 150, "power": 65, "level": 2},
        "CapMarvel": {"character": " Captain Marvel\n (The Captain Marvel)", "points": 1000, "iq": 160, "power": 90, "level": 2},
    
        # Level 3
        "Spidy": {"character": "Spiderman\n (Far From Home)", "points": 3000, "iq": 500, "power": 80, "level": 3},
        "Panther": {"character": "Black Panther\n (Black Panther)", "points": 2000, "iq": 200, "power": 75, "level": 3},
        "Strange": {"character": "Doctor Strange\n (Infinty War)", "points": 3000, "iq": 280, "power": 90, "level": 3},
    
        # Level 4
        "Wanda": {"character": "Scarlet Witch\n (Wanda Vision)", "points": 1000, "iq": 180, "power": 95, "level": 4},
        "Vision": {"character": "Vision\n (Age of Ultorn)", "points": 1000, "iq": 300, "power": 85, "level": 4},
        "Ant": {"character": "Antman\n (Antman)", "points": 1500, "iq": 160, "power": 60, "level": 4},
    
        # Level 5
        "Falcon": {"character": "Falcon\n (Civil War)", "points": 1500, "iq": 130, "power": 65, "level": 5},
        "Soldier": {"character": "Bucky\n (The Winter Soldier)", "points": 1500, "iq": 135, "power": 75, "level": 5},
        "Loki": {"character": "Loki\n (Loki)", "points": 10000, "iq": 250, "power": 999, "level": 5},
    
        # Level 6
        "Stark": {"character": "Tony Stark\n (The Avenger)", "points": 2000, "iq": 270, "power": 30, "level": 6},
        "Fury": {"character": "Nick Fury\n (The Avenger)", "points": 300, "iq": 160, "power": 40, "level": 6},
        "Hawk": {"character": "Hawkeye\n (The Avenger)", "points": 500, "iq": 140, "power": 50, "level": 6},
    
        # Level 7
        "Villain": {"character": "Thanos\n (Infinity War)", "points": 10000, "iq": 240, "power": 100, "level": 7},
        "Ultron": {"character": "Ultron\n (Age of Ultron)", "points": 1000, "iq": 260, "power": 90, "level": 7},
        "Red": {"character": "Red Skull\n (Captain America)", "points": 1000, "iq": 180, "power": 70, "level": 7},
    
        # Level 8
        "Hela": {"character": "Hela\n (Thor Ragnarok)", "points": 2000, "iq": 190, "power": 95, "level": 8},
        "Kill": {"character": "Killmonger\n (Black Panther)", "points": 1500, "iq": 170, "power": 75, "level": 8},
        "No Death": {"character": "Deadpool\n (Deadpool and Wolverine)", "points": 9000, "iq": 130, "power": 85, "level": 8},
    
        # Level 9
        "Wolverine": {"character": "Wolverine\n (Deadpool and Wolverine)", "points": 6000, "iq": 125, "power": 90, "level": 9},
        "she": {"character": "She-Hulk\n (She-Hulk)", "points": 100, "iq": 150, "power": 85, "level": 9},
        "Venom3": {"character": "Venom\n (Venom The Last Dance)", "points": 2000, "iq": 120, "power": 80, "level": 9},
    
        # Level 10
        "Groot": {"character": "Groot\n (Guardians of the Galaxy)", "points": 500, "iq": 90, "power": 70, "level": 10},
        "Rocket": {"character": "Rocket\n (Guardians of the Galaxy)", "points": 1500, "iq": 220, "power": 60, "level": 10},
        "Gamora": {"character": "Gamora\n (Guardians of the Galaxy)", "points": 500, "iq": 150, "power": 75, "level": 10},
        "Star": {"character": "Star Lord\n (Guardians of the Galaxy)", "points": 1500, "iq": 140, "power": 65, "level": 10},
        "Drax": {"character": "Drax\n (Guardians of the Galaxy)", "points": 100, "iq": 0, "power": 85, "level": 10},
        "Mantis": {"character": "Mantis\n (Guardians of the Galaxy)", "points": 400, "iq": 110, "power": 60, "level": 10},
        "Nebula": {"character": "Nebula\n (Guardians of the Galaxy)", "points": 100, "iq": 150, "power": 75, "level": 10},
        "Marvel's Flash": {"character": "Makkari\n (Eternals)", "points": 2000, "iq": 160, "power": 80, "level": 10}
    }


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data_file = "user_data.json"
        self.logged_in_email = None
        self.load_user_data()


        self.level_names = {
            0: "New Guy",
            1: "Beginner",
            2: "Trainee",
            3: "Recruit",
            4: "Fighter",
            5: "Hero",
            6: "Elite",
            7: "Avenger",
            8: "Legend",
            9: "Warrior",
            10: "Master"
        }

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


        self.result_card = MDCard(
            size_hint=(1, None),
            height=dp(380),
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            padding=dp(15),
            spacing=dp(10),
            orientation="vertical",
            ripple_behavior=True,
            md_bg_color=(0.12, 0.12, 0.2, 0.95),
            radius=[20],
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

        self.result_card.add_widget(self.card_label)
        self.add_widget(self.result_card)


        # Bottom navigation bar
        self.nav_bar = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "y": 0},
            spacing=dp(50),
            padding=dp(5),
        )

        # Redeem button
        self.redeem_nav_button = MDIconButton(
            icon="gift-outline",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),  # purple
            icon_size=dp(30),
        )
        
        # Team button
        self.team_nav_button = MDIconButton(
            icon="cards",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.team_nav_button.bind(on_release=self.go_team)

        self.trade_nav_button = MDIconButton(
            icon="swap-horizontal-bold",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.trade_nav_button.bind(on_release=self.go_trade)
        
        # Account button (active)
        self.account_nav_button = MDIconButton(
            icon="account-circle",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.account_nav_button.bind(on_release=self.go_account)

        self.nav_bar.add_widget(self.redeem_nav_button)
        self.nav_bar.add_widget(self.team_nav_button)
        self.nav_bar.add_widget(self.trade_nav_button)
        self.nav_bar.add_widget(self.account_nav_button)
        self.add_widget(self.nav_bar)




    def on_enter(self):
        """Load logged-in user email and update points."""
        login_screen = self.manager.get_screen("login")
        self.logged_in_email = login_screen.load_logged_in_email()


        # Points display
        self.points_button = MDFillRoundFlatIconButton(
            text="0",
            icon="star",
            pos_hint={"center_x": 0.25, "center_y": 0.94},
            size_hint=(0.4, 0.07),
            height=dp(45),
            text_color=(0, 0, 0, 1),
            icon_color=(1, 0.84, 0, 1),  # Gold
            font_size=dp(18),
            md_bg_color=(1, 246/255, 229/255, 1),
            line_color=(248/255, 226/255, 184/255, 1),
            line_width=dp(1),
        )
        self.add_widget(self.points_button)


        # Level button
        self.level_button = MDFillRoundFlatIconButton(
            text="",
            icon="",
            pos_hint={"center_x": 0.75, "center_y": 0.94},
            size_hint=(0.4, 0.07),
            height=dp(45),
            md_bg_color=(1, 246/255, 229/255, 1),
            text_color=(0, 0, 0, 1),  # Gold
            font_size=dp(18),
            icon_size=dp(30),
            halign="center",
            valign="center",
            line_color=(248/255, 226/255, 184/255, 1),
            line_width=dp(1),
        )
        self.level_button.bind(on_release=self.go_level)
        self.add_widget(self.level_button)

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
        
        # Update level button
        current_level = user_data.get("level", 0)
        self.level_button.icon = f"level_{current_level}.png" if current_level > 0 else ""
        self.level_button.text = f"    LEVEL {current_level}" if current_level > 0 else "    LEVEL 0"

        




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

        email_key = self.logged_in_email.replace(".", ",")
        ref = db.reference("users")
        user_data = ref.child(email_key).get()

        user_level = user_data.get("level", 0)
        card_data = self.predefined_codes.get(redeem_code, {})
        card_level = card_data.get("level", 0)

        
        if not self.logged_in_email:
            self.show_message("No user logged in!")
            self.color_message(1, 0, 0, 1)  # Red color
            return
    
        email_key = self.logged_in_email.replace(".", ",")
        ref = db.reference("users")
        user_data = ref.child(email_key).get()
    
        if not user_data:
            self.show_message("User data not found!")
            self.color_message(1, 0, 0, 1)
            return
        

        if card_level > user_level + 1 :
            # Show a message telling the user that the card is for a higher level
            self.show_message(f"Reach Level {card_level} to unlock this card!")
            self.result_card.md_bg_color = (1, 0.5, 0, 1)  # Orange
            self.card_label.text = f"Level {card_level} Card"
            self.card_label.font_style = "H6"
            return


    
        if "used_codes" not in user_data:
            user_data["used_codes"] = {}
    
        # Check if code already used
        if redeem_code in user_data["used_codes"]:
            self.show_message("Code already used!")
            self.color_message(5/255, 224/255, 91/255, 1)
            return
    
        # Check if code exists in predefined codes
        if redeem_code not in self.predefined_codes:
            self.show_message("Invalid redeem code!")
            self.color_message(1, 0, 0, 1)
            return
        

        # Decide what to show based on card level vs user level
   
        # Code is valid and new - process it
        code_data = self.predefined_codes[redeem_code]
        character = code_data["character"]
        points = code_data["points"]
        iq = code_data["iq"]
        power = code_data["power"]
        level = card_data.get("level", 1)

    

        if card_level == user_level + 1:
            # Save to Firebase
            user_data["used_codes"][redeem_code] = {
                "character": character,
                "points": points,
                "iq": iq,
                "power": power,
                "level": level
            }

            ref.child(email_key).update({
                "points": user_data.get("points", 0) + points,
                "used_codes": user_data["used_codes"]
            })

            self.update_points_label(user_data.get("points", 0) + points)
            self.show_message(f"Character: {character}\nPoints: {points}\nIQ: {iq}\nPower: {power}\nLevel: {level}")
        
            # Refresh team screen
            if self.manager.has_screen("team"):
                self.manager.get_screen("team").on_enter()

            self.check_level_completion(user_data)


    def show_message(self, message):
        """Display messages with proper formatting matching team screen cards"""
        # Clear existing card content
        redeem_code = self.redeem_code_input.text.strip()
        card_data = self.predefined_codes.get(redeem_code, {})
        card_level = card_data.get("level", 1)
        self.result_card.clear_widgets()
    
        # Set card styling to match team screen exactly
        self.result_card.md_bg_color = (0.12, 0.12, 0.2, 0.95)
        self.result_card.radius = [20]
        self.result_card.elevation = 0
        self.result_card.size_hint = (0.9, None)
        self.result_card.padding = dp(10)
        self.result_card.spacing = dp(10)
    
        # Handle different message types
        if message == "Invalid redeem code!" or message == "Code already used!" or message == "No user logged in!" or message == "User data not found!" or message == f"Reach Level {card_level} to unlock this card!":
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
            level = ""
    
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
                elif line.startswith("Level:"):
                    level = line.replace("Level:", "").strip()
    
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
                height=dp(200)
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
            stats_box.add_widget(create_stat_row(
                "shield-account", level, (0.2, 0.9, 0.2, 1), "LEVEL"
            ))
    
            self.result_card.add_widget(stats_box)
    
            # Set card height
            self.result_card.height = dp(320)
    
        # Show the card with animation
        anim = Animation(opacity=1, d=0.3) + Animation(opacity=1, d=5) + Animation(opacity=0, d=0.3)
        anim.start(self.result_card)

    def color_message(self, r, g, b, a):
        """Set the color of the message text."""
        self.result_card.md_bg_color = (r, g, b, a)


    def go_account(self, instance):
        self.manager.current="account"
        self.manager.transition.direction = 'left'

    def go_team(self, instance):
        team_screen = self.manager.get_screen("team")
        team_screen.on_enter()  # Force refresh
        self.manager.current = "team"
        self.manager.transition.direction = 'left'

    def go_trade(self, instance):
        self.manager.current = "trade"
        self.manager.transition.direction = "left"

    def on_leave(self, *args):
        """Clear the redeem code input when leaving the screen."""
        self.redeem_code_input.text = ''
        self.result_card.opacity = 0


    def check_level_completion(self, user_data):
        current_level = user_data.get("level", 0)
        used_codes = user_data.get("used_codes", {})

        # Get all codes of the current level
        current_level_codes = [
            code for code, data in self.predefined_codes.items()
            if data.get("level") == current_level + 1
        ]

        collected = [code for code in current_level_codes if code in used_codes]

        if len(collected) == len(current_level_codes) and current_level < 10:
            new_level = current_level + 1
            email_key = self.logged_in_email.replace(".", ",")
            db.reference("users").child(email_key).update({"level": new_level})

            # Optionally update level display on account screen
            self.level_button.text = f"    Level {new_level}"
            self.level_button.icon = f"level_{new_level}.png"


    def go_level(self, instance):
        self.manager.current = "level"
        self.manager.transition.direction = 'left'




class levelscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user_data_file = "user_data.json"
        self.logged_in_email = None
        self.load_user_data()

        # If you want a colored background, use Kivy graphics instructions in Python like this:
        # with self.canvas.before:
        #     Color(0, 0, 0, 1)
        #     self.bg_rect = Rectangle(size=self.size, pos=self.pos)
        # self.bind(size=lambda instance, value: setattr(self.bg_rect, 'size', value))
        # self.bind(pos=lambda instance, value: setattr(self.bg_rect, 'pos', value))


        self.level_names = {
            0: "New Guy",
            1: "Beginner",
            2: "Trainee",
            3: "Recruit",
            4: "Fighter",
            5: "Hero",
            6: "Elite",
            7: "Avenger",
            8: "Legend",
            9: "Warrior",
            10: "Master"
        }

        self.temp_back= MDIconButton(
            icon="arrow-left",
            pos_hint={"center_x": 0.05, "center_y": 0.95},
            size_hint=(None, None),
            size=("40dp", "40dp"),
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            icon_size=dp(30),
        )
        self.temp_back.bind(on_release=self.go_temp_back)
        self.add_widget(self.temp_back)

        # Container to hold stage and level image together
        self.stage_container = RelativeLayout(
            size_hint=(1, None),
            height=Window.height * 0.3,
            pos_hint={"center_x": 0.5, "center_y": 0.75},
        )

        # Stage image at bottom
        self.stage_img = Image(
            source="stage.png",
            allow_stretch=True,
            keep_ratio=False,
            size_hint=(1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.stage_container.add_widget(self.stage_img)


        # Add combined layout to screen
        self.add_widget(self.stage_container)



    def on_enter(self):
        login_screen = self.manager.get_screen("login")
        email = login_screen.load_logged_in_email()
        if email:
            email_key = email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()
            if user_data:
                self.stage_update(user_data)


    #Update the stage image and level label based on the current level.
    def stage_update(self, user_data):
        # Level image on top of stage
        self.cur_level = Image(
            source="",
            size_hint=(None, None),
            size=("220dp", "60dp"),
            allow_stretch=True,
            pos_hint={"center_x": 0.5, "center_y": 0.65},  # Adjust as needed
        )
        self.stage_container.add_widget(self.cur_level)

        self.level_label = MDLabel(
            text="",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.4},
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
            bold=True,
            size_hint_y=None,
            height=dp(40),
            font_size=dp(24),
        )
        self.stage_container.add_widget(self.level_label)

        self.pre_level = Image(
            source="",
            color=(0.45, 0.45, 0.45, 1),  # Greyed out
            size_hint=(None, None),
            size=("220dp", "50dp"),
            allow_stretch=True,
            pos_hint={"center_x": 0.2, "center_y": 0.55},
        )
        self.stage_container.add_widget(self.pre_level)


        self.next_level = Image(
            source="",
            color=(0, 0, 0, 1),  # Greyed out
            size_hint=(None, None),
            size=("220dp", "50dp"),
            allow_stretch=True,
            pos_hint={"center_x": 0.8, "center_y": 0.55},
        )
        self.stage_container.add_widget(self.next_level)
        current_level = user_data.get("level", 0)
        self.cur_level.source = f"level_{current_level}.png" if current_level > 0 else ""
    
        # Previous level image

        if current_level == 0:
            self.pre_level.source = ""
            self.pre_level.opacity = 0
            self.level_label.text = self.level_names.get(current_level, "Unknown Level")
            self.cur_level.opacity = 0

        if current_level > 0 and current_level > 1:
            self.pre_level.source = f"level_{current_level - 1}.png"
            self.level_label.text = self.level_names.get(current_level, "Unknown Level")
        else:
            self.pre_level.source = ""
            self.pre_level.opacity = 0
            self.level_label.text = f"LEVEL {current_level} - {self.level_names.get(current_level, 'Unknown Level')}"
            
    
        # Next level image
        if current_level < 10:
            self.next_level.source = f"level_{current_level + 1}.png"
            self.level_label.text = self.level_names.get(current_level, "Unknown Level")
        else:
            self.next_level.source = ""
            self.next_level.opacity = 0
            self.level_label.text = self.level_names.get(current_level, "Unknown Level")

    
    def load_user_data(self):
        try:
            with open(self.user_data_file, "r") as file:
                self.user_data = json.load(file)
        except FileNotFoundError:
            self.user_data = {}

    def go_temp_back(self, instance):
        self.manager.current = 'game'
        self.manager.transition.direction = 'right'



        


class teamscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_in_email = None
        
        
        # Points display
        self.points_button = MDFillRoundFlatIconButton(
            text="0",
            icon="star",
            pos_hint={"center_x": 0.5, "center_y": 0.95},
            size_hint=(0.5, None),
            height=dp(45),
            md_bg_color=(0.1, 0.1, 0.2, 0.8),
            text_color=(1, 0.84, 0, 1),  # Gold
            icon_color=(1, 0.84, 0, 1),  # Gold
            font_size=dp(18),
        )
        self.add_widget(self.points_button)

        # Team title
        self.team_label = MDLabel(
            text="YOUR TEAM",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.88},
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),  # Purple
            font_style="H4",
            bold=True,
            size_hint_y=None,
            height=dp(40),
        )
        self.add_widget(self.team_label)

        # Progress bar
        self.progress_bar = MDProgressBar(
            pos_hint={"center_x": 0.5, "center_y": 0.84},
            size_hint=(0.8, None),
            height=dp(10),
            color=(90/255, 84/255, 255/255, 1),  # Purple
            max=100,
            value=0,
        )
        self.add_widget(self.progress_bar)

        # Scrollable card grid
        self.scroll_view = ScrollView(
            size_hint=(1, 0.7),
            pos_hint={"center_x": 0.5, "center_y": 0.45},
            bar_width=dp(6),
            bar_color=(90/255, 84/255, 255/255, 0.5),
            scroll_type=['bars', 'content'],
            bar_inactive_color=(90/255, 84/255, 255/255, 0.2),
        )
        
        self.grid_layout = GridLayout(
            cols=1,
            spacing=dp(15),
            padding=dp(20),
            size_hint_y=None,
        )
        self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
        self.scroll_view.add_widget(self.grid_layout)
        self.add_widget(self.scroll_view)

        # Empty state message
        self.empty_label = MDLabel(
            text="No characters collected yet!\nRedeem codes to build your team",
            halign="center",
            theme_text_color="Hint",
            font_style="H6",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        self.add_widget(self.empty_label)

        # Bottom navigation bar
        self.nav_bar = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "y": 0},
            spacing=dp(60),
            padding=dp(5),
        )

        # Redeem button
        self.redeem_nav_button = MDIconButton(
            icon="gift-outline",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.redeem_nav_button.bind(on_release=self.go_redeem)
        
        # Team button (active)
        self.team_nav_button = MDIconButton(
            icon="cards",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),  # Purple
            icon_size=dp(30),
        )
        
        self.trade_nav_button = MDIconButton(
            icon="swap-horizontal-bold",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.trade_nav_button.bind(on_release=self.go_trade)

        # Account button
        self.account_nav_button = MDIconButton(
            icon="account-circle",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.account_nav_button.bind(on_release=self.go_account)

        self.nav_bar.add_widget(self.redeem_nav_button)
        self.nav_bar.add_widget(self.team_nav_button)
        self.nav_bar.add_widget(self.trade_nav_button)
        self.nav_bar.add_widget(self.account_nav_button)
        self.add_widget(self.nav_bar)

    def on_enter(self):
        """Load team data when screen is entered"""
        self.grid_layout.clear_widgets()
        login_screen = self.manager.get_screen("login")
        self.logged_in_email = login_screen.load_logged_in_email()

        if not self.logged_in_email:
            self.empty_label.text = "Please login to view your team"
            return

        email_key = self.logged_in_email.replace(".", ",")
        ref = db.reference("users")
        user_data = ref.child(email_key).get()

        if user_data:
            # Update points and progress
            points = user_data.get("points", 0)
            self.points_button.text = str(points)
            
            # Calculate progress (max points 75,000 for 100%)
            progress = min(points / 75000, 1.0) * 100
            self.progress_bar.value = progress

            if "used_codes" in user_data:
                # Show collection stats
                collection_size = len(user_data["used_codes"])                
                # Hide empty state if we have cards
                if collection_size > 0:
                    self.empty_label.text = ""
                
                # Sort cards by points (highest level first)
                sorted_cards = sorted(
                    user_data["used_codes"].items(),
                    key=lambda x: x[1].get("level", 1),
                    reverse=True
                )



                # Store cards for lazy loading
                self.sorted_cards_to_load = sorted_cards
                self.card_index = 0
                Clock.schedule_interval(self.load_next_card, 0.05)  # Load cards every 20 FPS

            else:
                self.empty_label.text = "No characters collected yet!\nRedeem codes to build your team"
        else:
            self.empty_label.text = "User data not found"


    def load_next_card(self, dt):
        if self.card_index >= len(self.sorted_cards_to_load):
            return False  # Stop scheduling once all cards are loaded

        code, card = self.sorted_cards_to_load[self.card_index]
        self.add_character_card(
            card.get("character", "Unknown"),
            card.get("points", 0),
            card.get("iq", 0),
            card.get("power", 0),
            card.get("level", 1)
        )
        self.card_index += 1
        return True  # Continue scheduling


    def add_character_card(self, character, points, iq, power, level):
        """Create and add a character card to the grid"""
        # Parse character and movie name
        if '(' in character and ')' in character:
            char_name, movie = character.split('(', 1)
            movie = movie.rstrip(')').strip()
        else:
            char_name = character
            movie = "Unknown Movie"

        # Create card
        card = MDCard(
            size_hint=(1, None),
            height=dp(330),
            orientation="vertical",
            padding=dp(10),
            spacing=dp(10),
            md_bg_color=(0.12, 0.12, 0.2, 0.95),
            radius=[20],
            elevation=0,
        )

        # Character name section
        name_box = BoxLayout(
            orientation='vertical',
            size_hint=(1, None),
            height=dp(80),
            spacing=dp(5),
        )
        
        char_label = MDLabel(
            text=char_name.strip().upper(),
            halign="center",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H5",
            bold=True,
        )
        
        movie_label = MDLabel(
            text=f"({movie})",
            halign="center",
            theme_text_color="Custom",
            text_color=(0.7, 0.7, 1, 1),
            font_style="Subtitle1",
            italic=True,
        )
        
        name_box.add_widget(char_label)
        name_box.add_widget(movie_label)
        card.add_widget(name_box)

        # Stats section
        stats_box = GridLayout(
            cols=1,
            spacing=dp(10),
            size_hint=(1, None),
            height=dp(200),
            padding=dp(15),
        )

        def create_stat_row(icon, value, color, label):
            row = BoxLayout(
                orientation='horizontal',
                size_hint=(1, None),
                height=dp(40),
            )
            
            icon_widget = MDIcon(
                icon=icon,
                theme_text_color="Custom",
                text_color=color,
                size_hint=(None, None),
                size=(dp(32), dp(32)),
                pos_hint={'center_y': 0.5},
            )
            
            text_label = MDLabel(
                text=label,
                theme_text_color="Custom",
                text_color=(0.8, 0.8, 0.8, 1),
                halign="left",
                size_hint_x=0.6,
            )
            
            value_label = MDLabel(
                text=str(value),
                theme_text_color="Custom",
                text_color=color,
                font_style="H5",
                bold=True,
                halign="right",
            )
            
            row.add_widget(icon_widget)
            row.add_widget(text_label)
            row.add_widget(value_label)
            return row

        # Add stats rows
        stats_box.add_widget(create_stat_row(
            "brain", iq, (0.2, 0.9, 0.9, 1), "IQ"
        ))
        stats_box.add_widget(create_stat_row(
            "arm-flex", power, (0.9, 0.2, 0.2, 1), "POWER"
        ))
        stats_box.add_widget(create_stat_row(
            "star", points, (1, 0.84, 0, 1), "POINTS"
        ))
        stats_box.add_widget(create_stat_row(
            "shield-account", level, (0.2, 0.9, 0.2, 1), "LEVEL"
        ))  
        
        card.add_widget(stats_box)
        
        # Add to grid with animation
        self.grid_layout.add_widget(card)
        card.opacity = 0
        card.opacity = 1  # Instant display, no animation


    def go_account(self, instance):
        """Navigate to account screen"""
        self.manager.current = "account"
        self.manager.transition.direction = 'left'

    def go_redeem(self, instance):
        """Navigate to redeem screen"""
        self.manager.current = "game"
        self.manager.transition.direction = 'right'

    def go_trade(self, instance):
        self.manager.current = "trade"
        self.manager.transition.direction = "left"




class accountscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_in_email = self.load_logged_in_email()
        self.user_data_file = "user_data.json"


        self.account_icon = MDIconButton(
            icon="account-circle",
            size_hint=(None, None),
            icon_size=dp(80),
            pos_hint={"center_x": 0.5, "center_y": 0.82},
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
        self.edit_button.bind(on_release=self.go_edit)
        self.add_widget(self.edit_button)

        self.logout_button = MDFlatButton(
            text="Logout",
            pos_hint={"center_x": 0.1, "center_y": 0.25},
            theme_text_color='Custom',
            text_color='red'
        )
        self.logout_button.bind(on_release=self.handle_logout)
        self.add_widget(self.logout_button)

        # Bottom navigation bar
        self.nav_bar = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "y": 0},
            spacing=dp(50),
            padding=dp(5),
        )

        # Redeem button
        self.redeem_nav_button = MDIconButton(
            icon="gift-outline",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.redeem_nav_button.bind(on_release=self.go_redeem)
        
        # Team button
        self.team_nav_button = MDIconButton(
            icon="cards",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.team_nav_button.bind(on_release=self.go_team)

        self.trade_nav_button = MDIconButton(
            icon="swap-horizontal-bold",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.trade_nav_button.bind(on_release=self.go_trade)
        
        # Account button (active)
        self.account_nav_button = MDIconButton(
            icon="account-circle",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),  # purple
            icon_size=dp(30),
        )

        self.nav_bar.add_widget(self.redeem_nav_button)
        self.nav_bar.add_widget(self.team_nav_button)
        self.nav_bar.add_widget(self.trade_nav_button)
        self.nav_bar.add_widget(self.account_nav_button)
        self.add_widget(self.nav_bar)


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

    def on_enter(self):
        """Load user data when the account screen is entered."""
        login_screen = self.manager.get_screen("login")
        self.logged_in_email = login_screen.load_logged_in_email()

        if self.logged_in_email:
            email_key = self.logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if not user_data:
                self.show_message("User data not found.")
                return  # Exit early to avoid crash

            self.update_email_label(self.logged_in_email)

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



    def go_edit(self, instance):
        self.manager.current = "edit"
        self.manager.transition.direction = 'left'

    def go_team(self, instance):
        """Navigate to team screen"""
        team_screen = self.manager.get_screen("team")
        team_screen.on_enter()  # Refresh data
        self.manager.current = "team"
        self.manager.transition.direction = 'right'

    def go_redeem(self, instance):
        self.manager.current = "game"
        self.manager.transition.direction = 'right'

    def go_trade(self, instance):
        self.manager.current = "trade"
        self.manager.transition.direction = "left"


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
            md_bg_color=(0.1, 0.6, 0.6, 0.9),
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

    def on_enter(self):
        """Load user data when the edit screen is entered."""
        login_screen = self.manager.get_screen("login")
        logged_in_email = login_screen.load_logged_in_email()

        if logged_in_email:
            email_key = logged_in_email.replace(".", ",")
            ref = db.reference("users")
            user_data = ref.child(email_key).get()

            if user_data:
                username = user_data.get("user_name", "Not set")
                age = user_data.get("user_age", "Not set")
                user_id = user_data.get("user_id", "Not set")

                self.user_name_input.text = username
                self.age.text = str(age)
                self.user_id_input.text = user_id
            else:
                self.show_message("User data not found.")
        else:
            self.show_message("No user logged in!")

        
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
        
        if age < 0 or age > 120:
            self.show_message("Please enter a valid age!")
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

            self.show_message("Details saved successfully!")
            self.color_message(5/255, 224/255, 91/255, 1)
            self.manager.current = "account"
            self.manager.transition.direction = 'right'
        else:
            self.show_message("No user logged in!")


    def show_message(self, message):
        self.message_label.text = message
        anim = Animation(opacity=1, d=0.5)
        anim.start(self.message_card)

        Clock.schedule_once(self.hide_message, 3)

    def color_message(self, r, g, b, a):
        """Change the color of the message card."""
        self.message_card.md_bg_color = (r, g, b, a)

    def hide_message(self, *args):
        """Hide the result card."""
        anim = Animation(opacity=0, d=0.5)
        anim.start(self.message_card)

    def to_account(self, instance):
        self.manager.current="account"
        self.manager.transition.direction = 'right'


class tradingscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_in_email = None
        self.selected_card = None
        self.trade_check_clock = None
        self.trade_sound = SoundLoader.load('notify.wav')
        self.last_trade_count = 0
        # Add selected card style attributes
        self.selected_btn = None  # To track currently selected button
        self.normal_color = (0.2, 0.2, 0.3, 1)  # Default card color
        self.selected_color = (0.3, 0.3, 0.5, 1)  # Selected card color
        
        
        # Title
        self.title = MDLabel(
            text="CARD TRADING",
            halign="center",
            font_style="H4",
            pos_hint={"center_x": 0.5, "center_y": 0.95},
            theme_text_color="Custom",
            text_color=(1, 0.84, 0, 1),  # Gold
            size_hint_y=None,
            height=dp(40),
        )
        self.add_widget(self.title)

        # Trade partner input
        self.receiver_input = MDTextField(
            hint_text="Enter friend's email",
            pos_hint={"center_x": 0.5, "center_y": 0.88},
            size_hint=(0.8, None),
            height=dp(50),
            font_size=dp(16),
            mode="rectangle",
        )
        self.add_widget(self.receiver_input)

        # Send trade button
        self.send_button = MDRaisedButton(
            text="SEND CARD",
            pos_hint={"center_x": 0.5, "center_y": 0.79},
            size_hint=(0.7, None),
            height=dp(50),
            md_bg_color=(0.2, 0.7, 0.3, 1),  # Green
            font_size=dp(18),
        )
        self.send_button.bind(on_release=self.send_trade)
        self.add_widget(self.send_button)

        # Status message
        self.status_label = MDLabel(
            text="Select a card to trade",
            halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.72},
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),  # Grey
            font_style="Subtitle1",
            size_hint_y=None,
            height=dp(30),
        )
        self.add_widget(self.status_label)

        # Your Cards Section
        self.cards_label = MDLabel(
            text="YOUR CARDS:",
            halign="left",
            pos_hint={"x": 0.1, "center_y": 0.67},
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height=dp(30),
        )
        self.add_widget(self.cards_label)

        # Cards ScrollView
        self.cards_scroll = ScrollView(
            size_hint=(0.9, 0.25),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            bar_width=dp(4),
            bar_color=(0.5, 0.5, 0.8, 0.5),
        )
        
        self.cards_grid = GridLayout(
            cols=1,
            spacing=dp(10),
            size_hint_y=None,
            padding=dp(10),
        )
        self.cards_grid.bind(minimum_height=self.cards_grid.setter('height'))
        self.cards_scroll.add_widget(self.cards_grid)
        self.add_widget(self.cards_scroll)

        # Incoming CARDS Section
        self.incoming_label = MDLabel(
            text="INCOMING CARDS:",
            halign="left",
            pos_hint={"x": 0.1, "center_y": 0.3},
            theme_text_color="Primary",
            font_style="H6",
            size_hint_y=None,
            height=dp(30),
        )
        self.add_widget(self.incoming_label)

        # Incoming CARDS ScrollView
        self.incoming_scroll = ScrollView(
            size_hint=(0.9, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.18},
            bar_width=dp(4),
            bar_color=(0.5, 0.5, 0.8, 0.5),
        )
        
        self.incoming_grid = GridLayout(
            cols=1,
            spacing=dp(10),
            size_hint_y=None,
            padding=dp(10),
        )
        self.incoming_grid.bind(minimum_height=self.incoming_grid.setter('height'))
        self.incoming_scroll.add_widget(self.incoming_grid)
        self.add_widget(self.incoming_scroll)

        # Bottom navigation bar
        self.nav_bar = BoxLayout(
            size_hint=(1, None),
            height=dp(60),
            pos_hint={"center_x": 0.5, "y": 0},
            spacing=dp(50),
            padding=dp(5),
        )

        # Redeem button
        self.redeem_nav_button = MDIconButton(
            icon="gift-outline",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.redeem_nav_button.bind(on_release=self.go_redeem)
        
        # Team button
        self.team_nav_button = MDIconButton(
            icon="cards",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.team_nav_button.bind(on_release=self.go_team)

        self.trade_nav_button = MDIconButton(
            icon="swap-horizontal-bold",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(90/255, 84/255, 255/255, 1),  # purple
            icon_size=dp(30),
        )
        
        # Account button (active)
        self.account_nav_button = MDIconButton(
            icon="account-circle",
            size_hint=(0.33, 1),
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 0.5, 1),
            icon_size=dp(30),
        )
        self.account_nav_button.bind(on_release=self.go_account)

        self.nav_bar.add_widget(self.redeem_nav_button)
        self.nav_bar.add_widget(self.team_nav_button)
        self.nav_bar.add_widget(self.trade_nav_button)
        self.nav_bar.add_widget(self.account_nav_button)
        self.add_widget(self.nav_bar)


        # History button
        self.history_button = MDIconButton(
            icon="history",
            pos_hint={"center_x": 0.8, "center_y": 0.3},
            size_hint=(0.15, 0.06),
            height=dp(45),
            md_bg_color=(0.5, 0.3, 0.7, 1),  # Purple
            font_size=dp(16),
        )
        self.history_button.bind(on_release=self.go_history)
        self.add_widget(self.history_button)


    def on_enter(self):
        """Called when screen is displayed"""
        self.logged_in_email = self.load_logged_in_email()
        self.load_user_cards()
        self.load_incoming_trades()
        self.start_trade_check_timer()

    def on_leave(self):
        """Called when screen is hidden"""
        self.stop_trade_check_timer()
        self.receiver_input.text = ""
        self.status_label.text = "Select a card to trade"
        self.status_label.text_color = (0.5, 0.5, 0.5, 1)  # Grey

    def start_trade_check_timer(self):
        """Start checking for new CARDS"""
        self.stop_trade_check_timer()
        self.trade_check_clock = Clock.schedule_interval(
            lambda dt: self.load_incoming_trades(),
            5  # Check every 5 seconds
        )

    def stop_trade_check_timer(self):
        """Stop checking for new CARDS"""
        if self.trade_check_clock:
            self.trade_check_clock.cancel()
            self.trade_check_clock = None

    def load_logged_in_email(self):
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except:
            return None

    def load_user_cards(self):
        """Load user's cards for trading with selection support"""
        self.cards_grid.clear_widgets()
        if not self.logged_in_email:
            return
        
        email_key = self.logged_in_email.replace(".", ",")
        ref = db.reference("users")
        data = ref.child(email_key).get()

        if data and "used_codes" in data:
            for code, card in data["used_codes"].items():
                btn = MDRaisedButton(
                    text=f"{card.get('character', 'Unknown').split('(')[0].strip()}\nIQ: {card.get('iq', 0)} | Power: {card.get('power', 0)} | Points: {card.get('points', 0)} | Level: {card.get('level', 1)}",
                    size_hint_y=None,
                    height=dp(60),
                    size_hint=(1, None),
                    md_bg_color=(0.15, 0.15, 0.2, 1),
                    text_color=(1, 1, 1, 1),
                    line_color=(0.3, 0.3, 0.4, 1)
                    )
                # Bind the event after creating the button
                btn.bind(on_release=lambda instance, c=card: self.select_card(c, instance))
                # Store card data in button for reference
                btn.card_data = card
                self.cards_grid.add_widget(btn)

    def select_card(self, card, button):
        """Select a card for trading and update UI"""
        # Reset previously selected button color
        if self.selected_btn:
            self.selected_btn.md_bg_color = self.normal_color
            self.selected_btn.line_color = (0.3, 0.3, 0.4, 1)
        
        # Set new selection
        self.selected_card = card
        self.selected_btn = button
        button.md_bg_color = (0.3, 0.3, 0.5, 1)
        button.line_color = (0, 0, 1, 1)
        
        # Update status label
        self.status_label.text = f"Selected: {card['character'].split('(')[0].strip()}"
        self.status_label.theme_text_color = "Custom"
        self.status_label.text_color = (0.2, 0.9, 0.2, 1)  # Green


    def send_trade(self, instance):
        """Send card to another user"""
        if not self.selected_card:
            self.status_label.text = "Please select a card first!"
            self.status_label.text_color = (1, 0.2, 0.2, 1)  # Red
            return

        receiver = self.receiver_input.text.strip()
        if not receiver:
            self.status_label.text = "Enter receiver's email!"
            self.status_label.text_color = (1, 0.2, 0.2, 1)
            return

        if receiver == self.logged_in_email:
            self.status_label.text = "Can't trade with yourself!"
            self.status_label.text_color = (1, 0.2, 0.2, 1)
            return

        receiver_key = receiver.replace(".", ",")
        if not db.reference("users").child(receiver_key).get():
            self.status_label.text = "User not found!"
            self.status_label.text_color = (1, 0.2, 0.2, 1)
            return

        # Create trade
        trade_ref = db.reference("trades").child(receiver_key)
        trade_id = hashlib.sha256(
            f"{self.logged_in_email}{receiver}{self.selected_card['character']}"
            .encode()
        ).hexdigest()[:10]

        timestamp = str(datetime.datetime.now())

        trade_ref.child(trade_id).set({
            "from": self.logged_in_email,
            "card": self.selected_card,
            "status": "pending",
            "timestamp": timestamp
        })

        # Log history for SENDER
        sender_history_ref = db.reference("trade_history").child(
            self.logged_in_email.replace(".", ",")
        )
        sender_key = f"sender_{trade_id}"
        sender_history_id = f"sender_{trade_id}"
        sender_history_ref.child(sender_history_id).set({
            "type": "sent",
            "character": self.selected_card["character"],
            "status": "pending",
            "to": receiver,
            "timestamp": timestamp
        })


        self.status_label.text = f"Trade sent to {receiver}!"
        self.status_label.text_color = (0.2, 0.9, 0.2, 1)
        self.receiver_input.text = ''

        # Reset selection
        if self.selected_btn:
            self.selected_btn.md_bg_color = self.normal_color
        self.selected_btn = None
        self.selected_card = None

        # Refresh incoming CARDS
        self.load_incoming_trades()

    def load_incoming_trades(self):
        """Load incoming card"""
        self.incoming_grid.clear_widgets()
        if not self.logged_in_email:
            return
            
        email_key = self.logged_in_email.replace(".", ",")
        trades = db.reference("trades").child(email_key).get()
        pending_count = 0
        
        if trades:
            for trade_id, data in trades.items():
                if data["status"] == "pending":
                    pending_count += 1
                    box = BoxLayout(
                        orientation='horizontal',
                        size_hint_y=None,
                        height=dp(70),
                        spacing=dp(10),
                    )
                    
                    # Trade info
                    info_label = MDLabel(
                        text=f"{data['from']}\n{data['card']['character'].split('(')[0]}",
                        halign="left",
                        theme_text_color="Custom",
                        text_color=(0.8, 0.8, 0.8, 1),
                        size_hint_x=0.7,
                    )
                    
                    # Accept button
                    accept_btn = MDIconButton(
                        icon="check",
                        theme_text_color="Custom",
                        text_color=(0.2, 0.9, 0.2, 1),
                        on_release=lambda x, t=trade_id, c=data['card'], f=data['from']: 
                            self.process_trade(t, c, f, "accept"),
                    )
                    
                    # Reject button
                    reject_btn = MDIconButton(
                        icon="close",
                        theme_text_color="Custom",
                        text_color=(0.9, 0.2, 0.2, 1),
                        on_release=lambda x, t=trade_id, c=data['card'], f=data['from']: 
                            self.process_trade(t, c, f, "reject"),
                    )
                    
                    box.add_widget(info_label)
                    box.add_widget(accept_btn)
                    box.add_widget(reject_btn)
                    self.incoming_grid.add_widget(box)
        
        # Update notification dot
        if pending_count > 0:
            if pending_count > self.last_trade_count and self.trade_sound:
                self.trade_sound.play()
        else:
            return
            
        self.last_trade_count = pending_count

    def process_trade(self, trade_id, card, from_user, action):
        """Process trade (accept or reject)"""
        email_key = self.logged_in_email.replace(".", ",")

        # Update trade status in both histories
        status = "accepted" if action == "accept" else "rejected"
        receiver_up = db.reference("trades").child(email_key).child(trade_id).child("from").get()
        timestamp = str(datetime.datetime.now())

        # # Update sender's history
        sender_email_key = from_user.replace(".", ",")
        sender_history_ref = db.reference("trade_history").child(sender_email_key)
        sender_history_ref.child(f"sender_{trade_id}").update({
            "type": "sent",
            "character": card["character"],
            "status": status,
            "to": receiver_up,
            "timestamp": timestamp
        })

        email_key = self.logged_in_email.replace(".", ",")
        history_ref = db.reference("trade_history").child(email_key)
        history_id = f"receive_{hashlib.sha256(
            f"{self.logged_in_email}{from_user}{card['character']}{datetime.datetime.now()}"
            .encode()
        ).hexdigest()[:4]}"

        if action == "accept":
            # Add card to user's collection
            ref = db.reference("users").child(email_key)
            user_data = ref.get()

            if "used_codes" not in user_data:
                user_data["used_codes"] = {}

            # Check for duplicate
            for c in user_data["used_codes"].values():
                if c.get("character") == card.get("character"):
                    self.status_label.text = "You already have this card!"
                    self.status_label.text_color = (1, 0.2, 0.2, 1)
                    db.reference("trades").child(email_key).child(trade_id).delete()
                    self.load_incoming_trades()
                    history_ref.child(history_id).set({
                        "type": "received",
                        "character": card["character"],
                        "status": "Duplicate",
                        "from": from_user,
                        "timestamp": str(datetime.datetime.now())
                    })

                    return

            # Add card
            key = card["character"].split("\n")[0].replace(" ", "")
            user_data["used_codes"][key] = card
            new_points = user_data.get("points", 0) + card.get("points", 0)

            ref.update({
                "used_codes": user_data["used_codes"],
                "points": new_points
            })

            self.status_label.text = f"Trade accepted! +{card.get('points', 0)} points"
            self.status_label.text_color = (0.2, 0.9, 0.2, 1)
            db.reference("trades").child(email_key).child(trade_id).delete()
            history_ref.child(history_id).set({
                "type": "received",
                "character": card["character"],
                "status": "Accepted",
                "from": from_user,
                "timestamp": str(datetime.datetime.now())
            })
        else:
            self.status_label.text = "Trade rejected"
            self.status_label.text_color = (1, 0.5, 0, 1)

            # Remove trade from pending list
            db.reference("trades").child(email_key).child(trade_id).delete()
            self.load_incoming_trades()
            history_ref.child(history_id).set({
                "type": "received",
                "character": card["character"],
                "status": "Rejected",
                "from": from_user,
                "timestamp": str(datetime.datetime.now())
            })

        # Refresh team screen
        if self.manager.has_screen("team"):
            self.manager.get_screen("team").on_enter()


    def check_new_trades(self, dt):
        """Periodically check for new CARDS"""
        self.load_incoming_trades()

    def go_history(self, instance):
        history_screen = self.manager.get_screen("tradehistory")
        history_screen.on_enter()
        self.manager.current = "tradehistory"
        self.manager.transition.direction = 'left'


    def go_redeem(self, instance):
        self.manager.current = "game"
        self.manager.transition.direction = 'right'

    def go_team(self, instance):
        team_screen = self.manager.get_screen("team")
        team_screen.on_enter()
        self.manager.current = "team"
        self.manager.transition.direction = 'left'

    def go_account(self, instance):
        """Navigate to account screen"""
        self.manager.current = "account"
        self.manager.transition.direction = 'left'






class tradehistoryscreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_in_email = None
        self.refresh_clock = None
        
        # Background
        with self.canvas.before:
            self.bg = Rectangle(source='bg_dark.jpg', size=Window.size)
        
        # Title
        self.title = MDLabel(
            text="TRADE HISTORY",
            halign="center",
            font_style="H4",
            pos_hint={"center_x": 0.5, "center_y": 0.95},
            theme_text_color="Custom",
            text_color=(1, 0.84, 0, 1),  # Gold
            size_hint_y=None,
            height=dp(40),
        )
        self.add_widget(self.title)

        # Back button
        self.back_button = MDIconButton(
            icon="arrow-left",
            pos_hint={"x": 0.01, "top": 1},
            size_hint=(None, None),
            size=(dp(40), dp(40)),
            theme_text_color="Custom",
            text_color=(0, 0, 0, 1),
        )
        self.back_button.bind(on_release=self.go_back)
        self.add_widget(self.back_button)

        # History ScrollView
        self.scroll = ScrollView(
            size_hint=(0.95, 0.8),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            bar_width=dp(4),
            bar_color=(0.5, 0.5, 0.8, 0.5),
        )
        
        self.history_layout = GridLayout(
            cols=1,
            spacing=dp(15),
            size_hint_y=None,
            padding=dp(15),
        )
        self.history_layout.bind(minimum_height=self.history_layout.setter('height'))
        self.scroll.add_widget(self.history_layout)
        self.add_widget(self.scroll)

    def on_enter(self):
        """Called when screen is displayed"""
        self.logged_in_email = self.load_logged_in_email()
        self.load_history()
        self.start_refresh_timer()

    def on_leave(self):
        """Called when screen is hidden"""
        self.stop_refresh_timer()

    def start_refresh_timer(self):
        """Start the auto-refresh timer"""
        self.stop_refresh_timer()  # Ensure no duplicate timers
        self.refresh_clock = Clock.schedule_interval(
            lambda dt: self.load_history(), 
            20  # Refresh every 20 second
        )

    def stop_refresh_timer(self):
        """Stop the auto-refresh timer"""
        if self.refresh_clock:
            self.refresh_clock.cancel()
            self.refresh_clock = None


    def load_history(self):
        """Load and display trade history"""
        if not self.logged_in_email:
            return
            
        try:
            email_key = self.logged_in_email.replace(".", ",")
            history_ref = db.reference("trade_history").child(email_key)
            history = history_ref.get()
            
            self.history_layout.clear_widgets()
            
            if not history:
                self.show_empty_message("No trade history yet")
                return
                
            # Sort by timestamp (newest first)
            sorted_history = sorted(
                history.items(),
                key=lambda x: x[1].get("timestamp", ""),
                reverse=True
            )
            
            for history_id, trade in sorted_history:
                self.add_history_item(trade)
        except Exception as e:
            self.show_empty_message(f"Error loading history: {e}")

    def add_history_item(self, trade):
        """Add a trade history item to the layout"""
        card = MDCard(
            size_hint=(1, None),
            height=dp(120),
            padding=dp(15),
            md_bg_color=(0.12, 0.12, 0.2, 0.95),
            radius=[15],
        )
        
        # Determine status color
        if trade["status"] == "accepted":
            status_color = (0.2, 0.9, 0.2, 1)  # Green
        elif trade["status"] == "rejected":
            status_color = (0.9, 0.2, 0.2, 1)  # Red
        else:
            status_color = (0.8, 0.8, 0.8, 1)  # Gray
            
        # Main info
        main_box = BoxLayout(orientation='horizontal')
        
        # Icon based on trade type
        icon = MDIcon(
            icon="arrow-up" if trade["type"] == "sent" else "arrow-down",
            theme_text_color="Custom",
            text_color=status_color,
            size_hint_x=0.1,
        )
        
        # Trade details
        details_box = BoxLayout(orientation='vertical', spacing=dp(5))
        
        # Character and partner
        char_name = trade["character"].split('(')[0].strip()
        partner = trade.get("to", trade.get("from", "Unknown"))
        
        partner_label = MDLabel(
            text=f"With: {partner}",
            halign="left",
            theme_text_color="Custom",
            text_color=(0.5, 0.5, 1, 1),
            font_style="Subtitle1",
        )
        
        char_label = MDLabel(
            text=f"Card: {char_name}",
            halign="left",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="H6",
        )
        
        # Status and timestamp
        status_box = BoxLayout(orientation='horizontal', size_hint_y=None, height=dp(30))
        
        status_label = MDLabel(
            text=f"Status: {trade['status'].capitalize()}",
            halign="left",
            theme_text_color="Custom",
            text_color=status_color,
            font_style="Subtitle1",
        )
        
        timestamp = trade.get("timestamp", "").split('.')[0]  # Remove microseconds
        time_label = MDLabel(
            text=timestamp,
            halign="right",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            font_style="Caption",
        )
        
        status_box.add_widget(status_label)
        status_box.add_widget(time_label)
        
        details_box.add_widget(partner_label)
        details_box.add_widget(char_label)
        details_box.add_widget(status_box)
        
        main_box.add_widget(icon)
        main_box.add_widget(details_box)
        card.add_widget(main_box)
        
        self.history_layout.add_widget(card)

    def show_empty_message(self, message):
        """Show message when no history exists"""
        self.history_layout.add_widget(MDLabel(
            text=message,
            halign="center",
            theme_text_color="Hint",
            font_style="H5",
            size_hint_y=None,
            height=dp(100),
        ))

    def load_logged_in_email(self):
        try:
            with open("logged_in.json", "r") as file:
                data = json.load(file)
                return data.get("email", None)
        except:
            return None

    def go_back(self, instance):
        self.manager.current = "trade"
        self.manager.transition.direction = 'right'
        





class Collecteber(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Teal"
        sm = ScreenManager()

        login_screen = LoginScreen(name="login")
        sm.add_widget(login_screen)
        sm.add_widget(redeemCodeGame(name="game"))
        sm.add_widget(levelscreen(name="level"))
        sm.add_widget(teamscreen(name="team"))
        sm.add_widget(accountscreen(name="account"))
        sm.add_widget(editscreen(name="edit"))
        sm.add_widget(tradingscreen(name="trade"))
        sm.add_widget(tradehistoryscreen(name="tradehistory"))



        logged_in_email = login_screen.load_logged_in_email()
        if logged_in_email:
            sm.current = "game"
        else:
            sm.current = "login"

        return sm



if __name__ == "__main__":
    Collecteber().run()