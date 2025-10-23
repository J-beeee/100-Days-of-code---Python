#import colorgram
#
#colors = colorgram.extract('polizei.png', 99)
#
#
#rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
import random
from turtle import Turtle, Screen

color_list = [
    (250, 221, 65),   # Sonnengelb
    (90, 107, 56),    # Moosgrün
    (40, 65, 89),     # Stahlblau
    (93, 65, 18),     # Goldbraun
    (145, 146, 56),   # Olivgelb
    (222, 168, 61),   # Honig
    (36, 26, 11),     # Dunkelbraun
    (159, 73, 39),    # Rostrot
    (52, 93, 99),     # Petrol
    (177, 97, 163),   # Flieder
    (241, 124, 72),   # Apricot
    (90, 60, 155),    # Violett
    (19, 123, 74),    # Smaragdgrün
    (198, 47, 47),    # Ziegelrot
    (65, 105, 225),   # Königsblau
    (255, 140, 0),    # Orange
    (124, 205, 124),  # Frühlingsgrün
    (0, 191, 255),    # Himmelblau
    (255, 99, 71),    # Tomatenrot
    (186, 85, 211),   # Orchidee
    (255, 215, 0),    # Goldgelb
    (154, 205, 50),   # Gelbgrün
    (205, 133, 63),   # Peru
    (46, 139, 87),    # Seegrün
    (176, 224, 230),  # Hellblau
    (147, 112, 219),  # Mittelviolett
    (60, 179, 113),   # Mediumgrün
    (238, 130, 238),  # Magenta
    (218, 112, 214),  # Orchidee hell
    (205, 92, 92),    # Indisches Rot
    (139, 69, 19),    # Sattelbraun
    (72, 61, 139),    # Dunkellila
    (50, 205, 50),    # Limettengrün
    (255, 160, 122),  # Lachs
    (70, 130, 180),   # Stahlblau hell
    (199, 21, 133),   # Himbeere
    (255, 105, 180),  # Pink
    (210, 105, 30),   # Schokoladenbraun
    (0, 128, 128),    # Teal
    (128, 0, 128),    # Lila
    (255, 69, 0),     # Feuerrot
    (46, 90, 150),    # Nachtblau
    (135, 206, 235),  # Sky Blue
    (189, 183, 107),  # Khaki
    (60, 179, 200),   # Türkisblau
    (127, 255, 0),    # Neon-Grün
    (222, 184, 135),  # Sandbraun
    (255, 182, 193),  # Rosa
    (240, 128, 128),  # Hellrot
    (70, 90, 40),     # Waldgrün
    (173, 216, 230),  # Babyblau
    (244, 164, 96),   # Sandstein
    (152, 251, 152),  # Hellgrün
    (139, 0, 139),    # Dunkellila
    (205, 200, 0),    # Goldgrün
    (255, 127, 80),   # Koralle
    (154, 205, 50),   # Limettengelb
    (100, 149, 237),  # Kornblumenblau
    (240, 230, 140),  # Hellgelb
    (255, 228, 181),  # Pfirsich
    (0, 255, 255),    # Cyan
    (34, 139, 34),    # Waldgrün
    (173, 255, 47),   # Helllime
    (233, 150, 122),  # Lachsorange
    (255, 99, 71),    # Tomate
    (70, 130, 180),   # Stahlblau
    (186, 85, 211),   # Medium-Orchid
    (30, 144, 255),   # Dodger Blue
    (244, 164, 96),   # Sandy Brown
    (255, 218, 185),  # Peach Puff
    (205, 92, 92),    # Light Coral
    (139, 69, 19),    # Saddle Brown
    (255, 160, 122),  # Light Salmon
    (233, 150, 122),  # Dark Salmon
    (219, 112, 147),  # Pale Violet Red
    (255, 105, 180),  # Hot Pink
    (240, 128, 128),  # Light Coral
    (46, 139, 87),    # Sea Green
    (34, 139, 34),    # Forest Green
    (100, 149, 237),  # Cornflower Blue
    (123, 104, 238),  # Medium Slate Blue
    (186, 85, 211),   # Medium Orchid
    (199, 21, 133),   # Medium Violet Red
    (210, 105, 30),   # Chocolate
    (139, 0, 139),    # Dark Magenta
    (0, 128, 128),    # Teal
    (255, 140, 0),    # Dark Orange
    (255, 215, 0),    # Gold
    (255, 0, 255),    # Fuchsia
    (0, 191, 255),    # Deep Sky Blue
    (124, 252, 0),    # Lawn Green
    (173, 255, 47),   # Green Yellow
    (154, 205, 50),   # Yellow Green
    (255, 20, 147),   # Deep Pink
    (70, 130, 180),   # Steel Blue
    (244, 164, 96),   # Sandy Brown
]

t = Turtle()
s = Screen()
s.colormode(255)
t.hideturtle()
t.penup()
x= -350
y= -350
t.setposition(x,y)
t.speed("fastest")

#def move_up():
#    t.setheading(90)
#    t.forward(70)
#def turn_around(i):
#    if i % 2 != 0:
#        t.setheading(180)
#    else:
#        t.setheading(0)

i=1
while i <11:
    i += 1
    y += 70
    t.setposition(x,y)
    for _ in range(10):
        t.forward(70)
        t.dot(20,random.choice(color_list))

t.setposition(-1000, -1000)
s.exitonclick()