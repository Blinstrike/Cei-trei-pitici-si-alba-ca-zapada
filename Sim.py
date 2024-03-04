from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import json
import os 
import subprocess

class ParentInfoWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Satisfactory - Parent Confirmation")
        self.setGeometry(100, 100, 600, 400)  # Set initial window size
        self.setStyleSheet("background-color: black; color: red;")

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        email_label = QLabel("Parent Email Address:")
        email_label.setAlignment(Qt.AlignCenter)  # Align label to center
        email_label.setStyleSheet("color: red;")
        layout.addWidget(email_label)

        self.email_input = QLineEdit()
        self.email_input.setMinimumHeight(50)  # Set minimum height for text input
        self.email_input.setStyleSheet("font-size: 24px; color: red;")
        layout.addWidget(self.email_input)

        password_label = QLabel("Password:")
        password_label.setAlignment(Qt.AlignCenter)  # Align label to center
        password_label.setStyleSheet("color: red;")
        layout.addWidget(password_label)

        self.password_input = QLineEdit()
        self.password_input.setMinimumHeight(50)  # Set minimum height for text input
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setStyleSheet("font-size: 24px; color: red;")

        # Button to toggle password visibility
        self.toggle_password_button = QPushButton()
        self.toggle_password_button.setIcon(QIcon("D:\matei\Electronics Sim\Show.png"))  # Change "eye_icon.png" to your icon file
        self.toggle_password_button.setStyleSheet("background-color: transparent;")
        self.toggle_password_button.setCursor(Qt.PointingHandCursor)
        self.toggle_password_button.clicked.connect(self.toggle_password_visibility)

        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_input)
        password_layout.addWidget(self.toggle_password_button)
        layout.addLayout(password_layout)

        save_button = QPushButton("Continue")
        save_button.clicked.connect(self.check_and_save_parent_info)
        save_button.setStyleSheet("font-size: 24px; color: black; background-color: red;")
        layout.addWidget(save_button)

        self.setLayout(layout)

        # Connect returnPressed signal of line edits to check_and_save_parent_info method
        self.email_input.returnPressed.connect(self.check_and_save_parent_info)
        self.password_input.returnPressed.connect(self.check_and_save_parent_info)

    def toggle_password_visibility(self):
        if self.password_input.echoMode() == QLineEdit.Password:
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_password_button.setIcon(QIcon("D:\matei\Electronics Sim\Hide.png"))  # Change "eye_closed_icon.png" to your closed eye icon file
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_password_button.setIcon(QIcon("D:\matei\Electronics Sim\Show.png"))  # Change "eye_icon.png" to your open eye icon file

    def check_and_save_parent_info(self):
        parent_email = self.email_input.text()
        parent_password = self.password_input.text()

        if not parent_email:
            self.show_error_message("Email is missing!")
        elif not parent_password:
            self.show_error_message("Password is missing!")
        else:
            parent_info = {"parent_email": parent_email, "parent_password": parent_password}
            self.save_to_json(parent_info)
            self.run_satisfactory()
            self.close()  # Close the application

    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Error")
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setStyleSheet("background-color: black; color: red;")
        msg_box.addButton(QMessageBox.Ok)
        msg_box.exec()

    def save_to_json(self, data):
        with open("parent_info.json", "w") as json_file:
            json.dump(data, json_file)
        print("Parent information saved successfully!")

    def run_satisfactory(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        satisfactory_path = "D:\XboxGames\Satisfactory v8.3.0\Satisfactory\FactoryGame.exe"
        print("Satisfactory Path:", satisfactory_path)  # Debugging print
        if os.path.exists(satisfactory_path):
            subprocess.Popen(satisfactory_path)
        else:
            print("Satisfactory executable not found.")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    parent_info_widget = ParentInfoWidget()
    parent_info_widget.show()
    sys.exit(app.exec_())
