
from matplotlib import pyplot as plt
import numpy as np

# vars
G = 32.2

# table dims
Tl = 8
Tw = 4
Th = 4

# table points (@ z = 4)
x1 = 2
x2 = x1 + Tw
y1 = 2
y2 = y1 + Tl


def getTable():
    x = range(x1, x2+1)
    y = range(y1, y2+1)
    xs, ys = np.meshgrid(x, y)
    zs = np.array([[Th] * len(x)] * len(y))
    return xs, ys, zs


def getToss(toss_v, toss_fromVert, toss_fromX, toss_x, toss_y, n=50):
    Vx = toss_v * np.sin(np.radians(toss_fromVert)) * np.cos(np.radians(toss_fromX))
    Vy = toss_v * np.sin(np.radians(toss_fromVert)) * np.sin(np.radians(toss_fromX))
    Vz = toss_v * np.cos(np.radians(toss_fromVert)) * np.cos(np.radians(toss_fromX))
    
    xs, ys, zs = [], [], []
    for t in np.linspace(0, 8, n):
        x = toss_x + Vx * t
        y = toss_y + Vy * t
        z = Th + Vz * t - 1/6 * G * t**3

        if z < -Th:
            break
        else:
            xs.append(x)
            ys.append(y)
            zs.append(z)

    return xs, ys, zs


if __name__ == "__main__":
    numTosses = 100
    toss_loc = (0, 1)
    print(f"tossing {numTosses} dye...")


    # DATA
    Tx, Ty, Tz = getTable()
    tosses_x, tosses_y, tosses_z = [], [], []
    for _ in range(numTosses):
        fromVert = np.random.randint(10, 15)
        fromX = np.random.randint(20, 30)
        tossV = np.random.randint(20, 25)

        tx, ty, tz = getToss(tossV, fromVert, fromX, toss_loc[0], toss_loc[1])
        tosses_x.append(tx)
        tosses_y.append(ty)
        tosses_z.append(tz)


    # PLOTTING
    fig = plt.figure(figsize=(8, 6))
    ax = fig.add_subplot(111, projection='3d')

    # table
    ax.plot_surface(Ty, Tx, Tz, alpha=0.8)
    
    # tosses
    for i in range(numTosses):
        ax.plot(tosses_x[i], tosses_y[i], tosses_z[i])

    plt.xlim([0, y1+y2])
    plt.ylim([0, x1+x2])
    
    fs = 14
    ax.set_xlabel("$X$", fontsize=fs)
    ax.set_ylabel("$Y$", fontsize=fs)
    ax.set_zlabel("$Z$", fontsize=fs)

    plt.show()
