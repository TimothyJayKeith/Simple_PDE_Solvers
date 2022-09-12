import numpy as np

def Jacobi_Iter(init_matrix, num_iterations=1, print_iterations=False):
    old_matrix = init_matrix.copy()
    new_matrix = init_matrix.copy()

    if print_iterations:
        iteration_list = [old_matrix]

    for n in range(num_iterations):
        for i in range(1, len(old_matrix) - 1):
            for j in range(1, len(old_matrix[i]) - 1):
                new_matrix[i, j] = (1/4) * (old_matrix[i - 1, j] + old_matrix[i + 1, j] + old_matrix[i, j - 1] + old_matrix[i, j + 1])
        if print_iterations:
            iteration_list.append(new_matrix.copy())
        old_matrix = new_matrix.copy()

    if print_iterations:
        return iteration_list
    else:
        return new_matrix


def GS_Iter(init_matrix, num_iterations=1, print_iterations=False):
    iter_matrix = init_matrix.copy()

    if print_iterations:
        iteration_list = [iter_matrix.copy()]

    for n in range(num_iterations):
        for i in range(1, len(iter_matrix) - 1):
            for j in range(1, len(iter_matrix[i]) - 1):
                iter_matrix[i, j] = (1/4) * (iter_matrix[i - 1, j] + iter_matrix[i + 1, j] + iter_matrix[i, j - 1] + iter_matrix[i, j + 1])
        if print_iterations:
            iteration_list.append(iter_matrix.copy())

    if print_iterations:
        return iteration_list
    else:
        return iter_matrix


if __name__ == "__main__":
    example_matrix = np.zeros((4, 4))
    example_matrix[2, 3] = 24
    print(GS_Iter(example_matrix, num_iterations=4, print_iterations=True))