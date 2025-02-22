from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import *
class Question():
    def __init__(self, label, right, wrong, wrong1, wrong2):
        self.label = label
        self.right = right
        self.wrong = wrong
        self.wrong1 = wrong1
        self.wrong2 = wrong2
q_list = []
q1 = Question('Сколько будет 3 + 3?', '6', '5', '7', '9') 
q_list.append(q1)
q2 = Question('Сколько будет 2 + 2?', '4', '5', '3', '6')
q_list.append(q2)
q3 = Question('Сколько будет 4 + 4?', '8', '5', '3', '6')
q_list.append(q3)
q4 = Question('Сколько будет 5 + 5?', '10', '5', '3', '6')
q_list.append(q4)
q5 = Question('Сколько будет 6 + 6?', '12', '5', '3', '6')
q_list.append(q5)
q6 = Question('Сколько будет 7 + 7?', '14', '56', '30', '69')
q_list.append(q6)
q7 = Question('Сколько будет 8 + 8?', '16', '45', '35', '66')
q_list.append(q7)
q8 = Question('Сколько будет 9 + 9?', '18', '54', '23', '16')
q_list.append(q8)
q9 = Question('Сколько будет 12 + 6?', '18', '52', '34', '61')
q_list.append(q9)
q10 = Question('Сколько будет 6 + 0?', '6', '15', '13', '16')
q_list.append(q10)
app = QApplication([])
wind = QWidget()
wind.setWindowTitle('Memo Card')
wind.resize(500, 500)
wind.total = 0
wind.correct = 0
question = QLabel('Какой национальности не существует?')
ans1 = QRadioButton('Энцы')
ans2 = QRadioButton('Чулымцы')
ans3 = QRadioButton('Смурфы')
ans4 = QRadioButton('Алеуты')
mainHlayout1 = QHBoxLayout()
mainHlayout2 = QHBoxLayout()
mainHlayout3 = QHBoxLayout()
mainHlayout4 = QHBoxLayout()
mainHlayout5 = QHBoxLayout()
mainVlayout1 = QVBoxLayout()
mainVlayout2 = QVBoxLayout()
ans_but = QPushButton('Ответить')
ans_group = QGroupBox("Варианты ответов")
mainHlayout2.addWidget(ans1, alignment = Qt.AlignCenter)
mainHlayout2.addWidget(ans2, alignment = Qt.AlignCenter)
mainHlayout3.addWidget(ans3, alignment = Qt.AlignCenter)
mainHlayout3.addWidget(ans4, alignment = Qt.AlignCenter)
mainVlayout1.addLayout(mainHlayout2)
mainVlayout1.addLayout(mainHlayout3)
ans_group.setLayout(mainVlayout1)
ans_group2 = QGroupBox('Результат теста')
t1 = QLabel('Правильно/неправильно')
t2 = QLabel('Правильный ответ')
but_list = [ans1, ans2, ans3, ans4]
mainVlayout3 = QVBoxLayout()
mainVlayout3.addWidget(t1, alignment = (Qt.AlignLeft|Qt.AlignTop))
mainVlayout3.addWidget(t2, alignment = Qt.AlignHCenter)
ans_group2.setLayout(mainVlayout3)
mainHlayout4.addWidget(ans_group)
mainHlayout4.addWidget(ans_group2)
ans_group2.hide()
mainHlayout1.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
mainHlayout5.addStretch(1)
mainHlayout5.addWidget(ans_but, stretch = 2)
mainHlayout5.addStretch(1)
mainVlayout2.addLayout(mainHlayout1, stretch = 2)
mainVlayout2.addLayout(mainHlayout4, stretch = 8)
mainVlayout2.addStretch(1)
mainVlayout2.addLayout(mainHlayout5, stretch = 1)
mainVlayout2.addStretch(1)
mainVlayout2.setSpacing(4)
button_group = QButtonGroup()
button_group.addButton(ans1)
button_group.addButton(ans2) 
button_group.addButton(ans3) 
button_group.addButton(ans4)  
def show_result():
    ans_group.hide()
    ans_group2.show()
    ans_but.setText('Следующий вопрос')
def show_question():
    ans_group2.hide()
    ans_group.show()
    ans_but.setText('Ответить')
    button_group.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    button_group.setExclusive(True)
def start_test():
    if ans_but.text() == 'Ответить':
        show_result()
    elif ans_but.text() == 'Следующий вопрос':
        show_question()
def ask(q:Question):
    shuffle(but_list)
    but_list[0].setText(q.right)
    but_list[1].setText(q.wrong)
    but_list[2].setText(q.wrong1)
    but_list[3].setText(q.wrong2)
    question.setText(q.label)
    t2.setText(q.right)
    show_question()
def show_correct(result):
    t1.setText(result)
    show_result()
def check_answer():
    if but_list[0].isChecked():
        show_correct('Правильно')
        wind.correct += 1
    else:
        show_correct('Неправильно')
    print('ваша статистика:')
    print('Отвечено', wind.total)
    print('Правильно', wind.correct)
    print('Рейтинг', wind.correct / wind.total * 100)
def next_question():
    curquestion = randint(0, len(q_list) - 1)
    question_sh = q_list[curquestion]
    ask(question_sh)
    wind.total += 1
def click_ok():
    if ans_but.text() == 'Ответить':
        check_answer()
    elif ans_but.text() == 'Следующий вопрос':
        next_question()
ans_but.clicked.connect(click_ok)
next_question()
wind.setLayout(mainVlayout2)
wind.show()
app.exec()