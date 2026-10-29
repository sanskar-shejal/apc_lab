import numpy as np


def main():
    try:
        a1 = np.array([1, 2, 3, 4])
        print("1D Array:\n", a1)
        print("Shape:", a1.shape, "| Dimensions:", a1.ndim)

        b2 = np.array([[1, 2], [3, 4]])
        print("\n2D Array:\n", b2)
        print("Shape:", b2.shape, "| Dimensions:", b2.ndim)

        c3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
        print("\n3D Array:\n", c3)
        print("Shape:", c3.shape, "| Dimensions:", c3.ndim)

        print("\nTranspose of 2D Array b2:\n", b2.T)

        m1 = np.array([[1, 2], [3, 4]])
        m2 = np.array([[5, 6], [7, 8]])

        print("\nMatrix 1:\n", m1)
        print("Matrix 2:\n", m2)
        print("\nMatrix Addition (m1 + m2):\n", m1 + m2)
        print("Matrix Subtraction (m1 - m2):\n", m1 - m2)
        print("Element-wise Multiplication (m1 * m2):\n", m1 * m2)
        print("Matrix Dot Product (m1 @ m2):\n", np.dot(m1, m2))
        print("Matrix Division (m1 / m2):\n", m1 / m2)

        print("\nExponential of 1D Array np.exp(a1):\n", np.exp(a1))

        nums = np.array([10, 20, 30, 40, 50])
        print("\nStatistical Operations on array:", nums)
        print("Sum:", np.sum(nums))
        print("Average (Mean):", np.mean(nums))
        print("Standard Deviation:", np.std(nums))
        print("Maximum Value:", np.max(nums))
        print("Minimum Value:", np.min(nums))
        print("Index of Max (argmax):", np.argmax(nums))

    except ImportError:
        print("NumPy is not installed. Run 'pip install numpy' to test this section.")


if __name__ == "__main__":
    main()
