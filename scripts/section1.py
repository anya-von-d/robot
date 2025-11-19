#!/usr/bin/env python3
print("hello world")
import numpy as np
# add import and helper functions here

if __name__ == "__main__":
    print("Hello from section1.py!")

    np.random.seed(42)
    A = np.random.normal(size=(4, 4))
    B = np.random.normal(size=(4, 2))

    C = A @ B

    print(C)

    np.random.seed(42)
    x = np.random.normal(size=(4, 10))
    diff = x[:, None, :] - x[None, :, :]
    D = np.sum(diff**2, axis=2)

    print(D)