# penal-connection
The source code of penal connection, which was first proposed in [Rethinking skip connection model as a learnable Markov chain](https://arxiv.org/pdf/2209.15278.pdf).

## Install

```bash
git clone https://github.com/densechen/penal-connection.git
pip install -e .
```

## Usage

```python
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


```

```bash
(base) % python test.py 
Net(
  (fc_1): Linear(in_features=1, out_features=4, bias=True)
  (fc_2): Sequential(
    (0): Linear(in_features=4, out_features=4, bias=True)
    (1): PenalConnection(tau=0.0001)
  )
  (fc_3): Linear(in_features=4, out_features=4, bias=True)
  (fc_4): Linear(in_features=4, out_features=1, bias=True)
)
```

## Cite

```
@misc{2209.15278,
Author = {Dengsheng Chen and Jie Hu and Wenwen Qiang and Xiaoming Wei and Enhua Wu},
Title = {Rethinking skip connection model as a learnable Markov chain},
Year = {2022},
Eprint = {arXiv:2209.15278},
}
```
