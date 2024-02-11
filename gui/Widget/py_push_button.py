import os

from PySide6.QtGui import QPaintEvent #para criar quadro para desenho

from qt_core import *

class PyPushButton(QPushButton):
    def __init__(
        self,
        text= "", # texto do botão 
        height = 40, # altura do botão 
        minimum_width = 50, # largura minima 
        text_padding = 55, # afastar o texto do alinhamento da direita 
        text_color = "#c3ccdf", # cor do nosso texto 
        icon_path = "", # caminho do icone do botão 
        icon_color = "#c3ccdf", # cor do icone 
        btn_color ="#44475a", # cor de fundo do botão 
        btn_hover = "#4f5368", # cor do botão quando o mouse estiver sobre ele
        btn_pressed = "#282a36", # cor do botão ao ser pressionado
        is_active = False # parametro para saber se o botão está ativo
    ):
        super().__init__()
        
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)
        
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active
        
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
        )
    
    def set_active(self,is_active_menu):
        self.set_style(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = is_active_menu
        )
        
    def set_style(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#44475a",
        btn_hover = "#4f5368", # cor do botão quando o mouse estiver sobre ele
        btn_pressed = "#282a36", # cor do botão ao ser pressionado
        is_active = False # parametro para saber se o botão está ativo
    ):
        style = f"""
        
        QPushButton {{
            color: {text_color};
            background-color:{btn_color};
            padding-left:{text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover{{
            background-color: {btn_hover};
        }}
        QPushButton:pressed{{
            background-color: {btn_pressed};
        }}
        """
        
        active_style = f"""
         QPushButton {{
            background-color:{btn_hover};
            border-right: 5px solid #282a36;
        }}
        """
        
        if not is_active:
            self.setStyleSheet(style)
        
        else:
            self.setStyleSheet(style + active_style)
    
    def paintEvent(self, event):
        QPushButton.paintEvent(self,event)
        
        # painter 
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        rect = QRect(0,0,self.minimum_width,self.height())
        
        self.draw_icon(qp, self.icon_path, rect, self.icon_color)
        
        qp.end()
        
    def draw_icon(self, qp, image, rect,color):
        # pegar a pasta da imagem: 
        app_path = os.path.abspath(os.getcwd())
        folder = "gui/icons"
        path = os.path.join(app_path,folder)
        icon_path = os.path.normpath(os.path.join(path,image))
        
        icon = QPixmap(icon_path)
        painter = QPainter(icon)
        painter.setCompositionMode(QPainter.CompositionMode.CompositionMode_SourceIn)
        painter.fillRect(icon.rect(), color)
        qp.drawPixmap(
            (rect.width() - icon.width()) / 2,
            (rect.height() - icon.height()) / 2,
            icon
        )
        painter.end()       
