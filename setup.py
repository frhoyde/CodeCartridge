import os
import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        print(f"Error details: {e}")

def install_packages():
    packages = [
        "curl",
        "wget",
        "apt-transport-https",
        "ca-certificates",
        "software-properties-common",
        "zsh",
        "git",
        "neovim",
        "flameshot"
    ]
    run_command(f"sudo apt update && sudo apt install -y {' '.join(packages)}")

def install_vscode():
    run_command("sudo dpkg -i ~/Downloads/vscode.deb")
    run_command("sudo apt install -f")

def install_intellij():
    run_command("sudo tar -xzf ~/Downloads/intellij.tar.gz -C /opt/")
    run_command("sudo ln -s /opt/idea-*/bin/idea.sh /usr/local/bin/intellij")

def install_node():
    run_command("curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -")
    run_command("sudo apt install -y nodejs")
    run_command("sudo npm install -g npm@latest")
    run_command("sudo npm install -g yarn")

def install_java():
    run_command("sudo apt install -y openjdk-17-jdk")

def install_docker():
    run_command("curl -fsSL https://get.docker.com -o get-docker.sh")
    run_command("sudo sh get-docker.sh")
    run_command("sudo usermod -aG docker $USER")
    run_command("sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
    run_command("sudo chmod +x /usr/local/bin/docker-compose")

def install_databases():
    # PostgreSQL
    run_command("sudo apt install -y postgresql postgresql-contrib")
    # MongoDB
    run_command("wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -")
    run_command("echo \"deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse\" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list")
    run_command("sudo apt update && sudo apt install -y mongodb-org")
    # MySQL
    run_command("sudo apt install -y mysql-server")

def main():
    install_packages()
    install_vscode()
    install_intellij()
    install_node()
    install_java()
    install_docker()
    install_databases()
    print("Installation complete. Please restart your system to apply all changes.")

if __name__ == "__main__":
    main()

