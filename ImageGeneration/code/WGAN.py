# Library
import torch
from torch import nn
from torch import optim
from torch.autograd import Variable

# 생성기
class Generator(nn.Module):

    def __init__(self, channels):
        super().__init__()
        # Z latent vector
        self.conv1 = nn.ConvTranspose2d(in_channels=100, out_channels=1024, kernel_size=4, stride=1, padding=0)
        self.conv2 = nn.ConvTranspose2d(in_channels=1024, out_channels=512, kernel_size=4, stride=2, padding=1)
        self.conv3 = nn.ConvTranspose2d(in_channels=512, out_channels=256, kernel_size=4, stride=2, padding=1)
        self.conv4 = nn.ConvTranspose2d(in_channels=256, out_channels=channels, kernel_size=4, stride=2, padding=1)

        self.bn1 = nn.BatchNorm2d(1024)
        self.bn2 = nn.BatchNorm2d(512)
        self.bn3 = nn.BatchNorm2d(256)

        self.relu = nn.ReLU(True)
        self.tanh = nn.Tanh()
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu(x)
        x = self.conv4(x)
        out = self.tanh(x)
        return out

# 판별기
class Discriminator(nn.Module):

    def __init__(self, channels):
        super().__init__()
        self.conv1 = nn.Conv2d(in_channels=channels, out_channels=256, kernel_size=4, stride=2, padding=1)
        self.conv2 = nn.Conv2d(in_channels=256, out_channels=512, kernel_size=4, stride=2, padding=1)
        self.conv3 = nn.Conv2d(in_channels=512, out_channels=1024, kernel_size=4, stride=2, padding=1)
        self.conv4 = nn.Conv2d(in_channels=1024, out_channels=1, kernel_size=4, stride=1, padding=0)

        self.bn1 = nn.BatchNorm2d(512)
        self.bn2 = nn.BatchNorm2d(1024)

        self.leaky_relu = nn.LeakyReLU(0.2, inplace=True)

    def forward(self, x):
        x = self.conv1(x)
        x = self.leaky_relu(x)
        x = self.conv2(x)
        x = self.bn1(x)
        x = self.leaky_relu(x)
        x = self.conv3(x)
        x = self.bn2(x)
        x = self.leaky_relu(x)
        out = self.conv4(x)
        return out
      
# 모형
generator = Generator(1)
discriminator = Discriminator(1)

# Optimizer
optimizer_g = optim.SGD(generator.parameters(), lr=0.0001)
optimizer_d = optim.SGD(discriminator.parameters(), lr=0.0001)

# 학습

for epoch in range(10):
    d_losses = []
    g_losses = []

    for i, (img, _) in enumerate(trainloader):
        # 실제 사진
        real_imgs = imgs.float()

        # 잠재 변수
        z = Variable(torch.Tensor(np.random.normal(0,1,(imgs.shape[0], 100,1,1))))

        # 가짜 영상 생성
        fake_imgs = generator(z).detach()
        
        # 적대 손실
        loss_d = -torch.mean(discriminator(real_imgs)) + torch.mean(discriminator(fake_imgs))

        # 역전파
        optimizer_d.zero_grad()
        loss_d.backward()
        optimizer_d.step()

        d_losses.append(-loss_d.item())

        # Weight cliping, Lipschitz constraint
        for p in discriminator.parameters():
            p.data.clamp_(-0.01, 0.01)

        # 생성기 학습
        if i % 5 == 0:
            gen_imgs = generator(z)
            loss_g = -torch.mean(discriminator(gen_imgs))
            g_losses.append(loss_g.item())

            # 역전파
            optimizer_g.zero_grad()
            loss_g.backward()
            optimizer_g.step()
