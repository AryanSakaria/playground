import torch 
import yaml #???

import os 
import numpy as np 
from tqdm import tqdm 

from torch.optim import Adam 
from dataset.mnist import MnistDataset
from torch.utils.data import DataLoader
from model.unet import Unet

from noise_scheduler.noisescheduler import NoiseScheduler

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print('cuda' if torch.cuda.is_available() else 'cpu')
def train():
	print("starting training")
	scheduler = NoiseScheduler(1000, 0.0001, 0.02)

	mnist = MnistDataset('train', im_path = 'mnist_images')
	mnist_loader = DataLoader(mnist, batch_size = 16, shuffle = True, num_workers = 4)

	#model init
	model = Unet(im_channels = 1).to(device)
	model.train()

	output_dir = 'outputs'
	if not os.path.isdir(output_dir):
		os.makedirs(output_dir)


	num_epochs = 40
	optimizer = Adam(model.parameters(), lr=0.0001)
	criterion = torch.nn.MSELoss()
	epoch_start = 19
	model.load_state_dict(torch.load(os.path.join(output_dir, f'model_{epoch_start}.pth'), map_location=device))
	print("file exists", os.path.isfile(os.path.join(output_dir, f'model_{epoch_start}.pth')))
	for epoch_idx in range(epoch_start+1, num_epochs):
		print(f'training for {epoch_idx}')
		losses = []
		for im in tqdm(mnist_loader):
			optimizer.zero_grad()
			im = im.float().to(device)

			noise = torch.randn_like(im).to(device)

			t = torch.randint(0, 1000, (im.shape[0],)).to(device) # why im.shape[0]??

			noisy_im = scheduler.add_noise(im, noise, t)
			noise_pred = model(noisy_im, t)

			loss = criterion(noise_pred, noise)
			losses.append(loss.item())
			loss.backward()
			optimizer.step()

		if epoch_idx % 5 == 4:
			torch.save(model.state_dict(), os.path.join(output_dir, f'model_{epoch_idx}.pth'))

	print("training complete")

if __name__ == '__main__':
	train()