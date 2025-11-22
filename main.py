import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui import Ui_MainWindow
import os 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap 
from PIL import Image 

class ImageProcessor():
    def __init__(self):
        self.image = None 
        self.dir = None 
        self.filename = None 
        self.save_dir = "Modified/"

    def loadImage(self, dir, filename):
        self.dir = dir 
        self.filename = filename 
        image_path = os.path.join(dir, filename)
        self.image = Image.open(image_path)
    
    def showImage(self, label_widget, path):
        label_widget.hide()
        pixmapimage = QPixmap(path)
        w, h = label_widget.width(), label_widget.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        label_widget.setPixmap(pixmapimage)
        label_widget.show()

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.configure()
        self.workdir = ''
        self.workimage = ImageProcessor()
        
    def configure(self):
        self.ui.open_folder.clicked.connect(self.showFilenamesList)
        self.ui.list_image.currentRowChanged.connect(self.showChosenImage)
    
    def filter(self, files, extensions):
        result = []
        for filename in files:
            for ext in extensions:
                if filename.lower().endswith(ext):
                    result.append(filename)
                    break 
        return result 
    
    def showFilenamesList(self):
        # 1. Спочатку отримую папку яку я вибрав.
        dir_path = QFileDialog.getExistingDirectory(self, "Оберіть папку: ")
        # 2. Перевіряю чи я взагалі щось вибрав. (вибрав папку)
        if dir_path:
            # 3. Якщо я вибрав папку, то я з dir_path (тут посилання на папку) переносю в workdir
            self.workdir = dir_path 
            # 4. Це розширення фото які я буду потім фільтрувати.
            extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
            # 5. Витягую УСІ файли (без фільтру) і зберігаю їх у змінну.
            all_files_in_dir = os.listdir(self.workdir)
            # 6. Фільтрація (З нею я отримаю ТІЛЬКИ ті файли в яких є формат вказаний в extensions)
            filenames = self.filter(all_files_in_dir, extensions)
            # 7. Оновлення списку на екрані.
            self.ui.list_image.clear()
            self.ui.list_image.addItems(all_files_in_dir)
    
    def showChosenImage(self):
        if self.ui.list_image.currentRow() >= 0:
            filename = self.ui.list_image.currentItem().text()
            self.workimage.loadImage(self.workdir, filename)
            image_path = os.path.join(self.workimage.dir, self.workimage.filename)
            self.workimage.showImage(self.ui.image, image_path)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
