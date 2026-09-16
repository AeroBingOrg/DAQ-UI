from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        self.x = list(range(100))
        self.y = [randint(0, 100) for _ in range(100)]

        self.plot_graph.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        #When updating a graph in real time make a variable that is equal to the plot
        #This will get updated when calling the data_line.setData
        #Will probably have a variable for each of the plots we plan of having and will have to use SetData
        self.data_line = self.plot_graph.plot(self.x, self.y, pen=pen)

        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)

        self.y = self.y[1:]
        self.y.append(randint(0, 100))

        #The use of SetData, which will just update the plot with whatever is given
        self.data_line.setData(self.x, self.y)


app = QApplication()
w = MainWindow()
w.show()

app.exec()