from abc import ABC, abstractmethod
from pygame import Vector2, Surface

# -Classe abstrata base de todas as entidades.
# -É uma classe que não deve ser instanciada, 
# serve apenas de base para atributos comuns à todas
# as entidades.
# -Ou seja, player, projectile e shield possuem
# todos os atributos e métodos que a classe 
# Entity possui, pois derivam desta.
class Entity(ABC):
    # Vector2 é, resumidamente, uma classe do estilo:
    # class Vector2:
    #     x: float
    #     y: float
    def __init__(self, position: Vector2, sprite: Surface | None) -> None:
        self.position = position
        self.sprite = sprite

        # isso fica pra testar sprites posteriormente
        # if self.sprite == None:
        #     self.sprite = Surface((10, 10))

        # self.sprite.fill('Red')
        # self.spriteRect = self.sprite.get_rect()
        # self.spriteRect.x, self.spriteRect.y = position

        return

    # esse @abstractmethod serve pra declarar que o método
    # drawAt não vai ser definido/implementado nessa classe,
    # mas que as subclasses dela deverão obrigatoriamente
    # implementar esse método, afinal elas têm que ser 
    # desenhadas na tela
    @abstractmethod   
    def drawAt(self, screen: Surface) -> None:
        # veja que eu não escrevi nenhum código dentro da função,
        # só declarei o formato dela: recebe uma tela na qual a
        # entidade será desenhada e não retorna nada
        pass