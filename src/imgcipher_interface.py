import cmd
from os import listdir
from os.path import isfile, join
from Crypto.Cipher import AES

from imgcipher import get_img, plot_data, encrypt_img, save_data

class ImgCipherInterface(cmd.Cmd):

    intro = "Welcome on the image cipher. Type help or ? to list commands.\n"
    prompt = "(ImgCipher) "
    goodbye = "Goodbye ! Hope to see you soon !"
    img_ext = ('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')
    img_path = "./img/"
    key = 'abcdefghijklmnop'
    mode = AES.MODE_ECB
    iv = "azertyuiopmlkjhg"
    modes = {
        "ECB": AES.MODE_ECB,
        "CBC": AES.MODE_CBC,
    }

    def __init__(self):
        super().__init__()
        self.cur_mode = "ECB"
        self.output_file = None

    def do_exit(self, arg):
        print(self.goodbye)
        return True

    def help_exit(self):
        print("Exit the program.\n(But you won't do that right ?)")

    def get_files_in_dir(self, path):
        files = [f for f in listdir(path) if (isfile(join(path, f)) and f.lower().endswith(self.img_ext))]
        return files

    def do_show(self, arg):
        arg = arg.split(" ")
        if len(arg) < 1:
            print("I need a file to show !")
        else:
            if arg[0] in self.get_files_in_dir(self.img_path):
                data = get_img(self.img_path + arg[0])
                plot_data(data)
            else:
                print("I need an image !")

    def complete_show(self, text, line, begidx, endidx):
        return [f for f in self.get_files_in_dir(self.img_path) if f.startswith(text)]

    def help_show(self):
        print("Show an image.")
        print("Usage:")
        print("\tshow <image_name>")

    def do_cipher(self, arg):
        arg = arg.split(" ")
        if len(arg) < 1:
            print("I need a file to cipher !")
        else:
            if arg[0] in self.get_files_in_dir(self.img_path):
                if len(arg) > 1:
                    self.update_config(arg[1:])
                data = encrypt_img(self.img_path + arg[0], self.key, self.mode, self.iv)
                if self.output_file != None:
                    save_data(data, self.img_path + self.output_file)
                    self.output_file = None
                plot_data(data)
            else:
                print("I need an image !")

    complete_cipher = complete_show

    def help_cipher(self):
        print("Cipher then show an image.")
        print("Usage: cipher <image_name> key=<KEY> mode=<MODE> iv=<IV> out=<filename>")
        print("\timage_name: the name of the file image")
        print("\tkey: the key used for the encryption")
        print("\tmode: the mode used for the AES encryption")
        print("\tiv: the initial value used in the encryption if needed")
        print("\tout: the name of the file where to store the encrypted image")

    def update_config(self, args):
        for arg in args:
            arg = arg.split("=")
            if arg[0] == "key":
                self.update_key(arg[1])
            elif arg[0] == "mode":
                self.update_mode(arg[1])
            elif arg[0] == "iv":
                self.update_iv(arg[1])
            elif arg[0] == "out":
                self.output_file = arg[1]

    def update_iv(self, iv):
        if len(iv) != 16:
            print("Wrong IV size ! Must be 16 bytes long !")
            print("I keep using the previous IV.")
        else:
            self.iv = iv

    def update_key(self, key):
        if len(key) != 16:
            print("Wrong key size ! Must be 16 bytes long !")
            print("I keep using the previous key.")
        else:
            self.key = key

    def update_mode(self, mode):
        if mode in self.modes:
            self.cur_mode = mode
            self.mode = self.modes[self.cur_mode]
        else:
            print("Wrong mode !")
            print("Available modes:")
            for m in self.modes:
                print("\t{}".format(m))
            print("I keep using the previous mode.")

    def do_config(self, arg):
        print("Key:  {}".format(self.key))
        print("Mode: {}".format(self.cur_mode))
        print("IV:   {}".format(self.iv))

    def help_config(self):
        print("Display the current configuration of the ciphering instance.")

    def emptyline(self):
        pass

if __name__ == "__main__":
    ic = ImgCipherInterface()
    ic.cmdloop()
