import torch
import torch.nn as nn
import torch.nn.functional as F

class Softmax(nn.Module):
    def __init__(self):
        super(Softmax, self).__init__()
    
    def forward(self, x):
        # Compute softmax
        exp_x = torch.exp(x)
        sum_exp_x = torch.sum(exp_x)
        softmax_output = exp_x / sum_exp_x
        return softmax_output

class SoftmaxStable(nn.Module):
    def __init__(self):
        super(SoftmaxStable, self).__init__()
    
    def forward(self, x):
        # Compute softmax in a numerically stable way
        max_x = torch.max(x)
        exp_x = torch.exp(x - max_x)
        sum_exp_x = torch.sum(exp_x)
        softmax_output = exp_x / sum_exp_x
        return softmax_output

# Example usage:
if __name__ == "__main__":
    input_tensor = torch.tensor([1.0, 2.0, 3.0])

    # Using the Softmax class
    softmax = Softmax()
    output = softmax(input_tensor)
    print("Softmax output:", output)

    # Using the SoftmaxStable class
    softmax_stable = SoftmaxStable()
    output_stable = softmax_stable(input_tensor)
    print("SoftmaxStable output:", output_stable)
