import rich 
import os
import shutil
import pathlib
import sys #used
import ctypes #used

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

    #list of the folders:
    targeted_dirs = [os.environ.get('temp'), 'C:\\Windows\\Prefetch']

    #itenences
    obj = WinOptimizer()
    sk_files,number,size = obj.cleaner(targeted_dirs)
    size_mb = size / (1024 * 1024)

    print(f'Skipped Files {len(sk_files)}', '\n')
    print(f'Total files cleared {number}', '\n')
    print(f'✅ {size_mb} MB space freed')

main()


#written by surya 15-09-2026 11:52