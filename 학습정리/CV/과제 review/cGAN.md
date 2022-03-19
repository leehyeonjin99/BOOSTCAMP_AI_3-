# Architecture of cGAN
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159127499-96e5a65f-14df-4fa9-8131-4ed9d7ac3e2a.png" width='70%'></p>

# GAN vs. cGAN
<p align='center'><img src="https://user-images.githubusercontent.com/57162812/159127572-ae79b746-a641-4a72-b182-32937f0f07b9.png" width='50%'></p>

GAN은 class와 상관없이 image를 생성해낸다. 하지만 우리는 원하는 class에 대해서 image를 생성해내고 싶다. 따라서, condition을 추가하여 cGAN이 제안되었다.

## Generator

```python
class Generator(nn.Module):
    # initializers
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1_1 = nn.Linear(100, 256)
        self.fc1_1_bn = nn.BatchNorm1d(256)
        self.fc1_2 = nn.Linear(10, 256)
        self.fc1_2_bn = nn.BatchNorm1d(256)
        self.fc2 = nn.Linear(512, 2048)
        self.fc2_bn = nn.BatchNorm1d(2048)
        self.fc3 = nn.Linear(2048, 1024)
        self.fc3_bn = nn.BatchNorm1d(1024)
        self.fc4 = nn.Linear(1024, 784)
        self.dropout = nn.Dropout(p=0.2)

    # weight_init
    def weight_init(self, mean, std):
        for m in self._modules:
            normal_init(self._modules[m], mean, std)

    # forward method
    def forward(self, input, label):
        x = F.relu(self.fc1_1_bn(self.fc1_1(input)))
        y = F.relu(self.fc1_2_bn(self.fc1_2(label)))
        x = torch.cat([x, y], 1)
        x = F.relu(self.fc2_bn(self.fc2(x)))
        x = self.dropout(x)
        x = F.relu(self.fc3_bn(self.fc3(x)))
        x = self.dropout(x)
        x = F.tanh(self.fc4(x))

        return x
```

- label에 대한 정보, 즉 condition을 함께 입력해 image와 합친다.
- `self.fc1_1`과 `self.fc2_1`의 output dimension은 input dimension보다 크다. input과 label을 합치기 전에 dimension을 맞춰주는 작업에 있어서 공간정보를 잃지 않기 위해서 이다.
- activation function으로 `tanh()`를 사용하였다. `sigmoid()`는 중심이 0이 아니기 때문에 문제점이 발생할 수 있는 부분을 `tanh()`가 해결해준다. 이 실험에서는 noise를 많이 없애주는 것을 확인할 수 있다.

## Discriminator
```python
class Discriminator(nn.Module):
    # initializers
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc1_1 = nn.Linear(784, 1024)
        self.fc1_2 = nn.Linear(10, 1024)
        self.fc2 = nn.Linear(2048, 512)
        self.fc2_bn = nn.BatchNorm1d(512)
        self.fc3 = nn.Linear(512, 256)
        self.fc3_bn = nn.BatchNorm1d(256)
        self.fc4 = nn.Linear(256, 1)
        self.dropout = nn.Dropout(p=0.2)

    # weight_init
    def weight_init(self, mean, std):
        for m in self._modules:
            normal_init(self._modules[m], mean, std)

    # forward method
    def forward(self, input, label):
        x = F.leaky_relu(self.fc1_1(input), 0.1)
        y = F.leaky_relu(self.fc1_2(label), 0.1)
        x = torch.cat([x, y], 1)
        x = F.leaky_relu(self.fc2_bn(self.fc2(x)), 0.1)
        x = self.dropout(x)
        x = F.leaky_relu(self.fc3_bn(self.fc3(x)), 0.1)
        x = F.sigmoid(self.fc4(x))

        return x
```

## Training
```python
g_loss = torch.Tensor([0])
d_loss = torch.Tensor([0])

for epoch in range(parser.n_epochs):
  for batch_idx, (x, y) in enumerate(train_loader):
    generator.train()
    # linear layer 통과를 위해 이미지 차원 resize
    x_flatten = x.view(x.shape[0], -1)
    # 라벨 one-hot encoding
    one_hot_label = torch.nn.functional.one_hot(y, num_classes=parser['n_classes'])
    # to GPU
    img_torch2vec = x_flatten.type(torch.FloatTensor).cuda()  
    label_torch = one_hot_label.type(torch.FloatTensor).cuda()

    # Adversarial ground truths
    valid = torch.ones(parser.batch_size, 1).cuda()
    fake = torch.zeros(parser.batch_size, 1).cuda()

    # Configure input
    real_imgs = img_torch2vec
    labels = label_torch

    # Train Gen
    optimizer_G.zero_grad()

    # Sample noise and labels as generator input
    z = torch.randn(parser.batch_size, parser.latent_dim).cuda()
    gen_labels = []
    for randpos in np.random.randint(0, parser.n_classes, parser.batch_size):
      gen_labels.append(torch.eye(parser.n_classes)[randpos])
    gen_labels = torch.stack(gen_labels).cuda()

    # Generate a batch of images
    gen_imgs = generator(z, gen_labels)
    
    # Loss measures generator's ability to fool the discriminator
    val_output = discriminator(gen_imgs, gen_labels)
    g_loss = cross_entropy(val_output, valid)

    g_loss.backward()
    optimizer_G.step()

    # Train Disc
    optimizer_D.zero_grad()
    
    validity_real = discriminator(real_imgs, labels)
    try:
        d_real_loss = cross_entropy(validity_real, valid)
    except:
        valid = torch.ones(validity_real.shape[0], 1).cuda()
        d_real_loss = cross_entropy(validity_real, valid)

    # val = output         
    validity_fake = discriminator(gen_imgs.detach(), gen_labels)
    d_fake_loss = cross_entropy(validity_fake, fake)

    d_loss = (d_real_loss + d_fake_loss) / 2

    d_loss.backward()
    optimizer_D.step()
```

- `z = torch.randn(parser.batch_size, parser.latent_dim).cuda()`는 generator에 넣어줄 값이다. random한 값들로 만들어진 image이기 때문에 noise가 심하다.
- `gen_image`는 generator를 통해서 만들어진 image이며, `val_output`은 generator가 만든 image를 discriminator가 real, fake로 구분한다. generator는 discriminator가 자신이 만든 image를 real로 판별하기를 원하기 때문에, generator_loss는 `cross_entropy(val_output, valid)`로 이뤄진다. valid는 모두 1로 이루어진 tensor이다.
- try를 하는 이유는 마지막 batch가 batch_size가 일정한 값이 아닐 수 있기 때문이다. generator에 대해서는 하지 않는 이유는 generator는 항상 batch_size만큼의 image를 만들어내기 때문이다.
- discriminatro는 real image에 대해서는 모두 real로 판별하고 generated image에 대해서는 fake image로 판별하기를 원한다. 따라서 discriminator_loss는 `d_real_loss = cross_entropy(validity_real, valid)`와 `d_fake_loss = cross_entropy(validity_fake. fake)`의 평균으로 이뤄진다. fake는 모두 0으로 이루어진 tensor이다.
