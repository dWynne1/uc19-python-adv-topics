class Apple:

    def __init__(self):
        self.color = 'red'

    def changeColor(self, new_color):
        self.color = new_color

drews_apple = Apple()
print(drews_apple.color)

jeffs_apple = Apple()
print(jeffs_apple.color)
jeffs_apple.changeColor('blue')
print(jeffs_apple.color)
