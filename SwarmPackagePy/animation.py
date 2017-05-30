from matplotlib import pyplot as plt
import matplotlib.animation
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd


def animation(agents, function, lb, ub, sr=False):

    side = np.linspace(lb, ub, (ub - lb) * 5)
    X, Y = np.meshgrid(side, side)
    Z = np.array([np.array([function([X[i][j], Y[i][j]])
                            for j in range(len(X))])
                  for i in range(len(X[0]))])

    fig = plt.figure()
    plt.axes(xlim=(lb, ub), ylim=(lb, ub))
    plt.pcolormesh(X, Y, Z, shading='gouraud')
    plt.colorbar()

    x = np.array([j[0] for j in agents[0]])
    y = np.array([j[1] for j in agents[0]])
    sc = plt.scatter(x, y, color='black')

    plt.title(function.__name__, loc='left')

    def an(i):
        x = np.array([j[0] for j in agents[i]])
        y = np.array([j[1] for j in agents[i]])
        sc.set_offsets(list(zip(x, y)))
        plt.title('iteration: {}'.format(i), loc='right')

    ani = matplotlib.animation.FuncAnimation(fig, an, frames=len(agents) - 1)

    if sr:

        ani.save('result.mp4')

    plt.show()


def animation3D(agents, function, lb, ub, sr=False):

    side = np.linspace(lb, ub, 45)
    X, Y = np.meshgrid(side, side)
    zs = np.array([function([x, y]) for x, y in zip(np.ravel(X), np.ravel(Y))])
    Z = zs.reshape(X.shape)

    fig = plt.figure()

    ax = Axes3D(fig)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='jet',
                           linewidth=0, antialiased=False)
    ax.set_xlim(lb, ub)
    ax.set_ylim(lb, ub)

    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    iter = len(agents)
    n = len(agents[0])
    t = np.array([np.ones(n) * i for i in range(iter)]).flatten()
    b = []
    [[b.append(agent) for agent in epoch] for epoch in agents]
    c = [function(x) for x in b]
    a = np.asarray(b)
    df = pd.DataFrame({"time": t, "x": a[:, 0], "y": a[:, 1], "z": c})

    def update_graph(num):
        data = df[df['time'] == num]
        graph._offsets3d = (data.x, data.y, data.z)
        title.set_text(function.__name__ + " " * 45 + 'iteration: {}'.format(
            num))

    title = ax.set_title(function.__name__ + " " * 45 + 'iteration: 0')

    data = df[df['time'] == 0]
    graph = ax.scatter(data.x, data.y, data.z, color='black')

    ani = matplotlib.animation.FuncAnimation(fig, update_graph, iter,
                                             interval=50, blit=False)

    if sr:

        ani.save('result.mp4')

    plt.show()
