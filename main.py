import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class FontAdjuster(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Font Size and Color Adjuster")
        self.setGeometry(100, 100, 600, 300)

        self.label = QLabel("F1D022056", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont("Courier New", 30))
        self.label.setAutoFillBackground(True)
        self.label.setFixedHeight(100)
        self.label.setMinimumWidth(500)

        self.font_slider = QSlider(Qt.Horizontal)
        self.font_slider.setMinimum(20)
        self.font_slider.setMaximum(60)
        self.font_slider.setValue(30)
        self.font_slider.valueChanged.connect(self.update_font_size)

        self.font_color_slider = QSlider(Qt.Horizontal)
        self.font_color_slider.setMinimum(0)
        self.font_color_slider.setMaximum(255)
        self.font_color_slider.setValue(0)
        self.font_color_slider.valueChanged.connect(self.update_font_color)

        self.bg_color_slider = QSlider(Qt.Horizontal)
        self.bg_color_slider.setMinimum(0)
        self.bg_color_slider.setMaximum(255)
        self.bg_color_slider.setValue(255)
        self.bg_color_slider.valueChanged.connect(self.update_bg_color)

        font_label = QLabel("Font Size")
        font_color_label = QLabel("Font Color")
        bg_color_label = QLabel("Background Color")

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        for title, slider in [(font_label, self.font_slider),
                              (bg_color_label, self.bg_color_slider),
                              (font_color_label, self.font_color_slider)]:
            sublayout = QVBoxLayout()
            sublayout.addWidget(title)
            sublayout.addWidget(slider)
            layout.addLayout(sublayout)

        self.setLayout(layout)
        self.update_colors()

    def update_font_size(self):
        size = self.font_slider.value()
        self.label.setFont(QFont("Courier New", size))

    def update_font_color(self):
        self.update_colors()

    def update_bg_color(self):
        self.update_colors()

    def update_colors(self):
        font_gray = self.font_color_slider.value()
        bg_gray = self.bg_color_slider.value()

        palette = self.label.palette()
        palette.setColor(QPalette.WindowText, QColor(font_gray, font_gray, font_gray))
        palette.setColor(QPalette.Window, QColor(bg_gray, bg_gray, bg_gray))
        self.label.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FontAdjuster()
    window.show()
    sys.exit(app.exec_())
