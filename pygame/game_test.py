import pygame

class Wall:
    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.blocks = []

    def create_wall(self):
        for row in range(self.rows):
            block_row = []
            for col in range(self.cols):
                block_x = col * self.width
                block_y = row * self.height
                rect = pygame.Rect(block_x, block_y, self.width, self.height)
                block_row.append(rect)
            self.blocks.append(block_row)

    def draw_wall(self, screen):
        for row in self.blocks:
            for block in row:
                pygame.draw.rect(screen, (255, 255, 255), block)


class Paddle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, direction):
        if direction == "left":
            self.x -= self.speed
        elif direction == "right":
            self.x += self.speed


class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y


import unittest
import pygame

class TestGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen_width = 600
        self.screen_height = 600
        self.screen = pygame.Surface((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()

        self.wall = Wall(rows=10, cols=10, width=50, height=20)
        self.wall.create_wall()
        self.player_paddle = Paddle(x=100, y=100, width=80, height=20, speed=5)
        self.ball = Ball(x=self.player_paddle.x + (self.player_paddle.width // 2),
                         y=self.player_paddle.y - self.player_paddle.height,
                         radius=8, speed_x=3, speed_y=-3)

    def test_wall_creation(self):
        self.assertIsInstance(self.wall, Wall)

    def test_paddle_movement(self):
        initial_x = self.player_paddle.x
        self.player_paddle.move("right")
        self.assertEqual(self.player_paddle.x, initial_x + self.player_paddle.speed)

    def test_ball_movement(self):
        initial_x = self.ball.x
        initial_y = self.ball.y
        self.ball.move()
        self.assertEqual(self.ball.x, initial_x + self.ball.speed_x)
        self.assertEqual(self.ball.y, initial_y + self.ball.speed_y)

    def test_wall_dimensions(self):
        self.assertEqual(len(self.wall.blocks), self.wall.rows)
        for row in self.wall.blocks:
            self.assertEqual(len(row), self.wall.cols)

    def test_paddle_initial_position(self):
        self.assertEqual(self.player_paddle.x, 100)
        self.assertEqual(self.player_paddle.y, 100)

    def test_ball_initial_position(self):
        expected_ball_x = self.player_paddle.x + (self.player_paddle.width // 2)
        expected_ball_y = self.player_paddle.y - self.player_paddle.height
        self.assertEqual(self.ball.x, expected_ball_x)
        self.assertEqual(self.ball.y, expected_ball_y)

    def tearDown(self):
        pygame.quit()

if __name__ == '__main__':
    unittest.main()
