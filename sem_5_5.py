import matplotlib.pyplot as plt

# Clipping window boundaries
X_MIN, Y_MIN = 0, 0
X_MAX, Y_MAX = 10, 10

# Region codes
INSIDE, LEFT, RIGHT, BOTTOM, TOP = 0, 1, 2, 4, 8

# Compute region code
def compute_code(x, y):
    code = INSIDE
    if x < X_MIN: code |= LEFT
    elif x > X_MAX: code |= RIGHT
    if y < Y_MIN: code |= BOTTOM
    elif y > Y_MAX: code |= TOP
    return code

# Cohen–Sutherland algorithm
def cohen_sutherland_line_clip(x1, y1, x2, y2):
    code1, code2 = compute_code(x1, y1), compute_code(x2, y2)
    while True:
        if code1 == 0 and code2 == 0:      # Both inside
            return (x1, y1, x2, y2)
        elif (code1 & code2) != 0:         # Both outside same region
            return None
        else:
            code_out = code1 if code1 != 0 else code2
            if code_out & TOP:
                x = x1 + (x2 - x1) * (Y_MAX - y1) / (y2 - y1)
                y = Y_MAX
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (Y_MIN - y1) / (y2 - y1)
                y = Y_MIN
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (X_MAX - x1) / (x2 - x1)
                x = X_MAX
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (X_MIN - x1) / (x2 - x1)
                x = X_MIN

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

# Draw window and lines
def draw(x1, y1, x2, y2):
    plt.plot([X_MIN, X_MAX, X_MAX, X_MIN, X_MIN],
             [Y_MIN, Y_MIN, Y_MAX, Y_MAX, Y_MIN], 'k-')  # Window
    plt.plot([x1, x2], [y1, y2], 'b--')  # Original line
    res = cohen_sutherland_line_clip(x1, y1, x2, y2)
    if res:
        plt.plot([res[0], res[2]], [res[1], res[3]], 'r-', lw=2)
    plt.axis([-2, 12, -2, 12])
    plt.grid(True)
    plt.show()

# Example
draw(2, 3, 12, 5)
