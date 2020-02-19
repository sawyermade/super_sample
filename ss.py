import numpy as np, sys, os
from PIL import Image 
from ISR.models import RDN

def main():
	# Opens image and converts to numpy
	img_path, min_size = sys.argv[1], int(sys.argv[2])
	img_pil = Image.open(img_path)
	img = np.array(img_pil)

	# Super samples image and converts back to pil
	rdn = RDN(weights='noise-cancel')
	img_ss = img.copy()
	count = 0
	while(img_ss.shape[1] < min_size):
		img_ss = rdn.predict(img_ss, by_patch_of_size=50)
		count += 1
	img_new = Image.fromarray(img_ss)

	# Creates output file path
	img_path_split = img_path.split(os.sep)
	fname_in_full = img_path_split[-1]
	if len(img_path_split) > 1:
		input_dir = os.path.join(*img_path_split[:-1])
	else:
		input_dir = ''
	fname_in_file, fname_in_ext = fname_in_full.rsplit('.', 1)
	fname_out_file = fname_in_file + f'-ss_{img_ss.shape[1]}x{img_ss.shape[0]}'
	fname_out_full = os.path.join(input_dir, fname_out_file + '.png')

	# Saves new super sampled image and prints old/new resolutions
	print(f'\nOriginal Resolution = {img.shape[1]}x{img.shape[0]}')
	print(f'New Resolution = {img_ss.shape[1]}x{img_ss.shape[0]}')
	print(f'Number of iterations = {count}\n')
	img_new.save(fname_out_full)

if __name__ == '__main__':
	main()