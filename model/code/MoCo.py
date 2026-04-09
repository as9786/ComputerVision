# Library
import torch
from torch import nn
from torch.nn import functional as F
from torchvision import models

class MoCo(nn.Module):

    def __init__(self, encoder, dim=128, K=65536, m=0.999, T=0.07):
        '''
        dim : Feature dimension
        k : Query size
        m : Momentum coefficient
        T : Temperature
        '''

        super().__init__()
        self.K = K
        self.m = m
        self.T = T

        # Query encoder
        self.encoder_q = encoder(num_classes=dim)
        # Key encoder
        self.encoder_k = encoder(num_classes=dim)

        # Key encoder는 query encoder의 초기값
        for param_q, param_k in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            param_k.data.copy_(para_q.data)
            param_k.requires_grad = False # Key encoder doesn't need gradients
        
        # Queue : [dim, K]
        self.register_buffer('queue', torch.randn(dim, K))
        self.queue = F.normalize(self.queue, dim=0)

        # Queue pointer
        self.register_buffer('queue_ptr', torch.zeros(1, dtype=torch.long))

    @torch.no_grad()
    def momentum_update_key_encoder(self):
        for param_q, param_k in zip(self.encoder_q.parameters(), self.encoder_k.parameters()):
            param_k.data = param_k.data * self.m + param_q.data * (1 - self.m)

    @torch.no_grad()
    def dequeue_and_enqueue(self, keys):
        batch_size = keys.shape[0]
        ptr = int(self.queue_ptr)

        self.queue[:, ptr:ptr+batch_size] = keys.T
        ptr = (ptr + batch_size) % self.K
        self.queue_ptr[0] = ptr

    def forward(self, im_q, im_k):

        q = self.encoder_q(im_q)
        q = F.normalize(q, dim=1)

        with torch.no_grad():
            self.momentum_update_key_encoder()
            k = self.encoder_k(im_k)
            k = F.normalize(k, dim=1)

        l_pos = torch.einsum('nc,nc->n', [q,k]).unsqueeze(-1)
        l_neg = torch.einsum('nc,ck->nk', [q, self.queue.clone().detach()])
        logits = torch.cat([l_pos, l_neg], dim=1)
        logits /= self.T
        labels = torch.zeros(logits.shape[0], dtype=torch.long, device=logits.device)

        self.dequeue_and_enqueue(k)

        return logits, labels
