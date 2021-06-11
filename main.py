import shutil
import matplotlib.pyplot as plt

"""
The show_disc_info() function takes a path of a drive 
and displays the total size of the drive, the used space on the drive and the total free space remaining
on the specified drive.
"""


class StorageReport:

    def __init__(self, drive_path):
        self.drive_path = drive_path
        self.total, self.used, self.free = shutil.disk_usage(drive_path)
        self.formatted_used = self.used // (2**30)
        self.formatted_free = self.free // (2**30)
        self.disc_values = [self.formatted_used, self.formatted_free]

    def show_disc_info(self):
        print(f"Total: {self.total // (2**30)} gb on drive: {str(self.drive_path)}")
        print(f"Used: {self.formatted_used} gb on drive:  {str(self.drive_path)}")
        print(f"Free: {self.formatted_free} gb on drive:  {str(self.drive_path)}")

    # Used to display the percent values and original values on the pie chart

    def generate_autopct(self, d_values):
        def make_autopct(pct):
            total = sum(d_values)
            val = int(round(pct*total/100.0))
            return f'{pct:.2f}% ({val:d}gb)'
        return make_autopct

    def display_disc_graph(self):
        colours = ['#ff9999', '#99ff99']
        disc_info = 'Used', 'Free'
        explode_pie = (0.05, 0.05)
        plt.pie(self.disc_values,
                autopct=self.generate_autopct(self.disc_values),
                colors=colours,
                pctdistance=0.85,
                explode=explode_pie,
                shadow=True
                )
        plt.legend(disc_info, loc="best")
        plt.show()



x = StorageReport("C:")
x.show_disc_info()
x.display_disc_graph()