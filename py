import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Balle:
    def __init__(self, x, y, change_x, change_y, rayon, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < self.rayon:
            self.x = self.rayon
            self.change_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:
            self.x = SCREEN_WIDTH - self.rayon
            self.change_x *= -1
        if self.y < self.rayon:
            self.y = self.rayon
            self.change_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.y = SCREEN_HEIGHT - self.rayon
            self.change_y *= -1

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    def update(self):
        self.x += self.change_x
        self.y += self.change_y

        if self.x < 0:
            self.x = 0
            self.change_x *= -1
        elif self.x + self.width > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH - self.width
            self.change_x *= -1
        if self.y < 0:
            self.y = 0
            self.change_y *= -1
        elif self.y + self.height > SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.height
            self.change_y *= -1

    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.l_balle = []
        self.l_rectangle = []

    def on_draw(self):
        arcade.start_render()
        for balle in self.l_balle:
            balle.draw()
        for rectangle in self.l_rectangle:
            rectangle.draw()

    def on_update(self, delta_time):
        for balle in self.l_balle:
            balle.update()
        for rectangle in self.l_rectangle:
            rectangle.update()

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass

    def on_mouse_press(self, x, y, button, modifiers):
        les_couleurs = [arcade.color.RED, arcade.color.BLUE, arcade.color.GREEN, arcade.color.ORANGE,
                        arcade.color.PINK, arcade.color.PURPLE, arcade.color.YELLOW]

        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.randint(10, 30)
            color = random.choice(les_couleurs)
            balle = Balle(x, y, random.randint(-10, 10), random.randint(-10, 10), rayon, color)
            self.l_balle.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            color = random.choice(les_couleurs)
            rectangle = Rectangle(x, y, random.randint(-10, 10), random.randint(-10, 10),
                                   random.randint(20, 100), random.randint(20, 100), color, random.randint(0, 360))
            self.l_rectangle.append(rectangle)


def main():
    my_game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
    arcade.run()

