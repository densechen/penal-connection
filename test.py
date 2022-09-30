import penal_connection as pc

import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc_1 = nn.Linear(1, 4)
        
        # use as a layer
        self.fc_2 = nn.Sequential(
            nn.Linear(4, 4),
            pc.PenalConnection(tau=1e-4),
        )

        self.fc_3 = nn.Linear(4, 4)

        self.fc_4 = nn.Linear(4, 1)
    
    def forward(self, x):
        fc_1 = self.fc_1(x)

        fc_2 = fc_1 + self.fc_2(fc_1)

        # use as a function
        fc_3 = fc_2 + pc.penal_connection(self.fc_3(fc_2), tau=1e-4)

        return self.fc_4(fc_3)

print(Net())
