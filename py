#Enoch immanuel wang
#importer les modules
import arcade
import random
#set le size de l,écran
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
#liste des couleurs
les_couleurs = [arcade.color.AERO_BLUE, arcade.color.AFRICAN_VIOLET, arcade.color.AIR_FORCE_BLUE, arcade.color.AQUA,
                arcade.color.BABY_BLUE_EYES, arcade.color.BANANA_YELLOW, arcade.color.BLIZZARD_BLUE,
                arcade.color.BLUEBERRY]


#créer une classe pour les balls
class Balls:
    def __init__(self, x, y, c_x, c_y, rayon, colors):
        self.x = x
        self.y = y
        self.c_x = c_x
        self.c_y = c_y
        self.rayon = rayon
        self.colors = colors
#créer une fonction pour update
    def update(self):

        self.x += self.c_x
        self.y += self.c_y

        if self.x < self.rayon:

            self.c_x *= -1
        elif self.x > SCREEN_WIDTH - self.rayon:

            self.c_x *= -1
        if self.y < self.rayon:

            self.c_y *= -1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.c_y *= -1
#créer une fonction pour dessiner
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.colors)

#créer une classe pour les rectanglees
class Rectangle:
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.colors, self.angle)
    def __init__(self, x, y, c_x, c_y, width, height, colors, angle):
        self.x = x
        self.y = y
        self.c_x = c_x
        self.c_y = c_y
        self.width = width
        self.height = height
        self.colors = colors
        self.angle = angle
    def update(self):
        self.x += self.c_x
        self.y += self.c_y
        if self.x < 0:
            self.x = 0
            self.c_x *= -1
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.c_x *= -1
        if self.y < 0:
            self.y = 0
            self.c_y *= -1
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.c_y *= -1

#créer une classe pour le jeux, pour le window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "bruhh")
        self.l_balle = []
        self.l_recs = []
    def update(self, delta_time):
        for balles in self.l_balle:
            balles.update()
        for rec in self.l_recs:
            rec.update()
    def on_draw(self):
        arcade.start_render()
        for balles in self.l_balle:
            balles.draw()
        for recs in self.l_recs:
            recs.draw()
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.uniform(10, 30)
            colors = random.choice(les_couleurs)
            balle = Balls(x, y, random.uniform(-5, 5), random.uniform(-5, 5), rayon, colors)
            if balle.c_y == 0:
                balle.c_y = 1
            if balle.c_x == 0:
                balle.c_x = 1
            self.l_balle.append(balle)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            width = random.uniform(20, 50)
            height = random.uniform(20, 50)
            colors = random.choice(les_couleurs)
            rec = Rectangle(x, y, random.uniform(-5, 5), random.uniform(-5, 5), width, height, colors, random.uniform(1,180))
            if rec.c_y == 0:
                rec.c_y = 1
            if rec.c_x == 0:
                rec.c_x = 1
            self.l_recs.append(rec)
    def setup(self):
        arcade.set_background_color(arcade.color.BLACK)
        arcade.schedule(self.update, 1/60)
#créer une fonction pour commencer le jeux
def main():
    window = MyGame()
    window.setup()
    arcade.run()
main()
