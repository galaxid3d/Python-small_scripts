# 20.02.2023 by galaxid3d
# Рисует цифры, точку, двоеточие, нижнее подчёркивание с помощью черепахи

from turtle import *
import datetime

SIZE = 20
offset = 3
X_POS_LEFT = -(screensize()[0] - SIZE)
Y_POS_LEFT = 240
COLS = 23
shape('turtle')
bgcolor('black')
color('white', 'green')
speed(850)

penup()
setposition(X_POS_LEFT, Y_POS_LEFT)
pendown()

def draw_number(number):
	if number == "0":
		setheading(90)
		
		for _ in range(2):
			forward(2 * SIZE)
			right(90)
			forward(SIZE)
			right(90)
		
		penup()
		setheading(0)
		forward(SIZE)
	elif number == "1":
		penup()
		setheading(90)
		forward(2 * SIZE)
		right(90)
		forward(SIZE)
		pendown()
		setheading(-90)
		
		forward(2 * SIZE)
	elif number == "2":
		penup()
		setheading(90)
		forward(2 * SIZE)
		pendown()
		
		for _ in range(3):
			right(90)
			forward(SIZE)
		for _ in range(2):
			left(90)
			forward(SIZE)
	elif number == "3":
		penup()
		setheading(90)
		forward(2 * SIZE)
		pendown()
		
		for j in range(2):
			for _ in range(3 - j):
				right(90)
				forward(SIZE)
			penup()
			right(180)
			forward(SIZE)
			pendown()
	elif number == "4":
		penup()
		setheading(90)
		forward(2 * SIZE)
		pendown()
		
		right(180)
		forward(SIZE)
		for _ in range(2):
			left(90)
			forward(SIZE)
		right(180)
		forward(2 * SIZE)
	elif number == "5":
		penup()
		setheading(90)
		forward(2 * SIZE)
		right(90)
		forward(SIZE)
		pendown()
		setheading(180)

		for _ in range(2):
			forward(SIZE)
			left(90)
		for _ in range(3):
			forward(SIZE)
			right(90)
		
		penup()
		right(90)
		forward(SIZE)
	elif number == "6":
		penup()
		setheading(90)
		forward(2 * SIZE)
		right(90)
		forward(SIZE)
		pendown()
		setheading(180)

		for _ in range(2):
			forward(SIZE)
			left(90)
		for _ in range(4):
			forward(SIZE)
			right(90)
		
		penup()
		for _ in range(2):
			forward(SIZE)
			right(90)
	elif number == "7":
		penup()
		setheading(90)
		forward(2 * SIZE)
		pendown()
		setheading(0)
		
		forward(SIZE)
		right(90)
		forward(2 * SIZE)
	elif number == "8":
		setheading(90)
		
		for _ in range(2):
			forward(2 * SIZE)
			right(90)
			forward(SIZE)
			right(90)
		
		penup()
		forward(SIZE)
		right(90)
		pendown()
		forward(SIZE)
		penup()
		right(90)
		forward(SIZE)
		left(90)
	elif number == "9":
		setheading(90)
		
		penup()
		forward(SIZE)
		pendown()
		for _ in range(2):
			forward((1 + _) * SIZE)
			right(90)
			forward(SIZE)
			right(90)
		
		penup()
		forward(SIZE)
		right(90)
		pendown()
		forward(SIZE)
		penup()
		right(90)
		forward(SIZE)
		left(90)
	elif number == ".":
		penup()
		setheading(-180)
		forward(offset)
		right(90)
		pendown()
		for _ in range(4):
			forward(offset)
			left(90)
	elif number == ":":
		penup()
		setheading(-180)
		forward(offset)
		right(90)
		forward(offset)
		pendown()
		for __ in range(2):
			for _ in range(4):
				forward(offset)
				left(90)
			if __ == 0:
				penup()
				forward(3 * offset)
				pendown()
		
		penup()
		setheading(-90)
		forward(4 * offset)
	elif number == " ":
		penup()
		setheading(0)
		forward(SIZE)
	elif number == "_":
		setheading(0)
		forward(SIZE)
	elif number == "\n":
		penup()
		setheading(0)
		setposition(X_POS_LEFT, ycor() - 2 * SIZE - 3 *offset)
	penup()
	setheading(0)
	if number != "\n":
		forward(offset if number in "\n:." else 3 * offset)
	pendown()

while True:
	new_line = 0
	text = str(datetime.datetime.now()) + "\n"
	for number in text:
		if abs(xcor()) > screensize()[0] or abs(ycor()) > screensize()[1]:
			exitonclick()
		
		draw_number(number)
		if not number in "\n:.":
			new_line += 1
			if new_line % COLS == 0:
				drawNumber("\n")
		elif number == "\n":
			new_line = 0
