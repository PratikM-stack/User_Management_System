from PyQt5.QtWidgets import QLabel,QLineEdit,QDateEdit,QPushButton,QVBoxLayout,QFormLayout,QFileDialog,QRadioButton,QWidget,QMessageBox,QSplitter
from PyQt5.QtGui import QPixmap,QFont
from PyQt5.QtCore import Qt
from PyQt5 import QtCore,QtGui
from info.UM_info import UM_Info
from dbConfig import db

class UM_UserProfileForm(QWidget):
    def __init__(self, main_widget, outerWidgetLogin):
        super().__init__()
        self.main_widget=main_widget
        self.outerWidgetLogin=outerWidgetLogin
        self.UM_init_ui(main_widget)
    
    def UM_init_ui(self,main_widget):
        header_label=QLabel('User Info Form')
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setStyleSheet('background-color: #003A6B; color: white;padding: 10px; font-size: 22px; max-height:40px')
        
        self.backbtn=QPushButton("about us")
        self.backbtn.clicked.connect(lambda:self.UM_about_us())
        self.backbtn.setStyleSheet("background:qlineargradient(x1:0,y1:0,x2:1,y2:0,stop:0 #013565, stop:1 #057be7);max-width:100px;font-size:20px;color:#ffffff;margin-top:10px")
        
        self.UM_first_name_edit=QLineEdit()
        self.UM_last_name_edit=QLineEdit()
        self.UM_mobile_no_edit=QLineEdit()
        self.UM_college_name_edit = QLineEdit()
        self.UM_date_of_birth = QDateEdit()
        self.UM_age = QLineEdit()
        self.UM_profile_photo_label = QLabel('No file selected')
        self.UM_gender_radio_male = QRadioButton('Male')
        self.UM_gender_radio_female = QRadioButton('Female')
        self.UM_height_edit = QLineEdit()
        # Setting font for form elements
        self.UM_gender_radio_male.setFont(QFont('Arial', 12))
        self.UM_gender_radio_female.setFont(QFont('Arial', 12))
        self.UM_height_edit.setFont(QFont('Arial', 12))
        self.UM_age.setFont(QFont('Arial', 12))
        self.UM_date_of_birth.setDateRange(self.UM_date_of_birth.minimumDate(),self.UM_date_of_birth.maximumDate())
        
        self.UM_image_label=QLabel()
        self.UM_image_label.setAlignment(Qt.AlignCenter)
        self.UM_image_label.setFixedSize(200,200)
        self.UM_image_label.hide()
        
        self.UM_submit_button = QPushButton('Save')
        self.UM_view_record = QPushButton("View All Records")
        # Output label
        self.UM_output_label = QLabel()
        self.UM_output_label.setStyleSheet('font-size: 14px; margin-top:10px;')
        # Labels
        self.UM_age_label = QLabel('Enter Age:')
        self.UM_age_label.setFont(QFont('Arial', 12))
        self.UM_gender_label = QLabel('Gender:')
        self.UM_gender_label.setFont(QFont('Arial', 12))
        self.UM_height_label = QLabel("Height(cm):")
        self.UM_height_label.setFont(QFont('Arial', 12))
        
        # Form layout
        form_layout = QFormLayout()
        form_layout.addRow('Enter First Name:', self.UM_first_name_edit)
        form_layout.addRow('Enter Last Name:', self.UM_last_name_edit)
        form_layout.addRow('Enter Mobile No:', self.UM_mobile_no_edit)
        form_layout.addRow('Enter College Name:', self.UM_college_name_edit)
        form_layout.addRow('Enter DOB:', self.UM_date_of_birth)
        form_layout.addRow(self.UM_age_label,self.UM_age)
        form_layout.addRow(self.UM_gender_label, self.UM_gender_radio_male)
        form_layout.addRow('', self.UM_gender_radio_female)
        form_layout.addRow(self.UM_height_label, self.UM_height_edit)
        form_layout.setContentsMargins(0, 50, 0, 0)
        form_layout.setVerticalSpacing(5)
        # Setting font for form layout items
        for i in range(10):
            item = form_layout.itemAt(i)
            if item is not None:
                widget = item.widget()
                font = widget.font()
                font.setPointSize(12)
                widget.setFont(font)
                
        #button layout
        
        button_layout=QVBoxLayout()
        button_layout.addWidget(self.UM_submit_button)
        button_layout.addWidget(self.UM_view_record)
        button_layout.setContentsMargins(0,200,0,0)
        
        #left half layout
        left_layout=QVBoxLayout()
        left_layout.addWidget(header_label)
        left_layout.addWidget(self.backbtn)
        left_layout.addLayout(form_layout)
        left_layout.addLayout(button_layout)
        left_layout.addWidget(self.UM_output_label)
        
        self.splitter=QSplitter(Qt.Horizontal)
        self.splitter.addWidget(QWidget())
        self.splitter.setSizes([self.width()//2,self.width()//2])
        self.splitter.setStyleSheet("Qsplitter::handle{background:lightgray:}")
        self.splitter.widget(0).setLayout(left_layout)
        self.main_layout=QVBoxLayout()
        self.main_layout.addWidget(self.splitter)
        main_widget.addLayout(self.main_layout)
        
        self.UM_submit_button.clicked.connect(lambda:self.UM_submit_form())
        self.UM_view_record.clicked.connect(lambda:self.UM_fetch_records())
        
    def UM_submit_form(self):
        # Validation
        if not self.UM_first_name_edit.text() or not self.UM_last_name_edit.text() or not self.UM_mobile_no_edit.text():

        # Display an error message if any of the required fields are empty
            QMessageBox.critical(self, "Error", "Please fill in all required fields.")

            return
        # Mobile number validation
        mobile_no = self.UM_mobile_no_edit.text()
        if not mobile_no.isdigit() or len(mobile_no) != 10:
            QMessageBox.critical(self, "Error", "Please enter a valid 10-digit mobile number.")
            return
        # Get the values from the form
        first_name = self.UM_first_name_edit.text()
        last_name = self.UM_last_name_edit.text()
        gender = 'Male' if self.UM_gender_radio_male.isChecked() else 'Female'
        height = self.UM_height_edit.text()
        college_name = self.UM_college_name_edit.text()
        dob = self.UM_date_of_birth.text()
        age = self.UM_age.text()
        
        # Form output text
        output_text = f"Name: {first_name} {last_name}\n" \
                    f"Mobile No: {mobile_no}\n" \
                    f"College Name: "\
                    f"Date Of Birth: "\
                    f"Age: "\
                    f"Gender: {gender}\n" \
                    f"Height: {height} cm"
        # Get a reference to the Firestore collection
        user_profiles_ref = db.collection('user_profiles')      
        # Create a new user profile entry
        user_profile = {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_no': mobile_no,
            'college_name' : college_name,
            'dob': dob,
            'age':age,
            'gender': gender,
            'height': height
        }
        #get a refernce to the firestore collection    
        new_user_ref=user_profiles_ref.add(user_profile)
        # Get the unique ID generated by Firestore
        user_id = new_user_ref[1].id
        # Display success message with QMessageBox
        success_message = f"Form submitted successfully.\n\n" \
        f"Firestore User ID: {user_id}\n" \
        f"{output_text}"

        QMessageBox.information(self, "Success", success_message)
        
    # Method to fetch and display all records
    def UM_fetch_records(self):
        self.main_layout.removeWidget(self.splitter)
        obj = UM_Info(self.main_layout, UM_UserProfileForm)
    def UM_about_us(self):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://www.core2web.in/about-us"))