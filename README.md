# My Super Sampling Shit Using ISR RDN + GAN
## Setup & Run:
Using ISR(Image Super Resolution) using RDN_GANS/weights='noise-cancel' model
```bash
# Create anaconda environment
conda create -n ssgpu python=3.6 -y
conda activate ssgpu
pip install ISR
conda install tensorflow-gpu -y

# Clone repo and enter directory
git clone https://github.com/sawyermade/super_sample.git 
cd super_sample

# Run program, ex: $ python ss.py path/to/image/file min_width_integer
python ss.py sample_image.jpg 4000
```
Output: original/path/filename + -ss_widthxheight.png