import torch.nn as nn


def penal_connection(z, tau=3e-4):
    """Register a penal connection function if z requires grad.
    """
    if z.requires_grad:
        z.register_hook(lambda grad, z=z.detach().clone(): grad + tau * z)
    return z


class PenalConnection(nn.Module):
    """More friendly for exporting onnx.
    """

    def __init__(self, tau=3e-4):
        super(PenalConnection, self).__init__()

        self.tau = tau

    def forward(self, z):
        if self.training:
            return penal_connection(z, self.tau)
        else:
            return z

    def __repr__(self):
        return f"{self.__class__.__name__}(tau={self.tau})"
