from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpinBox, QButtonGroup, QRadioButton, QGroupBox
from PyQt5.QtCore import Qt

# Віджети
card_width, card_height = 600, 500
win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(0,0)
win_card.setWindowTitle("Memory card")

menu = QPushButton("Меню")
btn_sleep = QPushButton("Відпочити")
box_Minutes = QSpinBox()
box_Minutes.setValue(30)
text_minutes = QLabel("хвилин")
btn_OK = QPushButton("Відповісти")
lb_Question = QLabel('Запитання')

answer_1 = QRadioButton("1")
answer_2 = QRadioButton("2")
answer_3 = QRadioButton("3")
answer_4 = QRadioButton("4")

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer_1)
RadioGroup.addButton(answer_2)
RadioGroup.addButton(answer_3)
RadioGroup.addButton(answer_4)

Result = QLabel('Правильно')
Correct = QLabel('відповідь')

# Групи
RadioGroupBox = QGroupBox("Варіанти відповідей")
AnsGroupBox = QGroupBox()
AnsGroupBox.hide()

# Макети для варіантів відповідей
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans1 = QHBoxLayout()

layout_ans2.addWidget(answer_1)
layout_ans2.addWidget(answer_2)
layout_ans3.addWidget(answer_3)
layout_ans3.addWidget(answer_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

# Макет для результату
layout_res = QVBoxLayout()
layout_res.addWidget(Result)
layout_res.addWidget(Correct)
AnsGroupBox.setLayout(layout_res)

# Основні макети
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()
layout_card = QVBoxLayout()

layout_line1.addWidget(menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(text_minutes)

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(AnsGroupBox)
layout_line3.addWidget(RadioGroupBox)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)

layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addLayout(layout_line4)
layout_card.setSpacing(5)

win_card.setLayout(layout_card)
win_card.show()
