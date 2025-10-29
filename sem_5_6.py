import pygame, sys

pygame.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quadratic Bézier Curve (3 points)")

WHITE = (255, 255, 255)
RED = (255,   0,   0)
BLUE = (0,   0, 255)

# Three control points: start, control, end
points = [(100, 300), (300, 50), (500, 300)]
drag = None

def bezier_quad(p0, p1, p2, t):
    """Return (x, y) for quadratic Bezier at parameter t."""
    u = 1 - t
    # Quadratic Bézier formula: (1-u)^2 P0 + 2u(1-u) P1 + u^2 P2
    x = u * u * p0[0] + 2 * u * t * p1[0] + t * t * p2[0]
    y = u * u * p0[1] + 2 * u * t * p1[1] + t * t * p2[1]
    return int(x), int(y)

def draw():
    screen.fill(WHITE)
    # Draw control polygon (lines connecting the points)
    pygame.draw.lines(screen, RED, False, points, 2)
    # Draw control points
    for p in points:
        pygame.draw.circle(screen, RED, p, 6)
    # Draw the Bézier curve by sampling many points
    for i in range(101):
        t = i / 100
        pygame.draw.circle(screen, BLUE, bezier_quad(points[0], points[1], points[2], t), 2)
    pygame.display.flip()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            for i, p in enumerate(points):
                if abs(e.pos[0] - p[0]) < 8 and abs(e.pos[1] - p[1]) < 8:
                    drag = i
        if e.type == pygame.MOUSEBUTTONUP:
            drag = None
        if e.type == pygame.MOUSEMOTION and drag is not None:
            points[drag] = e.pos

    draw()
