import sys
import pymysql.cursors
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QVBoxLayout, QAbstractItemView, QGridLayout, QFrame, QHeaderView, QHBoxLayout, QRadioButton
from PyQt5.QtGui import QIcon, QPixmap, QIntValidator
from PyQt5.QtCore import pyqtSlot 
from twilio.rest import Client
#---------NEW WINDOW------------------------------------------------
class Login(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Dormitory Management System'.format("Login/Register")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 625, 351) 
        self.setFixedSize(self.size())
        
  #--------frame qouh touh--------------------      
        self.background = QLabel(self)
        self.backgroundLoc = QPixmap('etona.jpg')
        self.background.setPixmap(self.backgroundLoc)
        self.background.move(0,0)
        self.background.resize(625,351)
        self.background.setScaledContents(True)
#-------MAINPAGE LOGINNNN----------------------------        
        self.title = QLabel(self)
        self.title.setText('WELCOME TO YOUR MANAGEMENT SYSTEM')
        self.title.move(50, 25)
        self.title.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:white")
        self.title.adjustSize()
        
        self.username = QLabel(self)
        self.username.setText('Username')
        self.username.move(400, 50)
        self.username.setStyleSheet("font: 15pt Arial Rounded MT Bold; color:white")
        self.username.adjustSize()
        
        self.password = QLabel(self)
        self.password.setText('Password')
        self.password.move(400, 100)
        self.password.setStyleSheet("font: 15pt Arial Rounded MT Bold; color:white")
        self.password.adjustSize()    
        
#----------FILL UP BLANKS------------------------        
        self.mainuser = QLineEdit(self)
        self.mainuser.move(400, 80)
        self.mainuser.resize(170, 20)
        self.mainuser.setMaxLength(15)
        self.mainuser.setStyleSheet("font: 10pt Arial Rounded MT Bold; color:black")
        
        self.mainpassword = QLineEdit(self)
        self.mainpassword.setEchoMode(QLineEdit.Password)
        self.mainpassword.move(400, 130)
        self.mainpassword.resize(170, 20)
        self.mainpassword.setMaxLength(15)
        self.mainpassword.setStyleSheet("font: 10pt Arial Rounded MT Bold; color:black")
        
#FOR MY BUTTONS--------------------------------
        self.Loginb = QPushButton('LOGIN', self)
        self.Loginb.move(350, 200)
        self.Loginb.resize(100,25)
        self.Loginb.clicked.connect(self.Login)
        self.Loginb.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #fcfeff; border-style: outset; border-radius: 5px; padding: 2px;")
        
        
        self.Registerb = QPushButton('REGISTER', self)
        self.Registerb.move(500, 200)
        self.Registerb.resize(100,25)
        self.Registerb.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #fcfeff; border-style: outset; border-radius: 5px; padding: 2px;")
        self.Registerb.clicked.connect(self.RegisterWindow) 
        self.show()
        
    def Login(self):
        # Value allocator for Username and Password
        Username = self.mainuser.text() 
        Password = self.mainpassword.text() 
        
        # Connects Python to Mysql
        connection = pymysql.connect(host = 'localhost',
                             user= 'root',
                             password = '',
                             db = 'dormdb',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor,
                             port = 3306)
        with connection.cursor() as cursor:
            result=cursor.execute('SELECT * from accounts where Username = %s AND Password = %s ;',(Username,Password)) # Checks if there is a row with same Username and Password
           
            # If there is a corresponding account
            if(result==1): 
                # Declares the Account that is currently logged in
                global Account
                Account = Username
                self.newWindow = home()
                self.newWindow.show()
                self.hide()
                
            # If Username or Password is blank
            elif(len(Username) == 0 or len(Password) == 0):
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Do not leave blanks')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
             
            # If there is no corresponding account            
            else:
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Invalid Account!')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
        
                
#MyWindows---------------------------------------
    def RegisterWindow(self):
        self.newWindow = RegisterWindow()
        self.newWindow.show()
        self.hide
        
    def home(self):
        self.newWindow = home()
        self.newWindow.show()
        
#-----REGISTER WINDOW----------------        
class RegisterWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Register'.format("'")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 450, 325) 
        self.setFixedSize(self.size())
        
        #self.setStyleSheet("QWidget {background-image: url(acrybackground.jpg)}")
        self.regbg = QLabel(self)
        self.regbgLoc = QPixmap('heyo.jpg')
        self.regbg.setPixmap(self.regbgLoc)
        self.regbg.move(0,0)
        self.regbg.resize(450,330)
        self.regbg.setScaledContents(True)
        
        self.submitbreg = QPushButton('SUBMIT', self)
        self.submitbreg.move(150,250)
        self.submitbreg.resize(120,30)
        self.submitbreg.clicked.connect(self.Register)
        self.submitbreg.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #fcfeff; border-style: outset; border-radius: 5px; padding: 2px;")
                     
        self.userreg = QLabel(self)
        self.userreg.setText('Username:')
        self.userreg.move(130, 30)
        self.userreg.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        self.userreg.adjustSize()
        
        self.userbox = QLineEdit(self)
        self.userbox.move(130, 70)
        self.userbox.resize(170, 20)
        self.userbox.setMaxLength(15)
        self.userbox.setStyleSheet('border: 2px solid #f0ffe3;border-radius: 10px;'
                                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff);'
                                    'padding: 0 5px;'
                                    'font: 9pt Impact;color: #c0c7bf;')
        self.passreg = QLabel(self)
        self.passreg.setText('Password:')
        self.passreg.move(130, 100)
        self.passreg.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        self.passreg.adjustSize()
        
        self.passbox = QLineEdit(self)
        self.passbox.move(130, 140)
        self.passbox.resize(170, 20)
        self.passbox.setMaxLength(15)
        self.passbox.setEchoMode(QLineEdit.Password)
        self.passbox.setStyleSheet('border: 2px solid #f0ffe3;border-radius: 10px;'
                                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff);'
                                    'padding: 0 5px;'
                                    'font: 9pt Impact;color: #c0c7bf;')
        
        self.confirmpasswordreg = QLabel(self)
        self.confirmpasswordreg.setText('Confirm Password:')
        self.confirmpasswordreg.move(130, 180)
        self.confirmpasswordreg.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        self.confirmpasswordreg.adjustSize()
        
        self.confirmbox = QLineEdit(self)
        self.confirmbox.move(130, 210)
        self.confirmbox.resize(170, 20)
        self.confirmbox.setMaxLength(15)
        self.confirmbox.setEchoMode(QLineEdit.Password)
        self.confirmbox.setStyleSheet('border: 2px solid #f0ffe3;border-radius: 10px;'
                                    'background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #ffffff);'
                                    'padding: 0 5px;'
                                    'font: 9pt Impact;color: #c0c7bf;')
                                        
                                        
        self.show()
#-----REGISTER CONNECTION        
    def Register(self):
        # Value allocator for Username and Passwords
        Username = self.userbox.text() 
        Password = self.passbox.text()
        ConfirmPassword = self.confirmbox.text()
        
        # Connects Python to Mysql
        connection = pymysql.connect(host = 'localhost',
                             user= 'root',
                             password = '',
                             db = 'dormdb',
                             charset = 'utf8mb4',
                             cursorclass = pymysql.cursors.DictCursor,
                             port = 3306)
        with connection.cursor() as cursor:
            # Checks if the Username checked is existing and stores the value in result
            result=cursor.execute('SELECT * from Accounts where Username = %s ;',(Username)) 
            
            # Checks if the Password is shorter than seven characters
            if(len(Password)<4): 
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))    
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Do not leave boxes empty')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
                
            # Checks if the Username is shorter than seven characters   
            elif(len(Username)<4): 
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Username is too short!')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
            
            # Checks if the two passwords are equal
            elif(Password!=ConfirmPassword): 
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('The passwords does not match!')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
            
            # Checks if the Username is already taken
            elif(result==1): 
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\WarningMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('The username is already taken!')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
                
            # Adds another Account
            else:
                with connection.cursor() as cursor:
                    cursor.execute('INSERT INTO Accounts VALUES (%s, %s)', (Username,Password)) 
                    connection.commit()
                self.newWindow = Login()
                self.newWindow.show()
                self.hide()
                self.msgBox = QMessageBox()
                self.msgBox.setWindowIcon(QIcon(r'C:\Users\USER\Desktop\Project Images\SuccessMessageBoxIcon.png'))
                self.msgBox.setIcon(QMessageBox.NoIcon)
                self.msgBox.setText('Your account has been registered!')
                self.msgBox.setWindowTitle('Thank you!')
                self.msgBox.show()
                
        
        self.show() 
    def Loginb(self):
        Username = self.lineEdit.text()
        password = self.lineEdit1.text()

        NoEmptyField = True


        if (len(Username) == 0 or len(password) == 0):
            NoEmptyField = False 
            self.messagebox = QMessageBox()
            self.messagebox.setText("Please Complete the Entry.")
            self.messagebox.setWindowTitle("Message!")
            self.messagebox.setIcon(QMessageBox.Information)
            self.messagebox.show()

        if (NoEmptyField):
			# Connect to the database
            connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='dormdb',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            result = cursor.execute("select * from accounts where Username = %s and password = %s",(Username,password))
        if (result == 0):
            self.messagebox = QMessageBox()
            self.messagebox.setText("Invalid account!")
            self.messagebox.setWindowTitle("Message!")
            self.messagebox.setIcon(QMessageBox.Information)
            self.messagebox.show()

        else: 
            self.newWindow = RegisterWindow()
            self.newWindow.show()
            self.hide() 
#--------------HOME WINDOW-----------------            
class home(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Welcome to your Dormitory Management System'.format("'")
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 900, 500) # Window Size
        self.setFixedSize(self.size())
        self.contact = ''
        
        
        self.setWindowIcon(QIcon("orange.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(100,100,350,500)
        
        # Connects Python to Mysql
        connection = pymysql.connect(host = 'localhost',
                            user= 'root',
                            password = '',
                            db = 'dormdb',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            port = 3306)
        with connection.cursor() as cursor:
            numberoftenants=cursor.execute('SELECT * from Tenants')
            cursor.execute('SELECT * from Tenants')
            
        # Creates the Table
        #self.tab = QtWidgets.QTabWidget(self)
        self.tableWidget = QTableWidget()
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setMaximumWidth(590)
        self.tableWidget.setMaximumHeight(500)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['First Name','Last Name','Gender','Age','Address','ContactNo']) # Set Horizontal Header Labels
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed) # Makes the Columns width fixed
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) # Stretches the Columns to fit
        self.tableWidget.cellClicked.connect(self.Clicked)  
        
        self.tableWidget.setRowCount(numberoftenants)    
        for i in range(numberoftenants):
            tenant=cursor.fetchone()
            self.tableWidget.setItem(i,0, QTableWidgetItem('{}'.format(tenant['FirstName'])))
            self.tableWidget.setItem(i,1, QTableWidgetItem('{}'.format(tenant['LastName'])))
            self.tableWidget.setItem(i,2, QTableWidgetItem('{}'.format(tenant['Gender'])))
            self.tableWidget.setItem(i,3, QTableWidgetItem('{}'.format(tenant['Age'])))
            self.tableWidget.setItem(i,4, QTableWidgetItem('{}'.format(tenant['Address'])))
            self.tableWidget.setItem(i,5, QTableWidgetItem('{}'.format(tenant['ContactNo'])))
        self.tableWidget.cellChanged.connect(self.update)  
        #self.tabWidget.addTab(self.tab,"")                
 #frame           
        self.background = QLabel(self)
        self.backgroundLoc = QPixmap('homepage.jpg')
        self.background.setPixmap(self.backgroundLoc)
        self.background.move(0,0)
        self.background.resize(900,500)
        self.background.setScaledContents(True)
        # Adds a layout for widgets on the window
        self.Layout = QHBoxLayout()
        self.Layout.addWidget(self.tableWidget)
        self.setLayout(self.Layout)
        

        self.addnewbutton = QPushButton('ADD NEW INFORMATION', self)
        self.addnewbutton.move(30,15)
        self.addnewbutton.resize(120,30)
        self.addnewbutton.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #a6e3e3; border-style: outset; border-radius: 5px; padding: 2px;")    
        self.addnewbutton.clicked.connect(self.OpenWindow)
        
        self.deleteinformationbutton = QPushButton('DELETE INFORMATION', self)
        self.deleteinformationbutton.move(30,100)
        self.deleteinformationbutton.resize(120,30)
        self.deleteinformationbutton.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #a6e3e3; border-style: outset; border-radius: 5px; padding: 2px;")
        self.deleteinformationbutton.clicked.connect(self.Delete)
                                         
        self.signoutbutton = QPushButton('sign out', self)
        self.signoutbutton.move(35, 400)
        self.signoutbutton.resize(120,30)
        self.signoutbutton.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #a6e3e3; border-style: outset; border-radius: 5px; padding: 2px;")
        self.signoutbutton.clicked.connect(self.signout)
        
        #self.sms = QPushButton('send sms', self)
        #self.sms.clicked.connect(self.text)
        #self.sms.move(35,350)
        #self.sms.resize(120,30)
        #self.sms.setStyleSheet('QPushButton {border: 2px solid #f0ffe3;border-radius: 15px;font: 8pt Impact;color: #ffffff;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #9acced, stop: 1 #95edc7);}'
                                         #'QPushButton:hover {border: 2px solid #f0ffe3;border-radius: 15px;font: 8pt Impact;color: #ffffff;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c4bbf0, stop: 1 #f0bbe6);}'
                                         #'QPushButton:pressed {border: 0px solid #f0ffe3;border-radius: 15px;font: 8pt Impact;color: #ffffff;background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #bd3ec2, stop: 1 #de497d);}')    
        #self.addnewbutton.clicked.connect(self.OpenWindow)
        
                                        
        
    def signout (self):
        self.newWindow = Login()
        self.newWindow.show()
        self.hide()
        
        
        
    def update(self,row,column):
        
        	
        print('Updated!')
		
            

        Info = self.tableWidget.item(row,column).text()
        FirstName = self.tableWidget.item(row,0).text()
        LastName = self.tableWidget.item(row,1).text()
        Gender = self.tableWidget.item(row,2).text()
        Age = self.tableWidget.item(row,3).text()
        Address = self.tableWidget.item(row,4).text()
        ContactNo = self.tableWidget.item(row,5).text()
        Tenants = (FirstName,LastName,Gender,Age,Address,ContactNo)
        
        connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='dormdb',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            cursor.execute('select TenantID from Tenants where ContactNo = %s',(ContactNo))
            Tenant = cursor.fetchone()
            TenantID = Tenant['TenantID']
        Notblank = True

        if (len(Info) == 0):
            Notblank = False
            self.messagebox = QMessageBox()
            self.messagebox.setText("")
            self.messagebox.setWindowTitle("Message!")
            self.messagebox.setIcon(QMessageBox.Information)
            self.messagebox.show()

			

            connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='dormdb',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
            with connection.cursor() as cursor:
                numberoftenants=cursor.execute('select * from Tenants')
                cursor.execute('select * from Tenants')


            for i in range(numberoftenants):
                tenants=cursor.fetchone()
			
                self.tableWidget.setItem(i,0,QTableWidgetItem('{}'.format(tenant['FirstName'])))
                self.tableWidget.setItem(i,1,QTableWidgetItem('{}'.format(tenant['LastName'])))
                self.tableWidget.setItem(i,2,QTableWidgetItem('{}'.format(tenant['Gender'])))
                self.tableWidget.setItem(i,3,QTableWidgetItem('{}'.format(tenant['Age'])))
                self.tableWidget.setItem(i,4,QTableWidgetItem('{}'.format(tenant['Address'])))
                self.tableWidget.setItem(i,5,QTableWidgetItem('{}'.format(tenant['ContactNo'])))
             
        else:
             print('yas')
             connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='dormdb',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
             with connection.cursor() as cursor:
                    cursor.execute('update tenants set FirstName = %s ,LastName = %s,Gender = %s,Age = %s,Address = %s,ContactNo = %s where TenantID = %s',(FirstName,LastName,Gender,Age,Address,ContactNo,TenantID))
                    connection.commit()                                      
        
    def Delete(self):
        if(len(self.contact)==0):
            self.msgBox = QMessageBox()
            self.msgBox.setIcon(QMessageBox.Information)
            self.msgBox.setText('Please Select A Row')
            self.msgBox.setWindowTitle('Warning!')
            self.msgBox.show()
            
        
        else:
            connection = pymysql.connect(host = 'localhost',
                            user= 'root',
                            password = '',
                            db = 'dormdb',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            port = 3306)
            with connection.cursor() as cursor: 
                cursor.execute('delete from tenants where ContactNo = %s',(self.contact))
                numberoftenants=cursor.execute('SELECT * from Tenants')
                cursor.execute('SELECT * from Tenants')
                connection.commit()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Deleted Succesfully!')
                self.msgBox.setWindowTitle('Success!')
                self.msgBox.show()
                
                self.tableWidget.setRowCount(numberoftenants)    
                for i in range(numberoftenants):
                    tenant=cursor.fetchone()
                    self.tableWidget.setItem(i,0, QTableWidgetItem('{}'.format(tenant['FirstName'])))
                    self.tableWidget.setItem(i,1, QTableWidgetItem('{}'.format(tenant['LastName'])))
                    self.tableWidget.setItem(i,2, QTableWidgetItem('{}'.format(tenant['Gender'])))
                    self.tableWidget.setItem(i,3, QTableWidgetItem('{}'.format(tenant['Age'])))
                    self.tableWidget.setItem(i,4, QTableWidgetItem('{}'.format(tenant['Address'])))
                    self.tableWidget.setItem(i,5, QTableWidgetItem('{}'.format(tenant['ContactNo'])))
                
                     
             
        
        
        
    def Clicked(self,row,column):
        self.contact = self.tableWidget.item(row,5).text()
        
     #show windows----------------------------------------------------------------------------   
    def OpenWindow(self):
        self.newWindow = AddWindow()
        self.newWindow.show()
        self.hide()
        
    def DeleteWindow(self):
        self.newWindow = DeleteWindow()
        self.newWindow.show()
        
class AddWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Tenant{}s Information'.format("'") # Window Title
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 400, 300) # Window Size
        self.setFixedSize(self.size())
        
        self.background = QLabel(self)
        self.backgroundLoc = QPixmap('heyo.jpg')
        self.background.setPixmap(self.backgroundLoc)
        self.background.move(0,0)
        self.background.resize(400,300)
        self.background.setScaledContents(True)
        
        self.firstnamelabel = QLabel(self)
        self.firstnamelabel.setText('First Name:')
        self.firstnamelabel.move(0, 0)
        self.firstnamelabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.firstnamelabel.adjustSize()
        
        self.firstname = QLineEdit(self)
        self.firstname.move(150, 0)
        self.firstname.resize(140, 20)
        self.firstname.setMaxLength(15)
        self.firstname.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        
        self.lastnamelabel = QLabel(self)
        self.lastnamelabel.setText('Last Name:')
        self.lastnamelabel.move(0,50)
        self.lastnamelabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.lastnamelabel.adjustSize()
        
        self.lastname = QLineEdit(self)
        self.lastname.move(150, 50)
        self.lastname.resize(140, 20)
        self.lastname.setMaxLength(15)
        self.lastname.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        
        self.genderlabel = QLabel(self)
        self.genderlabel.setText('Gender: female   male')
        self.genderlabel.move(0,90)
        self.genderlabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.genderlabel.adjustSize()
        
        self.radiobutton1 = QRadioButton(self)
        self.radiobutton1.move(150,95)
     
        
        self.radiobutton2 = QRadioButton(self)
        self.radiobutton2.move(230,95)
   
        
        self.agelabel = QLabel(self)
        self.agelabel.setText('Age:')
        self.agelabel.move(0,130)
        self.agelabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.agelabel.adjustSize()
        
        self.age = QLineEdit(self)
        self.age.move(150, 130)
        self.age.resize(140, 20)
        self.age.setMaxLength(3)
        self.age.setValidator(QIntValidator())
        self.age.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        
        self.addresslabel = QLabel(self)
        self.addresslabel.setText('Address:')
        self.addresslabel.move(0,170)
        self.addresslabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.addresslabel.adjustSize()
        
        self.address = QLineEdit(self)
        self.address.move(150, 170)
        self.address.resize(140, 20)
        self.address.setMaxLength(15)
        self.address.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
        
        self.contactlabel = QLabel(self)
        self.contactlabel.setText('Contact:')
        self.contactlabel.move(0,210)
        self.contactlabel.setStyleSheet("font: 16pt Arial Rounded MT Bold; color:white")
        self.contactlabel.adjustSize()
        
        self.contact = QLineEdit(self)
        self.contact.move(150, 210)
        self.contact.resize(140, 20)
        self.contact.setMaxLength(12)
        #self.contact.setValidator(QIntValidator())
        self.contact.setStyleSheet("font: 11pt Arial Rounded MT Bold; color:black")
                                        
        self.submitbutton = QPushButton('Submit', self)
        self.submitbutton.move(70,250)
        self.submitbutton.resize(120,30)
        self.submitbutton.clicked.connect(self.Submit)
        self.submitbutton.setStyleSheet("font: 10pt Arial Rounded MT Bold; background-color: #a6e3e3; border-style: outset; border-radius: 5px; padding: 2px;")
        
        
    def Submit(self):
        Gender = ''
        if(self.radiobutton1.isChecked()):
            Gender = 'Female'
        elif(self.radiobutton2.isChecked()):
            Gender = 'Male'
        FirstName = self.firstname.text()
        LastName =self.lastname.text()
        Age = self.age.text()
        Address= self.address.text()
        ContactNo = self.contact.text()
        Information = (Gender,FirstName,LastName,Age,Address,ContactNo)
        
        NotBlank = True
        
        for i in Information:
            if(len(i)==0):
                NotBlank = False
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Please do not leave an entry blank!')
                self.msgBox.setWindowTitle('Warning!')
                self.msgBox.show()
                break
        
        if(NotBlank):
            Age = int(Age)
            connection = pymysql.connect(host = 'localhost',
                            user= 'root',
                            password = '',
                            db = 'dormdb',
                            charset = 'utf8mb4',
                            cursorclass = pymysql.cursors.DictCursor,
                            port = 3306)
            with connection.cursor() as cursor:    
                cursor.execute('insert into tenants (FirstName,LastName,Gender,Age,Address,ContactNo) values (%s,%s,%s,%s,%s,%s)',(FirstName,LastName,Gender,Age,Address,ContactNo))
                connection.commit()
                self.msgBox = QMessageBox()
                self.msgBox.setIcon(QMessageBox.Information)
                self.msgBox.setText('Thank you! Added Succesfully')
                self.msgBox.setWindowTitle('Add Success!')
                self.msgBox.show()
                self.hide()
                self.newWindow = home()
                self.newWindow.hide()
                self.newWindow.show()
                

#---------INDEX.PY----------------------------        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = Login()
    sys.exit(app.exec_())
