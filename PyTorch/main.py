import torch
import numpy as np

if __name__ == "__main__":
    # 1. Tensor Initialization

    # 1.1. Directly from data
    data = [[1, 2], [3, 4]]
    x_data = torch.tensor(data)
    print("1.1. x_data -", x_data)

    # 1.2. From a NumPy array
    np_array = np.array(data)
    x_np = torch.from_numpy(np_array)
    print("1.2. x_np -", x_np)

    # 1.3. From another tensor
    x_ones = torch.ones_like(x_data)  # retains the properties of x_data
    print(f"1.3. Ones Tensor: \n {x_ones} \n")

    x_rand = torch.rand_like(x_data, dtype=torch.float)  # overrides the datatype of x_data
    print(f"1.3. Random Tensor: \n {x_rand} \n")

    # 1.4. With random or constant values
    shape = (2, 3,)
    rand_tensor = torch.rand(shape)
    ones_tensor = torch.ones(shape, dtype=torch.int8)
    zeros_tensor = torch.zeros(shape)

    print(f"1.4. Random Tensor: \n {rand_tensor} \n")
    print(f"1.4. Ones Tensor: \n {ones_tensor} \n")
    print(f"1.4. Zeros Tensor: \n {zeros_tensor} \n")

    # 2. Tensor Attributes
    tensor = torch.rand(3, 4)

    print(f"2. Shape of tensor: {tensor.shape}")
    print(f"2. Datatype of tensor: {tensor.dtype}")
    print(f"2. Device tensor is stored on: {tensor.device}")

    # 3. Tensor Operations

    # 3.1. We move our tensor to the GPU if available
    if torch.cuda.is_available():
        tensor = tensor.to('cuda')
        print(f"3.1. Device tensor is stored on: {tensor.device}")
    else:
        print(f"3.1. Torch CUDA is NOT available")

    # 3.2. Standard numpy-like indexing and slicing
    tensor = torch.ones(4, 4)
    tensor[:2, 1:3] = 0
    print("3.2. Indexing and slicing -\n", tensor)

    # 3.3. Joining tensors
    t1 = torch.cat([tensor, tensor, tensor], dim=1)
    print("3.3. Joining tensors -\n", t1)

    # 3.4. Multiplying tensors
    t1 = torch.tensor([
        [10, 20, 30],
        [40, 50, 60]
    ])
    t2 = torch.tensor([
        [2, 3, 4],
        [5, 6, 7]
    ])
    # This computes the element-wise product
    print(f"3.4. tensor.mul(tensor) \n {t1.mul(t2)} \n")
    # Alternative syntax:
    print(f"3.4. tensor * tensor \n {t1 * t2}")

    # 3.5. matrix multiplication tensors
    t3 = torch.tensor([
        [10.5, 20.25, 30.75],
        [40.25, 50.75, 60.5]
    ])
    t4 = torch.tensor([
        [2.47, 3.35],
        [4.93, 5.18],
        [6.28, 7.69]
    ])

    print(f"3.5. tensor.matmul(tensor.T) \n {t3.matmul(t4)} \n")
    # Alternative syntax:
    print(f"3.5. tensor @ tensor.T \n {t3 @ t4}")

    print(f"tensor.matmul(tensor.T) \n {tensor.matmul(tensor.T)} \n")
    # Alternative syntax:
    print(f"tensor @ tensor.T \n {tensor @ tensor.T}")

    # 3.6. In-place operations
