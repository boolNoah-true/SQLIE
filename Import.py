import subprocess
import shutil
import os
import sys

def find_mysql_executable():
    paths = [
        'C:\\xampp\\mysql\\bin\\mysql.exe',
        'C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe',
        'C:\\Program Files (x86)\\MySQL\\MySQL Server 8.0\\bin\\mysql.exe',
        '/usr/local/mysql/bin/mysql',
        '/usr/local/bin/mysql',
        '/Applications/XAMPP/bin/mysql'
    ]

    for path in paths:
        if os.path.isfile(path):
            return path

    mysql_path = shutil.which('mysql')
    if mysql_path:
        return mysql_path

    return None

def run_mysql_import(dbname):
    mysql_path = find_mysql_executable()
    if not mysql_path:
        print("mysql executable not found. Please ensure MySQL is installed and mysql is in your PATH.")
        return

    print(f"mysql found at: {mysql_path}")

    sql_file = f'{dbname}.sql'

    if not os.path.isfile(sql_file):
        print(f"SQL file {sql_file} not found. Please ensure the file exists in the same directory as this script.")
        return

    if sys.platform == 'win32':
        command = f'"{mysql_path}" -u root -p {dbname} < "{sql_file}"'
    else:
        command = f'{mysql_path} -u root -p {dbname} < "{sql_file}"'

    print("Please enter the MySQL root password when prompted.")
    subprocess.run(command, shell=True)

    print("Import complete. Press Enter to exit.")
    input()

if __name__ == "__main__":
    dbname = input("Enter the name of the database you would like to import into: ")
    run_mysql_import(dbname)
