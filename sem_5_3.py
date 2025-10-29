def plot_circle_points(grid, xc, yc, x, y, grid_size):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        if 0 <= px < grid_size and 0 <= py < grid_size:
            grid[py][px] = 'X'  # Note: row = y, col = x


def plot_circle_bresenham(xc, yc, r, grid_size=20):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    x, y = 0, r
    p = 3 - 2 * r

    while x <= y:
        plot_circle_points(grid, xc, yc, x, y, grid_size)
        if p < 0:
            p += 4 * x + 6
        else:
            y -= 1
            p += 4 * (x - y) + 10
        x += 1

    return grid


def plot_circle_midpoint(xc, yc, r, grid_size=20):
    grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]
    x, y = 0, r
    p = 1 - r

    while x <= y:
        plot_circle_points(grid, xc, yc, x, y, grid_size)
        if p < 0:
            p += 2 * x + 3
        else:
            y -= 1
            p += 2 * (x - y) + 5
        x += 1

    return grid


def print_grid(grid, title):
    print(f"\n{title}")
    for row in reversed(grid):  # Reverse to show origin (0,0) at bottom-left
        print(" ".join(row))


def draw_circle(center, radius, grid_size=20):
    xc, yc = center
    print(f"Center: ({xc}, {yc}) | Radius: {radius} | Grid: {grid_size}x{grid_size}")

    # Bresenham
    grid_bresenham = plot_circle_bresenham(xc, yc, radius, grid_size)
    print_grid(grid_bresenham, "Bresenham's Circle Drawing")

    print("\n" + "-" * 40)

    # Midpoint
    grid_midpoint = plot_circle_midpoint(xc, yc, radius, grid_size)
    print_grid(grid_midpoint, "Mid-Point Circle Drawing")

    print("\n" + "-" * 40 + "\n")


# Example usage
draw_circle(center=(10, 10), radius=6, grid_size=21)
