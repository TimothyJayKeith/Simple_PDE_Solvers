import numpy as np

x_square = lambda a: a**2

def Wave(Delta_t, Delta_x, t_range = (0, 1), x_range = (0, 1), c=1, init_pos=lambda a:1, init_vel=lambda a:1):
    x_steps = int((x_range[1] - x_range[0])/Delta_x) + 1
    t_steps = int((t_range[1] - t_range[0])/Delta_t) + 1
    s = (c *Delta_x/Delta_t)**2
    iter_matrix = np.zeros((t_steps, x_steps))

    for n in range(t_steps):
        for j in range(n, x_steps - n):
            if n == 0:
                iter_matrix[n, j] = init_pos(j*Delta_x + x_range[0])
            if n == 1:
                iter_matrix[n, j] = (s/2)*(init_pos((j + 1)*Delta_x + x_range[0]) + init_pos((j - 1)*Delta_x + x_range[0])) + (1 - s)*init_pos(j*Delta_x + x_range[0]) + init_vel(j*Delta_x + x_range[0])*Delta_t
            if n > 1:
                iter_matrix[n, j] = 2*(1 - s)*iter_matrix[n - 1, j] + s*(iter_matrix[n - 1, j + 1] + iter_matrix[n - 1, j - 1]) - iter_matrix[n - 2, j]
    return(iter_matrix)

if __name__ == "__main__":
    print(Wave(.2, .2, x_range=(-2, 2), init_pos=x_square))

    exact_matrix = np.zeros((6, 21))
    for n in range(6):
        for j in range(n, 21 - n):
            exact_matrix[n, j] = (.2*j - 2)**2 + (.2*n)**2 + .2*n
    print(exact_matrix)
