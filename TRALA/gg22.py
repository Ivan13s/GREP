from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPainter, QPainterPath, QPen, QColor
from PySide6.QtWidgets import QVBoxLayout, QSlider, QWidget, QApplication


class CPBar(QWidget):
    def __init__(self):
        super().__init__()
        self.p=0
        self.setMinimumSize(208, 208)

    def upd(self,pp):
        if self.p == pp:
            return
        self.p = pp
        self.update()

    def paintEvent(self,e):
        pd = self.p * 360
        rd = 360 - pd
        p = QPainter(self)
        p.fillRect(self.rect(), Qt.white)
        p.translate(4, 4)
        p.setRenderHint(QPainter.Antialiasing)
        path, path2 = QPainterPath(),QPainterPath()
        path.moveTo(100, 0)
        path.arcTo(QRectF(0, 0, 200, 200), 90, -pd)
        pen, pen2 = QPen(), QPen()
        pen.setCapStyle(Qt.FlatCap)
        pen.setColor(QColor("#30b7e0"))
        pen.setWidth(8)
        p.strokePath(path, pen)
        path2.moveTo(100, 0)
        pen2.setWidth(8)
        pen2.setColor(QColor("#d7d7d7"))
        pen2.setCapStyle(Qt.FlatCap)
        pen2.setDashPattern([0.5, 1.105]) # remove this line to have continue cercle line
        path2.arcTo(QRectF(0, 0, 200, 200), 90, rd)
        pen2.setDashOffset(2.2) # this one too
        p.strokePath(path2, pen2)


class Test(QWidget):
  def __init__(self):
      super().__init__()
      l = QVBoxLayout(self)
      p = CPBar()
      s = QSlider(Qt.Horizontal, self)
      s.setMinimum(0)
      s.setMaximum(100)
      l.addWidget(p)
      l.addWidget(s)
      self.setLayout(l)
      s.valueChanged.connect(lambda :p.upd(s.value()/s.maximum()))

if __name__ == '__main__':
    app = QApplication()
    main_widget = Test()
    main_widget.show()
    app.exec_()