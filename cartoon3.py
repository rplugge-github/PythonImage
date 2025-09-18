#https://pyseek.com/2022/07/image-to-cartoon-converter-in-python/
import cv2
import pathlib
import pyautogui
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

class Image_Cartoonify:
    def __init__(self, root):
        self.window = root
        self.window.geometry("960x560")
        self.window.title('Cartoonify')
        ##self.window.resizable(width = False, height = False)

        self.width = 740
        self.height = 480

        self.Image_Path = './images'

        # ==============================================
        # ================Menubar Section===============
        # ==============================================
        # Creating Menubar
        self.menubar = Menu(self.window)

        # Adding Edit Menu and its sub menus
        edit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Open', menu=edit)
        edit.add_command(label='Open Image',command=self.open_image)
        
        # Menu widget to cartoonify the image
        cartoonify = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Cartoonify', menu=cartoonify)
        cartoonify.add_command(label='Create Cartoon', command=self.cartoonify)
        
        # Exit the Application
        exit = Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Exit', menu=exit)
        exit.add_command(label='Exit', command=self._exit)

        # Configuring the menubar
        self.window.config(menu=self.menubar)
        # ===================End=======================

        # Creating a Frame
        self.frame = Frame(self.window,
            width=self.width,height=self.height)
        self.frame.pack()
        self.frame.place(anchor='center', relx=0.5, rely=0.5)

    # Open an Image through filedialog
    def open_image(self):
        self.clear_screen()
        self.Image_Path = filedialog.askopenfilename(title = "Select an Image", filetypes = (("Image files", "*.jpg *.jpeg *.png"),))
        if len(self.Image_Path) != 0:
            self.show_image(self.Image_Path)
    
    # Display the Image
    def show_image(self, Img):
        # Opening the image
        image = Image.open(Img)
        # resize the image, so that it fits to the screen
        resized_image = image##.resize((self.width, self.height))

        # Create an object of tkinter ImageTk
        self.img = ImageTk.PhotoImage(resized_image)

        # A Label Widget for displaying the Image
        label = Label(self.frame, image=self.img)
        label.pack()

    def cartoonify(self):
        # Storing the image path to a variable
        ImgPath = self.Image_Path

        # If any image is not selected 
        if len(ImgPath) == 0:
            pass
        else:
            # Get the file name to be saved after cartoonify the image
            filename = pyautogui.prompt("Enter the filename to be saved")
            # Filename with the extension (extension of the original image)
            filename = "images/_cartoon3_" + filename + pathlib.Path(ImgPath).suffix
            # Read the image        
            Img = cv2.imread(ImgPath)
            ##Img = cv2.resize(Img, (740,480))
            GrayImg = cv2.cvtColor(src=Img, code=cv2.COLOR_BGR2GRAY)
            SmoothImg = cv2.medianBlur(src=GrayImg, ksize=5)

            Edges = cv2.adaptiveThreshold(src=SmoothImg, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=9, C=9)
            
            # Adjust the the values of sigmaColor and sigmaSpace to get a proper cartoon effect
            ColorImg = cv2.bilateralFilter(src=Img, d=9, sigmaColor=300, sigmaSpace=300)

            CartoonImg = cv2.bitwise_and(src1=ColorImg,src2=ColorImg,mask=Edges)

            cv2.imwrite(filename, CartoonImg)

            self.clear_screen()
            self.show_image(filename)

    # Remove all widgets from the frame
    def clear_screen(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    # It destroys the main GUI window of the
    # application
    def _exit(self):
        self.window.destroy()

if __name__ == "__main__":
    root = Tk()
    # Creating an object of Image_Cartoonify class
    obj = Image_Cartoonify(root)
    root.mainloop()