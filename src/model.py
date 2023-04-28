import torch
import torch.nn as nn
import torch.nn.functional as F
# import torch.optim as optim
# import matplotlib.pyplot as plt
# import seaborn as sns


class BasicNN(nn.Module):
    def __init__(self):
        super.__init__()
        self.w00 = nn.Parameter(torch.tensor(1.7), requires_grad=True)
        self.b00 = nn.Parameter(torch.tensor(0.8), requires_grad=True)

        self.w01 = nn.Parameter(torch.tensor(0.8), requires_grad=True)

        self.w10 = nn.Parameter(torch.tensor(0.8), requires_grad=True)
        self.b10 = nn.Parameter(torch.tensor(0.8), requires_grad=True)

        self.w11 = nn.Parameter(torch.tensor(0.8), requires_grad=True)

        self.final_bias = nn.Parameter(torch.tensor(0.8), requires_grad=True)

    def forward(self, input):
        input_to_top_relu = input*self.w00 + self.b00
        top_relu_output = F.relu(input_to_top_relu)
        scaled_top_relu_output = top_relu_output * self.w01

        input_to_bottom_relu = input*self.w10 + self.b10
        bottom_relu_output = F.relu(input_to_bottom_relu)
        scaled_bottom_relu_output = bottom_relu_output * self.w11

        input_to_final_relu = scaled_top_relu_output + scaled_bottom_relu_output + self.final_bias
        output = F.relu(input_to_final_relu)

        return output
