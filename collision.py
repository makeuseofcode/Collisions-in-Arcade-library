import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
MOVEMENT_SPEED = 5

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height, "My Game")
        arcade.set_background_color(arcade.color.WHITE)
        self.player = arcade.SpriteSolidColor(50, 50, arcade.color.BLUE)
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = 50
        self.enemies = arcade.SpriteList()
        self.score = 0
        for i in range(3):
            enemy = arcade.SpriteSolidColor(50, 50, arcade.color.RED)
            enemy.center_x = random.randint(0, SCREEN_WIDTH)
            enemy.center_y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
            self.enemies.append(enemy)

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemies.draw()
        arcade.draw_text(f"Score: {self.score}", 10, SCREEN_HEIGHT - 30, arcade.color.BLACK, 16)

    def update(self, delta_time):
        if arcade.check_for_collision_with_list(self.player, self.enemies):
            print("Game Over")
            arcade.close_window()
        else:
            self.player.update()
            for enemy in self.enemies:
                enemy.center_y -= MOVEMENT_SPEED / 2
                if enemy.center_y < 0:
                    enemy.center_x = random.randint(0, SCREEN_WIDTH)
                    enemy.center_y = random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT)
                    self.score += 1

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.center_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.center_x += MOVEMENT_SPEED

   

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
