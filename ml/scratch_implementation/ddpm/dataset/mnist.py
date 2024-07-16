import os
import glob 
import torchvision
from PIL import Image
from tqdm import tqdm 
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import Dataset

class MnistDataset(Dataset):
	def __init__(self, split, im_path, im_ext='png'):
		self.split = split # train/test?
		self.im_ext = im_ext 
		self.images, self.labels = self.load_images(os.path.join(im_path,self.split,'images'))

	def load_images(self, im_path):
		"""
		gets all images
		"""
		imgs = []
		labels = []
		print("in load images", im_path)
		for d_name in tqdm(os.listdir(im_path)):
			for f_name in glob.glob(os.path.join(im_path, d_name, f'*.{self.im_ext}')):
				imgs.append(f_name)
				labels.append(int(d_name))
				# print(os.path.isfile(f_name))
		print(f"Found {len(imgs)} for split {self.split}")
		return imgs, labels

	def __len__(self):
		return len(self.images)

	def __getitem__(self, index):
		im = Image.open(self.images[index])
		im_tensor = torchvision.transforms.ToTensor()(im)

		im_tensor = (2*im_tensor) - 1 # converts to -1 to 1
		return im_tensor
