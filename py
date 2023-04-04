#Enoch immanuel wang
#importer les modules
import arcade
import random
#set le size de l,écran
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
#liste des couleurs
les_couleurs = [arcade.color.AERO_BLUE, arcade.color.AFRICAN_VIOLET, arcade.color.AIR_FORCE_BLUE, arcade.color.AQUA,
                arcade.color.BABY_BLUE_EYES, arcade.color.BANANA_YELLOW, arcade.color.BLIZZARD_BLUE,
                arcade.color.BLUEBERRY]


#créer une classe pour les balls
class FortniteBallsss:
    #def l'initialization des attribut des balsssss
    def __init__(self, x, y,c_y , c_x, rayon, colors):
        self.rayon = rayon
        self.c_x = c_x
        self.c_y = c_y
        self.colors = colors
        self.x = x
        self.y = y
#créer une fonction pour update
    def update(self):
        self.x += self.c_x
        self.y += self.c_y
        if self.y < self.rayon:
            self.c_y *= -1
            self.c_y *= 1.1
        elif self.y > SCREEN_HEIGHT - self.rayon:
            self.c_y *= -1
            self.c_y *= 1.1
        if self.x < self.rayon:
                self.c_x *= -1
                self.c_x *= 1.1
        elif self.x > SCREEN_WIDTH - self.rayon:
                self.c_x *= -1
                self.c_x *= 1.1
#créer une fonction pour dessiner
    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.colors)

#créer une classe pour les rectanglees
class Rectangle:
    #Créer une fonction pour dessiner
    def draw(self):
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.colors, self.angle)
    # une fonction pour initialisation des attribut dans la classe des rectangles
    def __init__(self, x, y, c_x, c_y, width, height, colors, angle):
        self.c_x = c_x
        self.c_y = c_y
        self.x = x
        self.y = y
        self.angle = angle
        self.width = width
        self.height = height
        self.colors = colors
    #crééer une fonction pour faire bougers les ballssssss
    def update(self):
        self.x += self.c_x
        self.y += self.c_y
        #bounce off the wall
        if self.x < 0:
            self.x = 0
            self.c_x *= -1
            self.c_x *= 1.1
        elif self.x > SCREEN_WIDTH - self.width:
            self.x = SCREEN_WIDTH - self.width
            self.c_x *= -1
            self.c_x *= 1.1
        if self.y < 0:
            self.y = 0
            self.c_y *= -1
            self.c_y *= 1.1
        elif self.y > SCREEN_HEIGHT - self.height:
            self.y = SCREEN_HEIGHT - self.height
            self.c_y *= -1
            self.c_y *= 1.1

#créer une classe pour le jeux, pour le window
class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "HAAland>>>>>MESSI"*1000)
        #liste des blass ainsi que les recs
        self.l_recs = []
        self.l_balle = []
    #def mise a jour les rec et les balls qui est par rapport au time delta
    def update(self, delta_time):
        for balles in self.l_balle:
            balles.update()
        for rec in self.l_recs:
            rec.update()
    #créer une fonction pour pouvoir dessiner les rescs ainsi que les cercles
    def on_draw(self):
        arcade.start_render()
        for balles in self.l_balle:
            balles.draw()
        for recs in self.l_recs:
            recs.draw()
    #créer une fonction pour le mouse press, a chaque fois on appui sur une touche de la souris
    def on_mouse_press(self, x, y, button, modifiers):
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = random.uniform(10, 30)
            colors = random.choice(les_couleurs)
            balle = FortniteBallsss(x, y, random.uniform(-5, 5), random.uniform(-5, 5), rayon, colors)
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

#créer une fonction pour commencer le jeux
def main():
    window = MyGame()
    arcade.run()
#appeler main    
main()
