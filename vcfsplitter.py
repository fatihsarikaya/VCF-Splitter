import os
import re
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class VCFChromSplitter:
    def __init__(self, input_vcf_path,output_path):
        self.input_vcf_path = input_vcf_path
        self.output_path = output_path
        self.chrom_files = {}

        with open(self.input_vcf_path, 'r') as vcf:
            for line in vcf:
                if line.startswith('#'):
                    # Write header lines to all chromosome files
                    for chrom_file in self.chrom_files.values():
                        chrom_file.write(line)
                else:
                    # Extract the chromosome from the line
                    chrom_match = re.search(r'^(\w+)\t', line)
                    chrom = chrom_match.group(1)

                    # If this is the first variant for this chromosome, create a new file
                    if chrom not in self.chrom_files:
                        output_vcf_path = os.path.splitext(output_path)[0] + os.path.basename(input_vcf_path)+ f'.{chrom}.vcf'
                        self.chrom_files[chrom] = open(output_vcf_path, 'w')

                    # Write the variant to the appropriate chromosome file
                    self.chrom_files[chrom].write(line)

        # Close all chromosome files
        for chrom_file in self.chrom_files.values():
            chrom_file.close()

        messagebox.showinfo("Success","VCF File has been splitted")



def show_file_dialog_for_vcf():
    vcf_file_path = filedialog.askopenfilename(filetypes=[("VCF Files","*.vcf")])
    input_entry.insert(0,vcf_file_path)
def select_file_directory():
    output_path = filedialog.askdirectory()
    output_entry.insert(0,output_path)

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("VCF File Splitter")
root.geometry("400x300")
root.eval('tk::PlaceWindow . center')

# Create input elements
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Input VCF:   ")
input_label.pack(side=tk.LEFT)

input_entry = tk.Entry(input_frame)
input_entry.pack(side=tk.LEFT)

# Create output elements

output_frame = tk.Frame(root)
output_frame.pack(pady=10)

output_label = tk.Label(output_frame,text="Output Path:")
output_label.pack(side=tk.LEFT)

output_entry = tk.Entry(output_frame)
output_entry.pack(side=tk.LEFT)

# Create button to select vcf and output folder
find_vcf_file_button = tk.Button(root, text="Find VCF File",command=show_file_dialog_for_vcf)
find_vcf_file_button.pack(side=tk.TOP,pady=10)
select_output_file_button = tk.Button(root, text="Select Output Path", command=select_file_directory)
select_output_file_button.pack(side=tk.TOP)

# Create button to begin application and exit program

split_button = tk.Button(root, text="Split",command=lambda: VCFChromSplitter(input_entry.get(),output_entry.get()+"/"))
split_button.pack(side=tk.TOP,pady=10)

exit_button = tk.Button(root,text="Exit",command=exit_app)
exit_button.pack(side=tk.TOP,pady=10)
# Start the application
root.mainloop()
