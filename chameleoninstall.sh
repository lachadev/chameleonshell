#!/usr/bin/env bash

# Chameleonshell Installer
REPO_URL="https://github.com/lachadev/chameleonshell.git"
APP_DIR="$HOME/chameleonshell"

echo "Installing Chameleonshell..."

# Detect OS
OS="$(uname -s)"

if [[ "$OS" == "Darwin" || "$OS" == "Linux" ]]; then
    # macOS or Linux
    echo "Detected OS: $OS"

    # Clone repo if not exists
    if [ ! -d "$APP_DIR" ]; then
        git clone "$REPO_URL" "$APP_DIR"
    else
        echo "Directory $APP_DIR already exists, pulling latest changes..."
        cd "$APP_DIR" && git pull
    fi

    # Install Python3 if not installed
    if ! command -v python3 &> /dev/null; then
        echo "Python3 not found. Please install Python3 and rerun the script."
        exit 1
    fi

    # Install dependencies
    cd "$APP_DIR"
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt

elif [[ "$OS" == "MINGW"* || "$OS" == "CYGWIN"* || "$OS" == "MSYS"* ]]; then
    # Windows Git Bash / Cygwin / MSYS
    echo "Detected Windows environment"

    # Clone repo if not exists
    if [ ! -d "$APP_DIR" ]; then
        git clone "$REPO_URL" "$APP_DIR"
    else
        echo "Directory $APP_DIR already exists, pulling latest changes..."
        cd "$APP_DIR" && git pull
    fi

    # Install Python3 if not installed
    if ! command -v python &> /dev/null; then
        echo "Python not found. Please install Python3 and rerun the script."
        exit 1
    fi

    # Install dependencies
    cd "$APP_DIR"
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
else
    echo "Unsupported OS: $OS"
    exit 1
fi

echo
echo "✅ Chameleonshell installed successfully!"
echo "To start it, run:"
echo
echo "  cd $APP_DIR && python3 shell.py"
echo
