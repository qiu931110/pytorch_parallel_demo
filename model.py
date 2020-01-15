import torch.nn as nn
class MYmodel(nn.Module):
    # Our model

    def __init__(self, input_size, output_size):
        super(MYmodel, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, input):
        output = self.fc(input)
        print("\tIn Model: input size", input.size(),
              "output size", output.size())

        return output