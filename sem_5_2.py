def plot_line_bresenham(x1, y1, x2, y2, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        if 0 <= x1 < grid_size and 0 <= y1 < grid_size:
            grid[grid_size - 1 - y1][x1] = 'X'
        if x1 == x2 and y1 == y2:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

    print("Bresenham's Line from (2, 2) to (8, 6):\n")
    for row in grid:
        print(" ".join(row))


def plot_line_dda(x1, y1, x2, y2, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

    dx = x2 - x1
    dy = y2 - y1
    steps = max(abs(dx), abs(dy))
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    for _ in range(steps + 1):
        xi = int(round(x))
        yi = int(round(y))
        if 0 <= xi < grid_size and 0 <= yi < grid_size:
            grid[grid_size - 1 - yi][xi] = 'X'
        x += x_inc
        y += y_inc

    print("DDA Line from (1, 7) to (7, 3):\n")
    for row in grid:
        print(" ".join(row))


# Draw different lines
plot_line_bresenham(2, 2, 8, 6)
print("\n" + "-"*40 + "\n")
plot_line_dda(1, 7, 7, 3)
