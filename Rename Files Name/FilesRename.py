# Python version 3.11.2
import os


def rename_files(path:str, new_img_name):
    """ This function will rename the specified file to the specified name
    Args:
        path (str): pass your path where your files are stored
        new_img_name (_type_): give the name of the image to rename
    """
    
    try:
        img_list = os.listdir(path=path)
        
        for i, img_name in enumerate(img_list):
            extension_name = img_name.split('.')[1]
            old_img_path = os.path.join(path, img_name)
            new_img_path = os.path.join(path, f"{new_img_name}{i}.{extension_name}")
            os.rename(old_img_path, new_img_path)
        print("Successfully renamed")
    except Exception as e:
        print("Opps!! ", e)
        print("Please enter the valid path!!")


if __name__ == "__main__":
    rename_files(path="C:\\Users\\alami\\Downloads\\New folder", new_img_name="BangladeshFlag")