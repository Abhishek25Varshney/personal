
Below is an example **README.md** file that you can include in your project directory. Adjust the instructions as needed based on your specific project setup.

---

# HTML Encryption Desktop App

This application allows you to encrypt HTML files using a password, producing a base64-encoded ciphertext that can be embedded into a loader HTML page. Users can then enter the password to decrypt and view the original content.

## Features

- **Easy Encryption:** Use a friendly GUI to select an input HTML file, enter a password, and save the encrypted output.
- **Password Protection:** Ensures that only users with the correct password can view the decrypted HTML content.
- **Stand-alone Executable:** Build a stand-alone `.exe` (or binary for other platforms) that doesn’t require Python to be installed on the target system.

## Requirements

- **Python 3.7+** (for development and building the executable)
- **Dependencies:**
  - `cryptography`
  - `tkinter` (included with standard Python installations on most platforms)
  - `pyinstaller` (for packaging)

If you're only running the standalone executable, no additional software is required.

## Installation (Development Environment)

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install Dependencies:**
   ```bash
   pip install cryptography
   ```
   ```bash
   pip install pyinstaller
   ```

   *Note: tkinter usually comes with Python, so it may not need to be listed.*

3. **Test the Application (Before Packaging):**
   ```bash
   python desktop_app.py
   ```
   This will open the GUI. Select an HTML file, provide a password, and generate the encrypted output.

## Building the Standalone Executable

1. **Ensure PyInstaller is Installed:**
   ```bash
   pip install pyinstaller
   ```

2. **Build the Executable:**
   ```bash
   pyinstaller --onefile --windowed desktop_app.py
   ```
   - `--onefile`: Packages everything into a single executable.
   - `--windowed` (or `--noconsole`): Hides the console window behind the GUI.

3. **Find the Output:**
   After running the above command, you’ll find your executable inside the `dist` folder. For Windows, it will be `desktop_app.exe`.

## Running the Standalone Executable

- On Windows:
  ```bash
  dist\desktop_app.exe
  ```
  
  Double-click the executable or run it from File Explorer.

- On macOS/Linux (after adjusting build steps accordingly):
  ```bash
  ./dist/desktop_app
  ```
  
  If blocked by security settings on macOS, you may need to allow the app to run in System Preferences > Security & Privacy.

## Using the Application

1. **Input File:** Click "Browse" to select the HTML file you want to encrypt.
2. **Output File:** Click "Browse" to choose where to save the encrypted text (e.g., `encrypted.txt`).
3. **Password:** Enter the password that will be required to decrypt this file on the client side.
4. **Encrypt:** Click the "Encrypt" button. The encrypted text will be saved to your chosen file and shown in the text area.
5. **Integrate with Loader:** Copy the resulting encrypted text and paste it into the `loader.html` at the placeholder location. When `loader.html` is viewed, the user will be prompted for the password to decrypt and view the original HTML content.

## Troubleshooting

- If the GUI fails to start, ensure that Python is installed correctly and that `tkinter` is available.
- For encryption errors, double-check that your input file is accessible and that you have permission to read it.
- If PyInstaller fails or the executable does not run on another machine, verify that all dependencies are correctly installed and that you built it on a compatible platform.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Adjust the above README as needed to fit your specific project configuration and workflow.
