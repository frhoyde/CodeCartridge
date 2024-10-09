import os
import subprocess
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing command: {command}")
        logging.error(f"Error details: {e}")

def install_packages():
    packages = [
        "curl",
        "wget",
        "apt-transport-https",
        "ca-certificates",
        "software-properties-common",
        "git",
        "neovim",
        "flameshot",
        "python3-pip"  # Added pip installation
    ]
    try:
        run_command(f"sudo apt update && sudo apt install -y {' '.join(packages)}")
        logging.info("Packages installed successfully")
    except Exception as e:
        logging.error(f"Failed to install packages: {e}")

def install_intellij():
    try:
        run_command("sudo tar -xzf ~/Downloads/intellij.tar.gz -C /opt/")
        run_command("sudo ln -s /opt/idea-*/bin/idea.sh /usr/local/bin/intellij")
        create_intellij_desktop_entry()
        logging.info("IntelliJ IDEA installed successfully")
    except Exception as e:
        logging.error(f"Failed to install IntelliJ IDEA: {e}")

def create_intellij_desktop_entry():
    desktop_entry = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon[en_US]=/opt/idea-*/bin/idea.png
Name[en_US]=IntelliJ IDEA
Exec=/usr/local/bin/intellij
Name=IntelliJ IDEA
Icon=/opt/idea-*/bin/idea.png
"""
    try:
        run_command(f"echo '{desktop_entry}' | sudo tee /usr/share/applications/intellij.desktop")
        run_command("sudo chmod 644 /usr/share/applications/intellij.desktop")
        run_command("sudo chown root:root /usr/share/applications/intellij.desktop")
        logging.info("IntelliJ IDEA desktop entry created successfully")
    except Exception as e:
        logging.error(f"Failed to create IntelliJ IDEA desktop entry: {e}")

def install_node():
    try:
        run_command("curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash")
        run_command("export NVM_DIR=\"$HOME/.nvm\" && [ -s \"$NVM_DIR/nvm.sh\" ] && \\. \"$NVM_DIR/nvm.sh\"")
        run_command("nvm install --lts")
        run_command("nvm use --lts")
        run_command("npm install -g npm@latest")
        run_command("npm install -g yarn")
        logging.info("Node.js (via nvm), npm, and yarn installed successfully")
    except Exception as e:
        logging.error(f"Failed to install Node.js (via nvm), npm, or yarn: {e}")

def install_java():
    try:
        run_command("sudo apt install -y openjdk-17-jdk")
        logging.info("Java installed successfully")
    except Exception as e:
        logging.error(f"Failed to install Java: {e}")

def install_docker():
    try:
        run_command("curl -fsSL https://get.docker.com -o get-docker.sh")
        run_command("sudo sh get-docker.sh")
        run_command("sudo usermod -aG docker $USER")
        run_command("sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
        run_command("sudo chmod +x /usr/local/bin/docker-compose")
        logging.info("Docker and Docker Compose installed successfully")
    except Exception as e:
        logging.error(f"Failed to install Docker or Docker Compose: {e}")

def install_databases():
    try:
        # PostgreSQL
        run_command("sudo apt install -y postgresql postgresql-contrib")
        logging.info("PostgreSQL installed successfully")
    except Exception as e:
        logging.error(f"Failed to install PostgreSQL: {e}")

    try:
        # MongoDB
        run_command("wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -")
        run_command("echo \"deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse\" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list")
        run_command("sudo apt update && sudo apt install -y mongodb-org")
        logging.info("MongoDB installed successfully")
    except Exception as e:
        logging.error(f"Failed to install MongoDB: {e}")

    try:
        # MySQL
        run_command("sudo apt install -y mysql-server")
        logging.info("MySQL installed successfully")
    except Exception as e:
        logging.error(f"Failed to install MySQL: {e}")

def append_to_file(file_path, line):
    try:
        run_command(f"sudo sh -c 'echo \"{line}\" >> {file_path}'")
        logging.info(f"Successfully appended line to file")
    except Exception as e:
        logging.error(f"Failed to append line to file: {e}")

def main():
    install_packages()
    install_intellij()
    install_node()
    install_java()
    install_docker()
    install_databases()
    
    # Example usage of append_to_file function
    
    logging.info("Installation complete. Please restart your system to apply all changes.")

if __name__ == "__main__":
    main()
