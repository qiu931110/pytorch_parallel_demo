import torch.nn as nn
import torch
from torch.utils.data import Dataset,DataLoader
from model import MYmodel
from dataset import RandomDataset


if __name__ == "__main__":
    # init parameters
    input_size = 5
    output_size = 2
    batch_size = 30
    data_size = 100

    # get dataloaders
    rand_loader = DataLoader(dataset=RandomDataset(input_size, data_size), batch_size=batch_size, shuffle=True)

    # get device
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

    # get model
    model = MYmodel(input_size, output_size)
    if torch.cuda.device_count() > 1:
        print("Let's use", torch.cuda.device_count(), "GPUs!")
        # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
        model = nn.DataParallel(model)
    else:
        print("Let's use cpu!")

    model.to(device)

    # print data fake train
    for data in rand_loader:
        input = data.to(device)
        output = model(input)
        print("Outside: input size", input.size(),
              "output_size", output.size())
