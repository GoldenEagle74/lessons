from re import split
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QListWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QHBoxLayout, QListWidgetItem, QApplication
from math import pi


class Calculator(QMainWindow):

    def __init__(self):
        super().__init__()

       # setting title
        self.setWindowTitle("Калькулятор")

		# setting geometry
        self.setGeometry(700, 250, 400, 400)

        calc = QWidget()
        self.setCentralWidget(calc)

        vbox = QVBoxLayout()


        # creating a line
        self.list = QListWidget()
        self.list.setItemAlignment(Qt.AlignmentFlag.AlignBottom)
        self.list.setFixedHeight(105)
        
        self.error = QLabel()
        self.error.setFixedHeight(35)
        font = self.error.font()
        font.setPointSize(10)
        self.error.setFont(font)
        self.line = QLineEdit()
        self.line.setFixedHeight(35)
        font = self.line.font()
        font.setPointSize(16)
        self.line.setFont(font)



        grid1 = QGridLayout()
        list_grid = [QPushButton(str(i)) for i in ['⌦','(',')','mod','π',*list(range(7,10)),'÷','√',*list(range(4,7)),'×','x²',*list(range(1,4)),'-','0',',','%','+']]
        for button in list_grid: button.setFixedSize(75,40)
        

        grid2=QGridLayout()
        [grid1.addWidget(elem,id//5,id%5) if id < 15 else grid2.addWidget(elem,(id+1)//5,(id+1)%4) for id,elem in enumerate(list_grid)]


        equal = QPushButton('=')
        equal.setFixedSize(75,85)
        list_grid.append(equal)


        hbox = QHBoxLayout()
        hbox.addLayout(grid2)
        hbox.addWidget(equal)


        vbox.addWidget(self.list)
        vbox.addWidget(self.error)
        vbox.addWidget(self.line)
        vbox.addLayout(grid1)
        vbox.addLayout(hbox)
        vbox.setAlignment(Qt.AlignmentFlag.AlignBottom)
        calc.setLayout(vbox)



        self.stack = []
        operations = {
            'mod':'%',
            '÷':'/',
            '×':'*',
            '-':'-',
            ',':'.',
            '+':'+',
            '²':'**2',
            'π':str(pi)}
        
        
        def func(text,self):
            self.error.setText('')
            if text == 'x²': text = '²'
            if text == '⌦':
                self.stack.clear()
                text = ''
            if text == '=':
                pre_stack = self.stack
                self.stack = ''.join(self.stack)
                for i in range(len(self.stack)-1):
                    if (self.stack[i] in ['²','π',')'] and self.stack[i+1].isdigit()) or (self.stack[i].isdigit() and self.stack[i+1] in ['√','π','(']):
                        self.stack = self.stack[:i+1] + '×' + self.stack[i+1:]
                if '√' in self.stack or '%' in self.stack:
                    nums = []
                    delimiters = list(operations) + ['(',')']
                    stack = split(rf'{delimiters}', self.stack.replace('-','+'))
                    for num in stack:
                        if '√' in num: nums.append((num, num[1:]+'**0.5'))
                        if '%' in num: nums.append((num, stack[stack.index(num)-1] + '×' + str(eval(num[:-1]+'/100'))))
                    for k,v in nums: self.stack = self.stack.replace(k,v)
                for k,v in operations.items(): self.stack = self.stack.replace(k,v)
                try:
                    item = QListWidgetItem(self.line.text() + '=' + str(eval(self.stack)))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignRight)
                    font = item.font()
                    font.setPointSize(12)
                    item.setFont(font)
                    self.list.addItem(item)
                    self.line.setText(str(eval(self.stack)))
                    self.stack = []
                    
                except:
                    self.error.setText('Некорректное выражение')
                    self.stack = pre_stack

                
                return 0
            self.stack.append(text)
            self.line.setText(''.join(self.stack))

    
        def stack_change(text): self.stack=[text]


        self.line.textChanged.connect(stack_change)
        self.line.returnPressed.connect(lambda text=self.line.text(): func(text+'=',self))

        [button.clicked.connect(lambda ch, text=button.text(): func(text,self)) for button in list_grid]
        

if __name__ == '__main__':
    app = QApplication([])
    calc = Calculator()
    calc.show()
    app.exec()