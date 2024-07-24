# Computer Programming: Python
- Course Instructor: `Anthoniran Amalanathan`

## Course Modules
- Problem Solving Basics
- Python Basics
- Control Strutures
- Collections
- Strings and Regular Expression
- Functions and File Handling
- Modules and Packages

## Set up Python and Visual Studio Code (VS Code)
### 1. **Install Python**
**a. Download Python:**
1. Visit the [official Python website](https://www.python.org/downloads/).
2. Download the latest version of Python for your operating system.

**b. Install Python:**
1. Run the downloaded installer.
2. On the installation screen, make sure to check the box that says "Add Python to PATH" (this is crucial for accessing Python from the command line).
3. Choose either the "Install Now" option or "Customize Installation" if you want to specify a different installation directory or add/remove components.
4. Complete the installation process.

**c. Verify Installation:**
1. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
2. Type `python --version`to check if Python is installed correctly and is accessible from the command line.

### 2. **Install Visual Studio Code**
**a. Download Visual Studio Code:**
1. Go to the [Visual Studio Code website](https://code.visualstudio.com/).
2. Download the installer for your operating system.

**b. Install Visual Studio Code:**
1. Run the downloaded installer.
2. Follow the prompts to complete the installation. You can keep the default settings or customize the installation as needed.

### 3. **Set Up Visual Studio Code for Python Development**
**a. Install Python Extension:**
1. Open Visual Studio Code.
2. Go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side or by pressing `Ctrl+Shift+X` (Cmd+Shift+X on macOS).
3. Search for the "Python" extension by Microsoft and install it. This extension provides Python language support, debugging, and other features.

**b. Configure Python Interpreter:**
1. Open the Command Palette by pressing `Ctrl+Shift+P` (Cmd+Shift+P on macOS).
2. Type and select "Python: Select Interpreter".
3. Choose the Python interpreter you installed earlier. If you're working with virtual environments, ensure to select the appropriate interpreter for your environment.

## Develop Python script using Visual Studio Code
### 1. **Create a Workspace Folder**
**a. Choose a Location:**
1. Decide where you want to create your workspace folder. This could be anywhere on your local disk, such as `D:\Projects` on Windows or `~/Projects` on macOS/Linux.

**b. Create the Folder:**
1. Open your file explorer (File Explorer on Windows, Finder on macOS, or your file manager on Linux).
2. Navigate to the desired location and create a new folder. You can name it something like `PythonWorkspace`.

### 2. **Open the Workspace in Visual Studio Code**
**a. Open Visual Studio Code:**
1. Launch Visual Studio Code.

**b. Open the Folder:**
1. Go to `File` > `Open Folder...`.
2. Navigate to the location where you created the `PythonWorkspace` folder, select it, and click `Select Folder` or `Open`.

### 3. **Create a Hello World Python Script**
**a. Create a New File:**
1. In Visual Studio Code, click on the `New File` icon in the Explorer pane or go to `File` > `New File`.
2. Name the file `hello_world.py`.

**b. Write the Python Script:**
1. Open the `hello_world.py` file and enter the following code:

    ```python
    print("Hello, World!")
    ```

2. Save the file (`Ctrl+S` or `Cmd+S` on macOS).

### 4. **Run the Hello World Script**
**a. Use the Integrated Terminal:**
1. Open the integrated terminal in Visual Studio Code by going to `Terminal` > `New Terminal` or pressing `` Ctrl+` `` (the backtick key).

**b. Run the Script:**
1. In the terminal, ensure you're in the `PythonWorkspace` directory. If not, navigate there using the `cd` command.
2. Run the script by typing:

    ```bash
    python hello_world.py
    ```

3. You should see the output `Hello, World!` printed in the terminal.