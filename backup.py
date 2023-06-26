import shutil
import tarfile
import datetime

def create_backup(source_directory, destination_directory):
    # Create a timestamp for the backup file name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_filename = f"backup_{timestamp}.tar.gz"

    # Create a tarball of the source directory
    with tarfile.open(backup_filename, "w:gz") as tar:
        tar.add(source_directory, arcname=os.path.basename(source_directory))

    # Move the backup file to the destination directory
    destination_path = os.path.join(destination_directory, backup_filename)
    shutil.move(backup_filename, destination_path)

    print(f"Backup created: {destination_path}")

# Example usage
source_dir = '/path/to/source/directory'  # Update with the actual path to the directory you want to back up
destination_dir = '/path/to/destination/directory'  # Update with the desired destination directory for the backup

create_backup(source_dir, destination_dir)
