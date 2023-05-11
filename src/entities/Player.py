from entities.entity import Entity
from entities.shield import Shield
from pygame import Surface, Vector2, draw

class Player(Entity):
    def __init__(self, position: Vector2, health: int, shield: Shield):
        # inicializando classe pai
        Entity.__init__(self, position, None)

        self.health = health
        self.shield = shield
        return

    # esses métodos de movimento não vão existir no nosso jogo.
    # criei só pra poder mexer a bolinha na tela durante o teste
    def moveUp(self, deltaTime: int) -> None:
        self.position.y -= 300 * deltaTime

    def moveLeft(self, deltaTime: int) -> None:
        self.position.x -= 300 * deltaTime
        
    def moveDown(self, deltaTime: int) -> None:
        self.position.y += 300 * deltaTime

    def moveRight(self, deltaTime: int) -> None:
        self.position.x += 300 * deltaTime

    # -Sobrescrevendo o método abstrato da classe pai.
    # -Assim, cada entidade (player, projectile, shield)
    # define como será desenhada na tela, já que elas
    # devem ser desenhadas de maneira diferente.
    # -Isso pode mudar depois que implementarmos as sprites.
    def drawAt(self, screen: Surface) -> None:
        # desenhando o player como um círculo de raio 15 por enquanto, só pra testar
        draw.circle(screen, 'Red', self.position, 15)
        return 