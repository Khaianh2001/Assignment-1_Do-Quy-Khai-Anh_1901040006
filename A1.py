import cv2
from tkinter import Tk, Button, filedialog, Label
from PIL import Image, ImageTk

class ImageProcessingTool:
    def __init__(self):
        self.root = Tk()
        self.root.title("Image Processing Tool")

        self.image_path = None
        self.output_size = (300, 300)
        self.binary_threshold = 128

        self.load_button = Button(self.root, text="Chọn ảnh", command=self.load_image)
        self.resize_button = Button(self.root, text="Thay đổi kích thước", command=self.resize_image)
        self.binary_button = Button(self.root, text="Ngưỡng nhị phân", command=self.binary_thresholding)
        self.save_button = Button(self.root, text="Lưu ảnh", command=self.save_image)

        self.image_label = Label(self.root)

        self.load_button.pack(pady=10)
        self.resize_button.pack(pady=10)
        self.binary_button.pack(pady=10)
        self.save_button.pack(pady=10)
        self.image_label.pack()

        self.root.mainloop()
    def load_image(self):
        file_path = filedialog.askopenfilename(title="Chọn ảnh", filetypes=[("Image files", "*jfif;*.png;*.jpg;*.jpeg;*.gif")])
        if file_path:
            self.image_path = file_path
            self.display_image()
    def resize_image(self):
        if self.image_path:
            original_image = Image.open(self.image_path)
            resized_image = original_image.resize(self.output_size, Image.LANCZOS)
            self.display_image(resized_image)
    def binary_thresholding(self):
        if self.image_path:
            original_image = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
            _, binary_image = cv2.threshold(original_image, self.binary_threshold, 255, cv2.THRESH_BINARY)
            self.display_image(Image.fromarray(binary_image))
    def save_image(self):
        if self.image_path:
            save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                        filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if save_path:
                if not save_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    save_path += ".png"

                if not self.image_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                    original_image = cv2.imread(self.image_path)
                    cv2.imwrite(save_path, original_image)
                else:
                    image = Image.open(self.image_path)
                    image.thumbnail(self.output_size)
                    image.save(save_path)

    def display_image(self, image=None):
        if image is None:
            if self.image_path:
                image = Image.open(self.image_path)
            else:
                return

        image_tk = ImageTk.PhotoImage(image)

        self.image_label.configure(image=image_tk)
        self.image_label.image = image_tk

if __name__ == "__main__":
    ImageProcessingTool()
