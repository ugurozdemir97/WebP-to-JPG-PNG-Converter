from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from converter import Window
from PIL import Image
from pathlib import Path
import sys
import os


class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.path = None
        self.ui = Window()
        self.ui.setupUi(self)

        # ------------------------ BUTTONS ----------------------- #

        self.ui.about.clicked.connect(self.about)
        self.ui.select.clicked.connect(self.select)
        self.ui.jpg.clicked.connect(self.convert)
        self.ui.png.clicked.connect(self.convert)

    # ------------------------ ABOUT ----------------------- #

    @staticmethod
    def about():
        message = QMessageBox()
        message.setWindowTitle("WebP Converter")
        message.setText("This simple program allows you to convert annoying WebP images to JPG or PNG formats easily. "
                        "\n\n                                         Written by Uğur Özdemir in 2022.")
        message.setIcon(QMessageBox.Information)
        message.setStandardButtons(QMessageBox.Ok)
        message.exec_()

    # ------------------------ SELECT ----------------------- #

    def select(self):
        self.path, _ = QFileDialog.getOpenFileNames(self, "Open file", "", "Image files (*.webp)")
        self.ui.files.setText(f"Files selected: [{len(self.path)}]")

    # ----------------------- CONVERT ----------------------- #

    def convert(self):

        sender = self.sender()
        if sender.text() == "Convert to JPG":
            extension = "jpg"
        else:
            extension = "png"

        if self.path:  # If image is selected

            image_path = Path(self.path[0]).parent.absolute()  # Create a new folder to save images in the image folder
            if not os.path.exists(f"{image_path}/WebP Converter"):
                os.makedirs(f"{image_path}/WebP Converter")
            image_path = f"{image_path}/WebP Converter"

            try:
                for i in self.path:  # For each image, convert and save in the new path.
                    image = Image.open(i).convert("RGB")
                    image_name = os.path.basename(i)
                    image.save(f"{image_path}/{image_name}.{extension}")
            except:
                message = QMessageBox()
                message.setWindowTitle("WebP Converter")
                message.setText("An error occurred during the conversion. Sorry :(")
                message.setIcon(QMessageBox.Warning)
                message.setStandardButtons(QMessageBox.Ok)
                message.exec_()
                self.ui.files.setText(f"Files selected: [0]")
            else:
                self.path = None
                self.ui.files.setText(f"Files selected: [0] | Successful!")


def application():
    win = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(win.exec_())


application()
