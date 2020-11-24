from PIL import Image
import numpy as np
from Crypto.Cipher import AES

def get_img(img):
    image = Image.open(img)
    data = np.array(image)
    return data

def encrypt_img(img, key, mode, iv=None):
    cipher = AES.new(key, mode, iv)
    image = Image.open(img)
    data = np.array(image)
    for i in range(3):
        data[:,:,i] = encrypt_matrix(data[:,:,i], cipher)
    return data

def encrypt_matrix(data, c):
    dtype = data.dtype
    shape = data.shape
    data = data.reshape(-1)
    data = c.encrypt(bytes(data))
    data = np.frombuffer(data, dtype=dtype)
    data = data.reshape(shape)
    return data

def plot_data(data):
    img = Image.fromarray(data, 'RGB')
    img.show()

def save_data(data, filename):
    img = Image.fromarray(data, 'RGB')
    img.save(filename)

if __name__ == "__main__":
    key = 'abcdefghijklmnop'
    img = 'flag.jpg'
    mode = AES.MODE_ECB

    data = encrypt_img(img, key, mode)
    plot_data(data)
