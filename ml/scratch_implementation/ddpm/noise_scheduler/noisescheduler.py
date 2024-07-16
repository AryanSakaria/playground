import torch

class NoiseScheduler:
	def __init__(self, num_timestamps, beta_start, beta_end):
		self.num_timestamps = num_timestamps
		self.beta_start = beta_start
		self.beta_end = beta_end

		self.betas = torch.linspace(beta_start, beta_end, num_timestamps)
		self.alphas = 1 - self.betas 
		self.alpha_prod = torch.cumprod(self.alphas,dim=0)
		self.sqrt_alpha_prod = torch.sqrt(self.alpha_prod)
		self.sqrt_one_minus_alpha_prod = torch.sqrt(1 - self.alpha_prod)

	def add_noise(self, original_img, noise, t):
		original_shape = original_img.shape
		batch_size = original_shape[0]

		sqrt_alpha_prod = self.sqrt_alpha_prod.to(original_img.device)[t].reshape(batch_size) # print and see shape
		sqrt_one_minus_alpha_prod = self.sqrt_one_minus_alpha_prod.to(original_img.device)[t].reshape(batch_size)

		# reshaping to bx1x1x1
		for _ in range(len(original_shape) - 1):
			sqrt_alpha_prod = sqrt_alpha_prod.unsqueeze(-1)# see shape here also
			sqrt_one_minus_alpha_prod = sqrt_one_minus_alpha_prod.unsqueeze(-1)

		return (sqrt_alpha_prod.to(original_img.device) * original_img + sqrt_one_minus_alpha_prod.to(original_img.device)* noise) 

	def sample_prev_timestep(self, xt, noise_pred, t):
		x0 = ((xt - (self.sqrt_one_minus_alpha_prod.to(xt.device)[t] * noise_pred)) / 
			torch.sqrt(self.alpha_prod.to(xt.device)[t]))
		x0 = torch.clamp(x0, -1, max = 1) #brings everything to -1 to 1 range

		mean = xt - ((self.betas.to(xt.device)[t]*noise_pred)/self.sqrt_one_minus_alpha_prod.to(xt.device)[t])
		mean = mean / torch.sqrt(self.alphas.to(xt.device)[t])

		if t == 0:
			return mean, x0

		variance = self.betas.to(xt.device)[t] * ((1 - self.alpha_prod.to(xt.device)[t-1])/(1 - self.alpha_prod.to(xt.device)[t]))
		sigma = variance ** 0.5 #std deviation?
		z = torch.randn(xt.shape).to(xt.device)

		return mean + sigma*z, x0



