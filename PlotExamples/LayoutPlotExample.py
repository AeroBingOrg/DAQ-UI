from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import QTimer
import pyqtgraph as pg
import sys
from random import randint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Layout + Plots")

        self.x = list(range(10))
        self.y1 = [randint(20, 40) for _ in range(10)]
        self.y2 = [randint(100, 120) for _ in range(10)]
        self.y3 = [randint(0, 50) for _ in range(10)]

        self.plot_layout = QHBoxLayout()

        self.plot_graph1 = pg.PlotWidget()
        self.plot_graph2 = pg.PlotWidget()
        self.plot_graph3 = pg.PlotWidget()

        pen = pg.mkPen(color=(255, 0, 0))
        styles = {'color':'red', 'font-size':'30pt'}

        self.plot_graph1.setTitle("Plot 1", color="b", size="30pt")
        self.plot_graph2.setTitle("Plot 2", color="r", size="30pt")
        self.plot_graph3.setTitle("Plot 3", color="k", size="30pt")

        self.plot_graph1.setBackground("w")
        self.plot_graph2.setBackground("w")
        self.plot_graph3.setBackground("w")

        self.plot_graph1.setLabel('left', 'Units *', **styles)
        self.plot_graph1.setLabel('bottom', 'Units *', **styles)

        self.plot_graph2.setLabel('left', 'Units *', **styles)
        self.plot_graph2.setLabel('bottom', 'Units *', **styles)

        self.plot_graph3.setLabel('left', 'Units *', **styles)
        self.plot_graph3.setLabel('bottom', 'Units *', **styles)

        self.plot_graph1.showGrid(x=True, y=True)
        self.plot_graph2.showGrid(x=True, y=True)
        self.plot_graph3.showGrid(x=True, y=True)

        self.plot_line1 = self.plot_graph1.plot(self.x, self.y1, pen=pen, symbol="+")
        self.plot_line2 = self.plot_graph2.plot(self.x, self.y2, pen=pen, symbol="star")
        self.plot_line3 = self.plot_graph3.plot(self.x, self.y3, pen=pen, symbol="d")

        self.plot_layout.addWidget(self.plot_graph1)
        self.plot_layout.addWidget(self.plot_graph2)
        self.plot_layout.addWidget(self.plot_graph3)

        widget = QWidget()
        widget.setLayout(self.plot_layout)
        self.setCentralWidget(widget)

        self.timer = QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.update_plot)
        self.timer.start()

    def update_plot(self):
        self.x = self.x[1:]
        self.x.append(self.x[-1] + 1)
        self.y1 = self.y1[1:]
        self.y1.append(randint(20, 40))
        self.plot_line1.setData(self.x, self.y1)
        self.y2 = self.y2[1:]
        self.y2.append(randint(100, 120))
        self.plot_line2.setData(self.x, self.y2)
        self.y3 = self.y3[1:]
        self.y3.append(randint(0, 50))
        self.plot_line3.setData(self.x, self.y3)


app = QApplication()
w = MainWindow()
w.show()

app.exec()