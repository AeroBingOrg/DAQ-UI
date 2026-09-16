from PySide6.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.plot_graph = pg.PlotWidget()
        self.setCentralWidget(self.plot_graph)

        hour = [1,2,3,4,5,6,7,8,9,10,11,12]
        temperature = [30, 32, 35, 32, 34, 53, 10, 12, 43, 45, 77, 65]

        pen = pg.mkPen(color=(255, 0, 0))
        styles = {'color':'red', 'font-size':'20px'}
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setLabel('left', 'Temperature (C)', **styles)
        self.plot_graph.setLabel('bottom', 'Hour (H)', **styles)
        self.plot_graph.setTitle("Your Title Here", color="b", size="30pt")
        self.plot_graph.setBackground('w')
        self.plot_graph.plot(hour, temperature, pen=pen)

app = QApplication()
w = MainWindow()
w.show()
app.exec()