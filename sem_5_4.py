import math

# ---------- Helper Function ----------
def display_points(points, title):
    print(f"\n{title}")
    for i in range(len(points)):
        print(f"Point {i+1}: {points[i]}")

# ---------- 2D Transformations ----------
def translate_2d(points, tx, ty):
    return [(x + tx, y + ty) for x, y in points]

def scale_2d(points, sx, sy):
    return [(x * sx, y * sy) for x, y in points]

def rotate_2d(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    return [(x * cos_a - y * sin_a, x * sin_a + y * cos_a) for x, y in points]

def shear_2d(points, shx, shy):
    result = []
    for x, y in points:
        x_new = x + shx * y
        y_new = y + shy * x
        result.append((x_new, y_new))
    return result

# ---------- 3D Transformations ----------
def translate_3d(points, tx, ty, tz):
    return [(x + tx, y + ty, z + tz) for x, y, z in points]

def scale_3d(points, sx, sy, sz):
    return [(x * sx, y * sy, z * sz) for x, y, z in points]

def rotate_3d_x(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    result = []
    for x, y, z in points:
        y_new = y * cos_a - z * sin_a
        z_new = y * sin_a + z * cos_a
        result.append((x, y_new, z_new))
    return result

def rotate_3d_y(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    result = []
    for x, y, z in points:
        x_new = x * cos_a + z * sin_a
        z_new = -x * sin_a + z * cos_a
        result.append((x_new, y, z_new))
    return result

def rotate_3d_z(points, angle_deg):
    angle_rad = math.radians(angle_deg)
    cos_a = math.cos(angle_rad)
    sin_a = math.sin(angle_rad)
    result = []
    for x, y, z in points:
        x_new = x * cos_a - y * sin_a
        y_new = x * sin_a + y * cos_a
        result.append((x_new, y_new, z))
    return result

def shear_3d(points, shxy=0, shxz=0, shyx=0, shyz=0, shzx=0, shzy=0):
    result = []
    for x, y, z in points:
        x_new = x + shxy * y + shxz * z
        y_new = y + shyx * x + shyz * z
        z_new = z + shzx * x + shzy * y
        result.append((x_new, y_new, z_new))
    return result

# ---------- Main Program ----------
if __name__ == "__main__":
    # ===== 2D Transformation =====
    print("==== 2D TRANSFORMATIONS ====")
    points_2d = [(0, 0), (2, 0), (1, 2)]
    display_points(points_2d, "Original 2D Points")

    translated_2d = translate_2d(points_2d, 3, 2)
    display_points(translated_2d, "After Translation (tx=3, ty=2)")

    scaled_2d = scale_2d(points_2d, 2, 1.5)
    display_points(scaled_2d, "After Scaling (sx=2, sy=1.5)")

    rotated_2d = rotate_2d(points_2d, 45)
    display_points(rotated_2d, "After Rotation (45°)")

    sheared_2d = shear_2d(points_2d, shx=0.5, shy=0.2)
    display_points(sheared_2d, "After Shearing (shx=0.5, shy=0.2)")

    # ===== 3D Transformation =====
    print("\n==== 3D TRANSFORMATIONS ====")
    points_3d = [(1, 1, 1), (2, 1, 1), (1, 2, 1), (1, 1, 2)]
    display_points(points_3d, "Original 3D Points")

    translated_3d = translate_3d(points_3d, 2, 3, 4)
    display_points(translated_3d, "After Translation (tx=2, ty=3, tz=4)")

    scaled_3d = scale_3d(points_3d, 2, 0.5, 1.5)
    display_points(scaled_3d, "After Scaling (sx=2, sy=0.5, sz=1.5)")

    rotated_x = rotate_3d_x(points_3d, 45)
    display_points(rotated_x, "After Rotation about X-axis (45°)")

    rotated_y = rotate_3d_y(points_3d, 45)
    display_points(rotated_y, "After Rotation about Y-axis (45°)")

    rotated_z = rotate_3d_z(points_3d, 45)
    display_points(rotated_z, "After Rotation about Z-axis (45°)")

    sheared_3d = shear_3d(points_3d, shxy=0.3, shyz=0.2, shzx=0.4)
    display_points(sheared_3d, "After Shearing (shxy=0.3, shyz=0.2, shzx=0.4)")

