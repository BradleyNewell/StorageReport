import shutil

"""
The show_disc_info() function takes a path of a drive 
and displays the total size of the drive, the used space on the drive and the total free space remaining
on the specified drive.
"""


def show_disc_info(path):
    total, used, free = shutil.disk_usage(path)
    print(f"Total: {total // (2**30)} gb on drive: {str(path)}")
    print(f"Used: {used // (2**30)} gb on drive:  {str(path)}")
    print(f"Free: {free // (2**30)} gb on drive:  {str(path)}")


show_disc_info("C:")
