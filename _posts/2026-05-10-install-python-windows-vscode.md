---
layout: post
title: "Installing Python on Windows with Python Manager and Visual Studio Code"
description: "A step-by-step walkthrough for installing Python on Windows, setting up Visual Studio Code, opening a project folder, adding Python extensions, and running a first script."
tags: [Python, Windows, Visual Studio Code, Setup, Tutorial]
comments: true
---

# Installing Python on Windows with Python Manager and Visual Studio Code

This walkthrough shows the full process for getting Python ready on a Windows computer. We will install Python from the official Python website, use Python Manager to install a Python runtime, install Visual Studio Code, create a small project folder, write a first script, and run it from the VS Code terminal.

By the end, the system should be able to:

- Install and manage Python versions with the `py` command.
- Open a Python project folder in Visual Studio Code.
- Write and run a basic `.py` file.
- Confirm Python is working from the terminal.

## 1. Download Python Manager from python.org

Start at the official Python website: [python.org](https://www.python.org/). From the Windows download area, choose the current Windows download option.

![Python download page]({{ "/assets/python-install/screenshot-2026-05-10-142244.png" | relative_url }})

The download used here is the Python Install Manager package. This installs the `py` command, which can then download and manage Python runtimes for you.

## 2. Install Python Install Manager

Open the downloaded Python Manager installer.

![Install Python Install Manager prompt]({{ "/assets/python-install/screenshot-2026-05-10-142259.png" | relative_url }})

Leave **Launch when ready** selected if you want Python Manager to open after installation, then select **Install Python**.

## 3. Let Python Manager configure the system

After the installer runs, Python Manager opens in a terminal window. It may report that the global commands directory is not configured yet.

![Python Manager terminal after install]({{ "/assets/python-install/screenshot-2026-05-10-142312.png" | relative_url }})

If Python Manager asks to add its command directory to `PATH`, allow it. This is what makes commands like `py` available from normal terminals.

You may see a message explaining that configuration changed and the terminal needs to be restarted before the new setting is available.

![Python Manager PATH message]({{ "/assets/python-install/screenshot-2026-05-10-142322.png" | relative_url }})

Close and reopen the terminal when prompted so Windows can load the updated environment variables.

## 4. Install the latest Python runtime

In the Python Manager terminal, install Python by running:

```powershell
py install
```

![Running py install]({{ "/assets/python-install/screenshot-2026-05-10-142335.png" | relative_url }})

When Python Manager asks whether to install CPython, type `y` and press **Enter**.

![Python Manager installing CPython]({{ "/assets/python-install/screenshot-2026-05-10-142355.png" | relative_url }})

CPython is the standard Python runtime most people mean when they say "Python." After it installs, Python Manager can show installed runtimes and available commands.

## 5. Download Visual Studio Code

Next, install a code editor. Go to the Visual Studio Code website and download the Windows installer.

![Visual Studio Code download page]({{ "/assets/python-install/screenshot-2026-05-10-142504.png" | relative_url }})

The downloads folder now contains both installers: the Python Manager package and the VS Code installer.

![Downloads folder with Python Manager and VS Code installers]({{ "/assets/python-install/screenshot-2026-05-10-142542.png" | relative_url }})

![Downloaded installer files]({{ "/assets/python-install/screenshot-2026-05-10-142609.png" | relative_url }})

## 6. Run the VS Code installer

Open the Visual Studio Code installer. On the license agreement screen, choose **I accept the agreement**, then select **Next**.

![VS Code license agreement]({{ "/assets/python-install/screenshot-2026-05-10-142629.png" | relative_url }})

Choose the install location. The default location is fine for most systems.

![VS Code destination folder]({{ "/assets/python-install/screenshot-2026-05-10-142637.png" | relative_url }})

Choose the Start Menu folder. Again, the default is usually fine.

![VS Code Start Menu folder]({{ "/assets/python-install/screenshot-2026-05-10-142644.png" | relative_url }})

On the additional tasks screen, enable the useful Explorer and PATH options:

- **Add "Open with Code" action to Windows Explorer file context menu**
- **Add "Open with Code" action to Windows Explorer directory context menu**
- **Register Code as an editor for supported file types**
- **Add to PATH**

![VS Code additional tasks]({{ "/assets/python-install/screenshot-2026-05-10-142652.png" | relative_url }})

Review the setup summary, then select **Install**.

![VS Code ready to install]({{ "/assets/python-install/screenshot-2026-05-10-142658.png" | relative_url }})

Wait for the installer to finish copying files.

![VS Code installing]({{ "/assets/python-install/screenshot-2026-05-10-142705.png" | relative_url }})

When setup completes, leave **Launch Visual Studio Code** selected and select **Finish**.

![VS Code setup complete]({{ "/assets/python-install/screenshot-2026-05-10-142732.png" | relative_url }})

## 7. Start Visual Studio Code

When VS Code opens for the first time, it may offer account sign-in or sync setup.

![Authorize Visual Studio Code account prompt]({{ "/assets/python-install/screenshot-2026-05-10-142755.png" | relative_url }})

Signing in is optional. You can continue without sign-in if you only want to write and run local Python files.

After that, VS Code opens to its welcome screen.

![VS Code welcome screen]({{ "/assets/python-install/screenshot-2026-05-10-142839.png" | relative_url }})

## 8. Restart Windows after PATH changes

Because both Python Manager and VS Code update command-line settings, restart Windows before continuing. This helps make sure new `PATH` entries are available everywhere.

![Windows restart menu]({{ "/assets/python-install/screenshot-2026-05-10-142853.png" | relative_url }})

After the restart, commands like `py` and `code` should be easier for Windows to find.

## 9. Optional: Run VS Code as administrator

If you want VS Code to open with administrator permissions, adjust the shortcut settings. Right-click the Visual Studio Code shortcut, open **Properties**, then select **Advanced**.

![VS Code shortcut properties]({{ "/assets/python-install/screenshot-2026-05-10-143058.png" | relative_url }})

![VS Code shortcut details]({{ "/assets/python-install/screenshot-2026-05-10-143108.png" | relative_url }})

In the Advanced Properties window, select **Run as administrator**, then choose **OK**.

![VS Code advanced properties]({{ "/assets/python-install/screenshot-2026-05-10-143113.png" | relative_url }})

This step is optional. For regular Python projects, VS Code does not usually need administrator permissions. Use it only when your workflow requires elevated access.

## 10. Create a Python project folder

Open File Explorer and create a folder for your Python work. In this example, the folder is:

```text
C:\repos\pythonintro
```

![Creating a Python project folder]({{ "/assets/python-install/screenshot-2026-05-10-143309.png" | relative_url }})

Inside that folder, create a new Python file named:

```text
intro.py
```

![intro.py created in project folder]({{ "/assets/python-install/screenshot-2026-05-10-143337.png" | relative_url }})

You can create the file from the Explorer context menu.

![Creating a new file from the context menu]({{ "/assets/python-install/screenshot-2026-05-10-143353.png" | relative_url }})

## 11. Open the folder in VS Code

Open Visual Studio Code and choose **Open Folder**.

![Open folder in VS Code]({{ "/assets/python-install/screenshot-2026-05-10-143406.png" | relative_url }})

When VS Code asks whether you trust the authors of the files in the folder, choose **Yes, I trust the authors** for folders you created yourself.

![Trust folder prompt]({{ "/assets/python-install/screenshot-2026-05-10-143411.png" | relative_url }})

VS Code then opens the folder and shows `intro.py` in the Explorer.

## 12. Write a first Python script

Open `intro.py` and add a small test script:

```python
print("Python is working!")

# Let's also test variables and math
x = 10
y = 20
print("x + y =", x + y)

# And test importing a module
import math
print("Square root of 16 is", math.sqrt(16))
```

![First Python script in intro.py]({{ "/assets/python-install/screenshot-2026-05-10-143529.png" | relative_url }})

This script checks three important pieces:

- Python can run a file.
- Variables and arithmetic work.
- The standard library can be imported.

## 13. Install the Python extension for VS Code

Open the Extensions view in VS Code and search for **Python**. Install the official Python extension published by Microsoft.

![Python extension in VS Code]({{ "/assets/python-install/screenshot-2026-05-10-143553.png" | relative_url }})

The Python extension gives VS Code language support, interpreter selection, debugging, and run commands for Python files.

![Python extension install button]({{ "/assets/python-install/screenshot-2026-05-10-143604.png" | relative_url }})

## 14. Open the Python project folder from the extension prompt

VS Code may show a Python welcome panel with an **Open Project Folder** button. Use it to open the folder where `intro.py` lives.

![Python extension open project folder prompt]({{ "/assets/python-install/screenshot-2026-05-10-143633.png" | relative_url }})

Select the folder you created earlier.

![Selecting the pythonintro folder]({{ "/assets/python-install/screenshot-2026-05-10-143705.png" | relative_url }})

## 15. Install a package management helper

In the Extensions view, search for Python package tools. This example installs **Pip Manager**, which gives a visual interface for working with Python packages.

![Pip Manager extension page]({{ "/assets/python-install/screenshot-2026-05-10-143758.png" | relative_url }})

You may also see related package tools in the Extensions list.

![Python package extensions list]({{ "/assets/python-install/screenshot-2026-05-10-143807.png" | relative_url }})

This is not required for running Python, but it can make package management easier while learning.

## 16. Review and run the script

Return to `intro.py` and make sure the file is saved.

![intro.py open in VS Code]({{ "/assets/python-install/screenshot-2026-05-10-143831.png" | relative_url }})

Open the VS Code terminal with **Terminal > New Terminal**. From the project folder, run:

```powershell
py intro.py
```

If your terminal is already pointed at the project directory, this runs the script directly.

![Running intro.py in the VS Code terminal]({{ "/assets/python-install/screenshot-2026-05-10-143850.png" | relative_url }})

The output should look like this:

```text
Python is working!
x + y = 30
Square root of 16 is 4.0
```

![Successful Python output in terminal]({{ "/assets/python-install/screenshot-2026-05-10-143906.png" | relative_url }})

## 17. Confirm Python runs from the command line

The final screenshot shows the script running successfully through the Python launcher. This confirms that Windows can find Python and that the project file runs correctly.

![Final terminal confirmation]({{ "/assets/python-install/screenshot-2026-05-10-143913.png" | relative_url }})

At this point, Python is installed, Visual Studio Code is installed, the Python extension is active, and a first script runs successfully.

## Common checks if something does not work

If `py intro.py` does not run, try these checks:

- Restart Windows so the updated `PATH` settings are loaded.
- Open a new VS Code terminal after installing Python.
- Run `py --list` to see which Python versions are installed.
- Run `py install` again if no Python runtime appears.
- Confirm the terminal is inside the folder that contains `intro.py`.
- Confirm the file is named `intro.py`, not `intro.py.txt`.

Once those checks pass, the system is ready for Python development.


