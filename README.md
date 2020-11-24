# Image cipher
Image cipher is a command line tool developed in Python which able to cipher
images using AES-ECB or AES-CBC. It aims at providing a pedagogical tool for
understanding the differences between modes in symmetric cryptography.

## Requirements
- python

### Python packages
| Package    | Installation command   |
| ---------- | ---------------------- |
| virtualenv | pip install virtualenv |

## Usage
### Installation
`make install`

### Execution
`make run`

## Example
### Display an image
`(ImgCipher) show flag.jpg`  
The image must be in the `img` directory to be found by the program.

### Cipher an image
`(ImgCipher) cipher flag.jpg`  
By default the program use the ECB mode with the key='abcdefghijklmnop'.

### Use another mode
`(ImgCipher) show flag.jpg mode=CBC`  
Only ECB and CBC are currently available, also, this mode is now the default
mode.

### Change key
`(ImgCipher) show flag.jpg key=0123456789012345`  
The key must be 16 bytes (characters) long, also, this key is now the default
key.

### Change initial value
`(ImgCipher) show flag.jpg iv=wxcvbnqsdfghjklm`  
The initial value is only used if needed (i.e. in CBC mode currently) and it
must be 16 bytes (characters) long. Also, it is now the default initial value.

### Save the ciphered image
`(ImgCipher) show flag.jpg out=cipher.jpg`  
The saved image will be stored in the `img` directory.
