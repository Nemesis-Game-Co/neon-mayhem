from abc import ABC, abstractmethod
from pygame import Vector2, Surface

class Entity(ABC):
    def __init__(self, position: Vector2, sprite: Surface | None) -> None:
        self.__position = position
        self.__sprite = sprite

        if self.__sprite == None:
            self.__sprite = Surface(10, 10)

        self.__sprite.fill('Red')
        self.__spriteRect = self.__sprite.get_rect()
        self.__spriteRect.x, self.__spriteRect.y = position

        return

    @abstractmethod   
    def drawAt(self, screen: Surface) -> None:
        pass