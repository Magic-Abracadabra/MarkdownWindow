from markdown import markdown
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QTextBrowser, QHBoxLayout
from PyQt5.QtGui import QFont

# 幕后
幕后 = QApplication([])

# 平台
平台 = QWidget()
平台.setWindowTitle('Markdown')

# 舞者
输入舞者 = QTextEdit()
显示舞者 = QTextBrowser()

# 舞者之间
输入舞者.textChanged.connect(lambda: 显示舞者.setHtml(markdown(输入舞者.toPlainText())))

# 布局
布局 = QHBoxLayout()
布局.addWidget(输入舞者)
布局.addWidget(显示舞者)
平台.setLayout(布局)

# 演出
幕后.setFont(QFont('楷体', 32))
平台.show()
幕后.exec()
