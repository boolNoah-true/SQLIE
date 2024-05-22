import subprocess
import shutil
import os
import sys

def locate_mysqldump():
    paths = [
        'C:\\xampp\\mysql\\bin\\mysqldump.exe',
        'C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysqldump.exe',
        'C:\\Program Files (x86)\\MySQL\\MySQL Server 8.0\\bin\\mysqldump.exe',
        '/usr/local/mysql/bin/mysqldump',
        '/usr/local/bin/mysqldump',
        '/Applications/XAMPP/bin/mysqldump'
    ]

    for path in paths:
        if os.path.isfile(path):
            return path

    mysqldump_path = shutil.which('mysqldump')
    if mysqldump_path:
        return mysqldump_path

    return None

def run_mysqldump(dbname):
    mysqldump_path = locate_mysqldump()
    if not mysqldump_path:
        print("mysqldump not found. Please ensure MySQL is installed and mysqldump is in your PATH.")
        return

    print(f"mysqldump found at: {mysqldump_path}")

    if sys.platform == 'win32':
        command = f'"{mysqldump_path}" -u root -p {dbname} > {dbname}.sql'
    else:
        command = f'{mysqldump_path} -u root -p {dbname} > {dbname}.sql'

    print("Please enter the MySQL root password when prompted.")
    subprocess.run(command, shell=True)

    print("Export complete. Press Enter to exit.")
    input()

if __name__ == "__main__":
    dbname = input("Enter the name of the database you would like to export: ")
    run_mysqldump(dbname)
