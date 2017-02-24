import re
import os
def main():
    dir_to_clean = ['/home/z/test_dir_1/to_delete_1',
                    '/home/z/test_dir_1/to_delete_2',
                    '/home/z/test_dir_1/to_delete_3',
                    '/home/z/test_dir_1/to_delete_4']
    
    regex_to_delete = '^delete'

    euid = os.geteuid()
    if euid != 0:
        raise EnvironmentError("Need to run as root")
        exit()

    pat = re.compile(regex_to_delete)
    
    for dir in dir_to_clean:
	file_removed_flag = False
        print("\nCurrent directory ::: " + dir)
        os.chdir(dir)
        for filename in os.listdir(dir):
            if(pat.match(filename)):
                print("DELETING FILE ::: " + filename)
                os.remove(filename)
		file_removed_flag = True
	if not file_removed_flag:
		print("No files to remove")

if __name__ == '__main__':
    main()
