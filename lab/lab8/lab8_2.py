# def read_matrix():
#     """
#     Read number of rows and columns of a matrix.
#     Then, read each element and store it in a matrix.
#     Return the read-in matrix
#     :params Nothing
#     :return 2D-list contains the matrix
#     """
#     row = int(input('Input #rows? '))
#     col = int(input('Input #columns? '))
#     matrix = []
#     for i in range(row):
#         see = []
#         for j in range(col):
#             ele = int(input(f'Input element[{i + 1}][{j + 1}]: '))
#             see.append(ele)
#         matrix.append(see)
#     return matrix
#
#
# def print_matrix(matrix):
#     """
#     Display a matrix, where each number is displayed in 5 spaces and right-aligned.
#     :params a 2D-list contains a matrix
#     :return Nothing
#     """
#     for i in range(len(matrix)):
#         for j in matrix[i]:
#             print(f'{j:>5}', end='')
#         print()
#
#
# def print_row(matrix):
#     """
#     Print specific row from a matrix
#     :params 2D-list contains an original matrix
#     :return Nothing
#     """
#     n = int(input('Input row number: '))
#     for i in matrix[n - 1]:
#         print(f'{i:>5}', end='')
#     print()
#
#
# def print_column(matrix):
#     """
#     Print specific column from a matrix
#     :params 2D-list contains an original matrix
#     :return Nothing
#     """
#     n = int(input('Input column number: '))
#     for i in range(len(matrix)):
#         print(f'{matrix[i][n - 1]:>5}', end='')
#     print()
#
#
# n = int(input('Input n: '))
# matrix = []
# for i in range(n):
#     see = []
#     for j in range(n):
#         ele = int(input(f'Input element[{i + 1}][{j + 1}]: '))
#         see.append(ele)
#     matrix.append(see)
# sum_up_to_down = 0
# sum_down_to_up = 0
# j = 0
# for i in range(len(matrix[0])):
#     sum_down_to_up += matrix[::-1][i][j]
#     sum_up_to_down += matrix[i][j]
#     j += 1
# print(f'Sum of its diagonal elements '
#       f'(top-left to bottom-right) is {sum_up_to_down}')
# print(f'Sum of its diagonal elements '
#       f'(top-right to bottom-left) is {sum_down_to_up}')
#
#
# def transpose_matrix(matrix):
#     """
#     Transpose a matrix
#     :params 2D-list contains an original matrix
#     :return another 2D-list contains the transpose of original matrix
#
#     >>> print_matrix(transpose_matrix([[1,2],[3,4]]))
#         1    3
#         2    4
#     >>> print_matrix(transpose_matrix([[5,6,7],[8,9,10]]))
#         5    8
#         6    9
#         7   10
#     """
#     new_matrix = []
#     for i in range(len(matrix[0])):
#         col = []
#         for j in range(len(matrix)):
#             col.append(matrix[j][i])
#         new_matrix.append(col)
#     return new_matrix
#
#
# matrix = read_matrix()
# print("Matrix A is")
# print_matrix(matrix)
# print("Transpose of Matrix A is")
# print_matrix(transpose_matrix(matrix))

def average(score):
    return [int(score[i][0])*0.3 + int(score[i][1])*0.3 + int(score[i][2])*0.4 for i in range(len(score))]
    # average_score = []
    # for i in range(len(score)):
    #     result = 0
    #     for j in range(3):
    #         if j == 2:
    #             result += int(score[i][j])*0.4
    #         else:
    #             result += int(score[i][j])*0.3
    #     average_score.append(result)
    # return average_score


def convert_to_grade(score):
    if 0 <= score < 50:
        grade = 'F'
    elif score < 60:
        grade = 'D'
    elif score < 70:
        grade = 'C'
    elif score < 80:
        grade = 'B'
    else:
        grade = 'A'
    return grade


def read_one_student(index):
    print(f'Please input score of student{index}.')
    score = [int(input(f'Test{i+1} : ')) for i in range(3)]
    return score


def read_multiple_students(num_students):
    score = [read_one_student(i+1) for i in range(num_students)]
    return score


num_students = int(input('Numbers of students : '))
all_score = read_multiple_students(num_students)
avg_score = average(all_score)
for i in range(num_students):
    print(f'Average score of Student{i+1} is {avg_score[i]:.1f}, Grade {convert_to_grade(avg_score[i])}.')