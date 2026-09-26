import rich 
import os
import shutil
import pathlib
import sys #used
import ctypes #used
import tkinter as tk
from tkinter import messagebox


root = tk.Tk()

root.withdraw()

#remember 0 = false 1 = yes admin

class WinOptimizer:


    def __init__(self):
        print('Starting cleaning Demon..')


    def admin_check(self):
        if sys.platform == 'win32':
            if ctypes.windll.shell32.IsUserAnAdmin() == 1:
                return True
            else:
                return False
        else:
            return print('Please use a windows device.')

    def folder_size(self, dir_path):
        total_size = 0
    # os.walk drills through every folder and sub-folder automatically
        for dirpath, _, filenames in os.walk(dir_path): 
            for file in filenames:
                file_path = os.path.join(dirpath, file)
                total_size += os.path.getsize(file_path)
        return total_size
            

    def cleaner(self, path_dir_list):

        skipped_files = []
        total_number_cleaned = 0
        total_clear_size = 0

        if not self.admin_check(): #admin checker
            print('🚨No admin access.. System files will be skipped.')
            messagebox.showinfo("No admin perms", "Please provide some power please 🙏")

        for path_dir in path_dir_list:

            #checking if the path exists or not
            if not path_dir or not os.path.exists(path_dir):
                print(f"⚠️ Directory not found, skipping: {path_dir}")
                continue # Skips to the next folder safely

            for item_name in os.listdir(path_dir): #now we are inside like folder and find the files eg:= abcd.txt

                item_path = os.path.join(path_dir, item_name) #now we need a path of it so we will get = abcd.text/path_dir (given from before)

                try:

                    if os.path.isfile(item_path) or os.path.islink(item_path):

                        total_clear_size += os.path.getsize(item_path)
                        os.unlink(item_path)
                        print(f"✅Successfully deleted file: {item_path}")

                    elif os.path.isdir(item_path):

                        total_clear_size += self.folder_size(item_path)
                        shutil.rmtree(item_path)
                        print(f"✅Successfully deleted file: {item_path}")

                    
                    total_number_cleaned +=1

                except PermissionError:
                    skipped_files.append(item_path)
                    print(f"⚠️ Skipped (File is currently running/locked): {item_path}")

                except Exception as e:
                    skipped_files.append(item_path)
                    print(f'🚨Error: {e} Skipping {item_path}')


            # elif self.admin_check() == False:
            #     print('🚨No admin access..')
            #     return skipped_files, total_number_cleaned, total_clear_size
            
        print('Stopping the demon.. Finished ✅')
        return skipped_files, total_number_cleaned, total_clear_size
                    

def main():
    while True:
    #intences:
        obj = WinOptimizer()

        ask_user = int(input('''Hey what things you want me to delete?
Press 1: For deleting Temp, Prefetch, Recent (Recomended);
Press 2: For deleting Windwos Update caches, crashdumps, logs;
Press 3: For deleting DirectX Shader Cache;
Press 0: For Abort the mission.
        
'''))

        if ask_user == 1:
            targeted_dirs = [os.environ.get('temp'), 'C:\\Windows\\Prefetch', "C:\\Users\\surya\\AppData\\Roaming\\Microsoft\\Windows\\Recent"]
            sk_files,number,size = obj.cleaner(targeted_dirs)
            size_mb = size / (1024 * 1024)
            print(f'Skipped Files {len(sk_files)}', '\n')
            print(f'Total files cleared {number}', '\n')
            print(f'✅ {size_mb} MB space freed')
            print('💖Completed Tasks.')
        elif ask_user == 2:
            targeted_dirs = ["C:\\Windows\\SoftwareDistribution\\Download", "C:\\Users\\surya\\AppData\\Local\\CrashDumps", 'C:\\Windows\\Logs', ]
            sk_files,number,size = obj.cleaner(targeted_dirs)
            size_mb = size / (1024 * 1024)
            print(f'Skipped Files {len(sk_files)}', '\n')
            print(f'Total files cleared {number}', '\n')
            print(f'✅ {size_mb} MB space freed')
            print('💖Completed Tasks.') 
        elif ask_user == 3:
            again_ask_user = int(input('''What type of GPU do you use?
Press 1: For NVIDIA;
Press 2: For AMD;
Press 3: For No GPU (Cpu Graphics)

'''))
            if again_ask_user == 1:
                targeted_dirs = ['C:\\Users\\surya\\AppData\\Local\\NVIDIA\\DXCache']
                sk_files,number,size = obj.cleaner(targeted_dirs)
                size_mb = size / (1024 * 1024)
                print(f'Skipped Files {len(sk_files)}', '\n')
                print(f'Total files cleared {number}', '\n')
                print(f'✅ {size_mb} MB space freed')
                print('💖Completed Tasks.')
            
            elif again_ask_user == 2:
                targeted_dirs = ['C:\\Users\\surya\\AppData\\Local\\AMD\\DxCache']
                sk_files,number,size = obj.cleaner(targeted_dirs)
                size_mb = size / (1024 * 1024)
                print(f'Skipped Files {len(sk_files)}', '\n')
                print(f'Total files cleared {number}', '\n')
                print(f'✅ {size_mb} MB space freed')
                print('💖Completed Tasks.')
            elif again_ask_user == 3:
                targeted_dirs = ['C:\\Users\\surya\\AppData\\Local\\D3DSCache']
                sk_files,number,size = obj.cleaner(targeted_dirs)
                size_mb = size / (1024 * 1024)
                print(f'Skipped Files {len(sk_files)}', '\n')
                print(f'Total files cleared {number}', '\n')
                print(f'✅ {size_mb} MB space freed')
                print('💖Completed Tasks.')
            else:
                print('Please press between (1-2)')
        elif ask_user == 0:
            print('Aborting mission. 🫡')
            break
        else:
            print('Please press between 0-3')

main()


#written by surya 15-09-2026 11:52