import array
arr = array.array('i', [10, 20, 30, 40, 50])

print("Array:", arr)
print("First element:", arr[0])


import array
arr = array.array('i', [5, 10, 15, 20, 25, 30])
print("Array:", arr)
print("Last element:", arr[-1])


import array
arr = array.array('i', [100, 200, 300, 400, 500])

print(arr[2])


import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[1][1])


import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])

print(arr[2][2])


import numpy as np

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr[1][0][1])


import numpy as np

arr = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(arr[0][1][0])


import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])

print(arr[:4])


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[2:6])


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[4:])


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[::2])


import numpy as np
arr = np.array([10, 20, 30, 40, 50, 60, 70, 80])
print(arr[-3:])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[0])


import numpy as np

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[2])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:, 1])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:, 2])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:2])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:, :2])


import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print(arr[:2, :2])


import numpy as np
arr = np.array([10, 20, 30, 40, 50])
print(arr)


