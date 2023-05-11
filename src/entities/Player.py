from entity import Entity
from shield import Shield
from pygame import Surface, Vector2, draw

class Player(Entity):
    def __init__(self, position: Vector2, health: int, shield: Shield):
        Entity.__init__(position, None)
        self.__health = health
        self.__shield = shield
        return

    def drawAt(self, screen: Surface) -> None:
        draw.circle(screen, 'Red', self.__position, 15)
        return 