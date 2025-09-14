import numpy as np
import time
import os
import math

theta_spacing = 0.07
phi_spacing = 0.02
illumination = np.fromiter(".,-~:;=!*#$@", dtype="<U1")

A = 1
B = 1
R1 = 1
R2 = 2
K2 = 5


def render_frame(A: float, B: float, screen_size: int) -> np.ndarray:
    """Returns a frame of the spinning 3D donut."""
    K1 = screen_size * K2 * 3 / (8 * (R1 + R2))

    cos_A = np.cos(A)
    sin_A = np.sin(A)
    cos_B = np.cos(B)
    sin_B = np.sin(B)

    output = np.full((screen_size, screen_size), " ")
    zbuffer = np.zeros((screen_size, screen_size))

    cos_phi = np.cos(phi := np.arange(0, 2 * np.pi, phi_spacing))
    sin_phi = np.sin(phi)
    cos_theta = np.cos(theta := np.arange(0, 2 * np.pi, theta_spacing))
    sin_theta = np.sin(theta)
    circle_x = R2 + R1 * cos_theta
    circle_y = R1 * sin_theta

    x = (np.outer(cos_B * cos_phi + sin_A * sin_B * sin_phi, circle_x) - circle_y * cos_A * sin_B).T
    y = (np.outer(sin_B * cos_phi - sin_A * cos_B * sin_phi, circle_x) + circle_y * cos_A * cos_B).T
    z = ((K2 + cos_A * np.outer(sin_phi, circle_x)) + circle_y * sin_A).T
    ooz = np.reciprocal(z)
    xp = (screen_size / 2 + K1 * ooz * x).astype(int)
    yp = (screen_size / 2 - K1 * ooz * y).astype(int)
    L1 = (((np.outer(cos_phi, cos_theta) * sin_B) - cos_A * np.outer(sin_phi, cos_theta)) - sin_A * sin_theta)
    L2 = cos_B * (cos_A * sin_theta - np.outer(sin_phi, cos_theta * sin_A))
    L = np.around(((L1 + L2) * 8)).astype(int).T
    mask_L = L >= 0
    chars = illumination[L]

    for i in range(len(x)):
        mask = mask_L[i] & (ooz[i] > zbuffer[xp[i], yp[i]])
        zbuffer[xp[i], yp[i]] = np.where(mask, ooz[i], zbuffer[xp[i], yp[i]])
        output[xp[i], yp[i]] = np.where(mask, chars[i], output[xp[i], yp[i]])

    return output


def pprint(array: np.ndarray) -> None:
    BLUE = "\033[34m"
    RESET = "\033[0m"
    print(*[BLUE + " ".join(row) + RESET for row in array], sep="\n")


if __name__ == "__main__":
    start_time = time.time()
    duration = 5  # seconds

    while time.time() - start_time < duration:
        # Angle rotation
        A += theta_spacing
        B += phi_spacing

        # Screen size pulsing (oscillates between 30 and 50)
        elapsed = time.time() - start_time
        screen_size = int(40 + 10 * math.sin(elapsed * 2))  # speed & range of pulsing

        pprint(render_frame(A, B, screen_size))

        # Only clear if not the last frame
        if time.time() - start_time < duration:
            time.sleep(0.05)
            os.system("cls" if os.name == "nt" else "clear")
