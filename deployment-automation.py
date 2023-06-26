import os
import subprocess

def deploy_application(repo_url, target_directory):
    # Clone or pull the latest code from the Git repository
    if os.path.exists(target_directory):
        subprocess.run(["git", "pull"], cwd=target_directory)
    else:
        subprocess.run(["git", "clone", repo_url, target_directory])

    # Change to the target directory
    os.chdir(target_directory)

    # Install application dependencies
    subprocess.run(["pip", "install", "-r", "requirements.txt"])

    # Build the application (if required)
    # Example: subprocess.run(["python", "setup.py", "build"])

    # Restart services (if required)
    # Example: subprocess.run(["systemctl", "restart", "my-service"])

    print("Application deployment completed.")

# Example usage
git_repo = "https://github.com/example/repo.git"  # Update with the URL of your Git repository
deploy_dir = "/path/to/deploy/directory"  # Update with the desired target directory for the deployment

deploy_application(git_repo, deploy_dir)
