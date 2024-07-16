import torch 
import torchvision 
import os 
from torchvision.utils import make_grid
from tqdm import tqdm 
from model.unet import Unet
from noise_scheduler.noisescheduler import NoiseScheduler

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = Unet(im_channels = 1).to(device)

model.load_state_dict(torch.load(os.path.join('outputs', f'model_{39}.pth'), map_location=device))

model.eval()

scheduler = NoiseScheduler(1000, 0.0001, 0.02)

def sample(model, scheduler):
	xt = torch.randn((100,1, 28, 28)).to(device)
	
	for i in tqdm(reversed(range(1000))):
		noise_pred = model(xt, torch.as_tensor(i).unsqueeze(0).to(device))

		xt, x0_pred = scheduler.sample_prev_timestep(xt, noise_pred, torch.as_tensor(i).to(device))

		ims = torch.clamp(xt, -1,1).detach().cpu()

		ims = (ims + 1)/2
		grid = make_grid(ims, nrow = 10)
		img = torchvision.transforms.ToPILImage()(grid)
		if not os.path.isdir('outputs_grid'):
			os.makedirs('outputs_grid/samples')
		img.save(os.path.join('outputs_grid/samples',f'x0_{i}.png'))
		img.close()

		ims = torch.clamp(x0_pred, -1,1).detach().cpu()

		ims = (ims + 1)/2
		grid = make_grid(ims, nrow = 10)
		img = torchvision.transforms.ToPILImage()(grid)
		if not os.path.isdir('outputs_pred0_grid'):
			os.makedirs('outputs_pred0_grid/samples')
		img.save(os.path.join('outputs_pred0_grid/samples',f'x0_{i}.png'))
		img.close()
	pass
if __name__ == '__main__':
	with torch.no_grad():
		sample(model, scheduler)