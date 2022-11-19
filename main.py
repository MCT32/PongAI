import pygame


def main():
    pygame.init()

    pygame.display.set_caption("PongAI")

    screen = pygame.display.set_mode((600, 600))

    running = True

    paddle = Paddle()
    ball = Ball()

    while running:
        if ball.update(paddle):
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return

            if event.type == pygame.MOUSEMOTION:
                paddle.pos = event.pos[1] - paddle.width / 2
                paddle.clamp()

        screen.fill((0, 0, 0))
        paddle.draw(screen)
        ball.draw(screen)

        pygame.display.flip()


class Paddle:
    pos = 0
    width = 300

    def move(self, amount):
        self.pos += amount
        self.clamp()

    def clamp(self):
        if (self.pos < 0):
            self.pos = 0

        if (self.pos > 600 - self.width):
            self.pos = 600 - self.width

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (0, self.pos, 5, self.width))


class Ball:
    pos = [600, 300]
    vel = [-4, -5]
    radius = 5

    max_bounce_vel = 10

    def update(self, paddle):
        self.pos[0] = self.pos[0] + self.vel[0] / 60
        self.pos[1] = self.pos[1] + self.vel[1] / 60

        if self.pos[0] < 0:
            if self.pos[1] > paddle.pos and self.pos[1] < paddle.pos + paddle.width:
                hit = (self.pos[1] - paddle.pos) / paddle.width * 2 - 1
                self.vel[1] = self.max_bounce_vel * hit

                self.pos[0] = 0
                self.vel[0] = -self.vel[0]
            else:
                return True

        if self.pos[0] > 600:
            self.pos[0] = 600
            self.vel[0] = -self.vel[0]
        if self.pos[1] < 0:
            self.pos[1] = 0
            self.vel[1] = -self.vel[1]
        if self.pos[1] > 600:
            self.pos[1] = 600
            self.vel[1] = -self.vel[1]

        return False

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), tuple(self.pos), self.radius)


if __name__ == "__main__":
    main()
