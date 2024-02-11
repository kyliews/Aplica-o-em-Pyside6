from qt_core import *
from gui.pages.ui_pages import Ui_StackedWidget
from gui.Widget.py_push_button import PyPushButton



class ui_mainWindow(object):
    
    def setup_ui(self,parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        parent.resize(1200,720)
        parent.setMinimumSize(960,540)
        
        self.central_frame = QFrame()
        self.central_frame.setStyleSheet("background-color: #282e36")
        
        parent.setCentralWidget(self.central_frame)
        
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color:#44475a")
        self.left_menu.setMaximumWidth(50)
        self.left_menu.setMinimumWidth(50)
        
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(50)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame {background-color:red; }")
        
        
        self.left_menu_top_frame_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_frame_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_frame_layout.setSpacing(0)
        
        self.left_menu_spacer = QSpacerItem(20,20,QSizePolicy.Policy.Minimum,QSizePolicy.Policy.Expanding)
        
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame {background-color:red; }")
        
        self.left_menu_bottom_frame_layout = QVBoxLayout(self.left_menu_bottom_frame) 
        self.left_menu_bottom_frame_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_frame_layout.setSpacing(0)
        
        
        self.left_menu_label_version = QLabel("V1.0.0")
        self.left_menu_label_version.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.left_menu_label_version.setMinimumWidth(30)
        self.left_menu_label_version.setMaximumWidth(30)
        self.left_menu_label_version.setStyleSheet("color:#c3ccdf")
    
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        # BOTÕES DO MENU:
        
        self.toggle_buttom = PyPushButton(
            text = 'Ocultar Menu',
            is_active = True,
            icon_path = "icon_menu.svg"
        )
        self.btn_1 = PyPushButton(
            text = 'Página Inicial',
            icon_path = "icon_home.svg"
        )
        self.btn_2 = PyPushButton(
            text = 'Página 2',
            icon_path = "icon_widgets.svg"
        )
        
            
        #self.btn_3 = QPushButton("3")
        
        # ADICIONANDO OS BOTÕES NO LEFT MENU:
        
        self.left_menu_top_frame_layout.addWidget(self.toggle_buttom)
        self.left_menu_top_frame_layout.addWidget(self.btn_1)
        self.left_menu_top_frame_layout.addWidget(self.btn_2)
        #self.left_menu_top_frame_layout.addWidget(self.btn_3)
    
        
        self.content = QFrame()
        self.content.setStyleSheet("background-color:#282a36")
        
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color:#21232d;color:#6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        self.left_top_bar = QLabel("Esse menu é top!")
        self.top_spacer = QSpacerItem(20,20,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.rigth_top_bar = QLabel("|PAGINA INICIAL|")
        self.rigth_top_bar.setStyleSheet("font:700 9pt 'Segoe UI'")
        
        self.top_bar_layout.addWidget(self.left_top_bar)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.rigth_top_bar)
        
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size:12pt;color:#f8f8f2")
        self.ui_pages = Ui_StackedWidget()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.page_3)
        
        self.bottom_bar = QFrame()
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setStyleSheet("background-color:#21232d;color:#6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        
        self.left_bottom_bar = QLabel("Criado por: Kylie")
        self.bottom_spacer = QSpacerItem(20,20,QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Minimum)
        self.rigth_bottom_bar = QLabel("@ 2024")
        
        self.bottom_bar_layout.addWidget(self.left_bottom_bar)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.rigth_bottom_bar)
        
        
        self.settings_buttom = PyPushButton(
            text = "Configurações",
            icon_path = "icon_settings.svg"
        )
        self.left_menu_bottom_frame_layout.addWidget(self.settings_buttom)
        
        
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        