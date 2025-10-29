def plot_line_bresenham(x1, y1, x2, y2, grid_size=10):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    dx = x2 - x1
    dy = y2 - y1
    x, y = x1, y1
    p = 2 * dy - dx
    while x <= x2:
        if 0 <= x < grid_size and 0 <= y < grid_size:
            grid[grid_size - 1 - y][x] = 'X'
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * (dy - dx)
    print(f"Bresenham's Line from ({x1}, {y1}) to ({x2}, {y2}):\n")
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
    print(f"DDA Line from ({x1}, {y1}) to ({x2}, {y2}):\n")
    for row in grid:
        print(" ".join(row))


plot_line_bresenham(2, 2, 8, 6)
print("\n" + "-"*40 + "\n")
plot_line_dda(1, 7, 7, 3)

