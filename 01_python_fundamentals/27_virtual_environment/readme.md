# 📖 **Getting Started with Python Environments**

Welcome to this **simple overview** of Python environments. This will help you understand why using virtual environments can make your life easier when working on different Python projects. We’ll also look at how to install packages and keep track of your dependencies.

---

## 🌱 What Are Virtual Environments?

A **virtual environment** is like a mini version of Python, just for one project. It has its own place to store packages (libraries) and doesn’t mess with other projects on your system.

### Why Use a Virtual Environment?
- **Security**: You don’t need special (admin or superuser) permissions to install packages, reducing risks of installing malware.
- **No Conflicts**: Each project can have specific package versions without affecting other projects.
- **Easier Upgrades**: Updating a package in one project won’t break other projects’ code.
- **Clearer Dependencies**: You can list exactly which packages your project needs, making everything tidy.

---

## 🛠 How to Manage Packages

### PyPI and Conda-Forge
- **PyPI** (Python Package Index) is the main place to find Python libraries. You’ll often use `pip install <package_name>` to get them.
- **Conda-Forge** is linked to the **Anaconda** ecosystem. You can install packages with `conda install <package_name>`.

### Examples of Installing Packages
```bash
# Using pip
pip install requests

# Using conda
conda install requests
```

---

## 📜 Tracking Dependencies

It’s important to keep track of all the libraries your project needs. This helps you (and others) to recreate the same environment later. Common ways include:

- A simple `requirements.txt` file (used with `pip`).
- A `Pipfile` (used with `pipenv`).
- A `pyproject.toml` (used with `poetry`).

---

## 🤔 Quick Example

Imagine you have a **Django** web project that needs version `3.2` of Django. Another project might need version `4.1`. If you installed Django globally, you’d only have one version on your system. This could cause a problem if one project needs the older version.

**Solution**: Create a virtual environment for each project:
1. Project A uses Django 3.2
2. Project B uses Django 4.1

No conflicts! Both can run on the same computer without clashing.

---

# 🏗 What Are `venv` and `virtualenv`?

- **`virtualenv`**: A library that creates virtual environments for your Python projects.
- **`venv`** (available by default in Python 3.3+): A built-in tool that acts almost like a drop-in replacement for `virtualenv`.

Both help you avoid conflicts between different projects’ dependencies.

---

## 📂 Where Should You Put Your Environment?

Instead of creating your `env` (or `.venv`, `venv`) **inside** the project folder, you can keep it somewhere else. Why?

1. **Faster & Lighter Backups**  
   If you keep the environment **outside** your main project, you don’t waste time and space backing up all the installed packages again and again.

2. **Portability**  
   You can move or share your project without dragging along its virtual environment. This means you can store your project on a flash drive or remote drive and keep it super portable.

3. **No Source Control Bloats**  
   Virtual environment files can clutter your version control system (like Git). If the environment is outside the project, you won’t risk accidentally uploading these files.

> **Tip**: If you do keep the environment in your project, remember to add the environment folder (for example, `.venv`) to your `.gitignore` or similar files so it’s not committed to source control.

---

# 🌐 Creating a `venv` – Simple Guide

Below is a quick, **beginner-friendly** overview of how to create and activate a Python virtual environment on different operating systems. We’ll also look at some important points to keep in mind. Don’t worry if you’re new; this guide will walk you through the basics!

---

## 📂 Current Location

> **Your location**: `DELL` on `~/Desktop/Python-Deep-Dive` (main branch)

This means you’ll likely be running commands from:
```
~/Desktop/Python-Deep-Dive
```
But feel free to adjust paths to fit your own folder structure.

---

## 🏗 Steps to Create and Activate a `venv`

### 1. Linux/Unix/macOS
Using **zsh** or **bash**:
```bash
# Step 1: Create the virtual environment
python3 -m venv envs/your_env

# Step 2: Activate the environment
source envs/your_env/bin/activate

# After this, you'll see a prompt like:
(your_env) $
```
- **(your_env)** in front of your prompt indicates you’re in the virtual environment.

### 2. Windows (cmd.exe)
```cmd
# Step 1: Create the virtual environment
python.exe -m venv envs\your_env

# Step 2: Activate the environment
envs\your_env\Scripts\activate.bat

# Prompt will change to:
(your_env) C:\Users\YourName>
```

### 3. Windows (PowerShell)
```powershell
# Step 1: Create the virtual environment
python.exe -m venv envs\your_env

# Step 2: Activate the environment
envs\your_env\Scripts\Activate.ps1

# Prompt will change to:
(your_env) PS C:\Users\YourName>
```

> **Note**: If you run into permission issues in PowerShell, you might need to adjust the execution policy:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## ⚠️ Important Notes

1. **No `sudo` Required**  
   You do **not** need superuser privileges (like `sudo`) to create or activate virtual environments. Using `sudo` can be a security risk.

2. **Install Missing Packages**  
   - If you’re on Ubuntu, you might need to install:
     ```bash
     sudo apt-get update
     sudo apt-get install python3-venv
     ```
     because Ubuntu’s default Python sometimes excludes `ensurepip`.

3. **Venv vs Virtualenv**  
   - **`venv`** is built into Python 3.3+.
   - **`virtualenv`** is an external library that offers similar functionality.
   - Either one works, but `venv` is often preferred if you’re already on Python 3.3+.

4. **Why the `(your_env)` Prefix?**  
   - It helps you see that you’re “inside” a virtual environment. Any `python` or `pip` commands will only affect this environment.

---

# 🌐 Using `virtualenv` (Instead of `venv`) – Simple Overview

Below is a **friendly guide** to help you create and activate Python virtual environments using **`virtualenv`**. It also shows you how to specify different Python interpreter versions!

---

## 📍 Your Current Directory
> **Location**:  
> `C:\Users\DELL\Desktop\Python-Deep-Dive\01_python_fundamentals\27_virtual_environment>`

This means your commands will be run from:
```
C:\Users\DELL\Desktop\Python-Deep-Dive\01_python_fundamentals\27_virtual_environment>
```
Feel free to adapt the path to match your folder names.

---

## 🤔 Why `virtualenv`?

- You can easily specify which **Python version** to use (e.g., `python3.8`).
- It’s an alternative to `venv`, especially handy if you’re on older Python versions or want more flexibility.

---

## 🔨 Creating a Virtual Environment with `virtualenv`

1. **Basic Command**  
   ```bash
   virtualenv envs/your_env
   ```
   - This works just like `python3 -m venv envs/your_env`.

2. **Choosing a Specific Python Version**  
   ```bash
   virtualenv -p python3.8 envs/your_env
   ```
   or  
   ```bash
   virtualenv --python=python3.8 envs/your_env
   ```
   - This will create a new environment using **Python 3.8**.  

> **Alternatively**, if you’re using `venv`, you can do:
> ```bash
> python3.8 -m venv envs/your_env
> ```
> But that’s a slightly different syntax than `virtualenv`.

---

## 🚀 Activating Your Environment

Once you create your virtual environment, you need to **activate** it before installing packages or running Python scripts inside it.

### 🐧 Linux/Unix (bash or zsh)
```bash
source envs/your_env/bin/activate
(your_env) $
```

### 🪟 Windows (cmd.exe)
```cmd
envs\your_env\Scripts\activate.bat
(your_env) C:\Users\YourName>
```

### 🔹 Windows (PowerShell)
```powershell
envs\your_env\Scripts\Activate.ps1
(your_env) PS C:\Users\YourName>
```

> **Tip**: The `(your_env)` prefix indicates you’re inside the virtual environment!

---

## 🎉 Why Activate?

**When activated**, your system’s `PATH` is updated so that:
1. Any `python` or `pip` command now refers to **your_env**’s Python and pip.  
2. Your prompt changes to `(your_env)`—a clear reminder you’re using a separate environment.

---

# 🚀 Installing Packages in Your Virtual Environment

Below is a **simple** explanation of how to install Python packages inside a virtual environment, see which packages you’ve installed, and optionally share packages between your system and your virtual environment.

---

## 🍃 Isolated Package Installs

### Basic Installation
When your virtual environment is **activated**, you can install packages as usual:
```bash
pip3 install <package>
```
All installed packages are kept **separate** from your system’s global Python packages.

### Listing Installed Packages
```bash
pip3 freeze
```
You’ll see only the packages (and dependencies) installed **in** your virtual environment – no extra clutter.

---

## 🔗 Using System Packages (Optional)

Sometimes, you might want your environment to access **system** packages (for example, you have a system-installed package that you don’t want to reinstall). In that case, you can create the environment like this:
```bash
python.exe -m venv --system-site-packages envs/your_env
```
This tells Python to **append** system packages to your environment’s search path:
- If a package isn’t found in the environment, Python will check your system’s global packages.

### Listing Only Local Packages
If you choose to allow system packages, your `pip3 freeze` might show **everything**, including system-wide packages. To limit the listing to **just** local packages:
```bash
pip3 freeze --local
```
You’ll then see only the packages actually installed in your virtual environment, ignoring any system-wide packages.


Explicitly installing or updating a package within your virtual environment will effectively
hide the system package from within your virtual environment. Uninstalling the package
from your virtual environment will make it reappear.

---

# 📦 **Managing Dependencies with `pip` and `requirements.txt`**

## 🗂 1. Storing Dependencies in `requirements.txt`

A **requirements.txt** file is the most straightforward way to keep track of your Python dependencies. It typically lives in your project’s root folder and contains lines like:
```
requests==2.31.0
django==4.2
```
Each line represents a package (and optionally a version restriction).

### Creating It Manually

You can create **requirements.txt** by hand. For example:
```
django==4.2
requests>=2.0.0
numpy
```
> This file is simply text, so you can include comments (using `#`), version specifiers, or placeholders.

### Creating It Automatically with `pip freeze`

If you already have packages installed in a virtual environment, you can **generate** a `requirements.txt`:
```bash
# While inside your activated virtual environment
pip3 freeze > requirements.txt
```
- This writes all installed packages **and** their versions to `requirements.txt`.
- You can then **edit** the file to remove packages you don’t actually need or to adjust version constraints.

---

## 🔧 2. Installing Packages from `requirements.txt`

Once you have `requirements.txt`, you (or anyone else) can install all its packages in a new, empty virtual environment with:
```bash
pip3 install -r requirements.txt
```

### Updating a Requirements File

Suppose you install a new package or upgrade an existing one:
```bash
pip3 install progressbar2
```
Next, see what changed compared to your `requirements.txt`:
```bash
pip3 freeze -r requirements.txt
```
This shows you lines that were **added** (or changed). If you’re satisfied, you can **append** or **merge** those changes into your `requirements.txt`.

---

## 🏷 3. Understanding Version Specifiers

### Pinning Versions Exactly

When you see lines like:
```
progressbar2==3.47.0
```
You’re **pinning** the package version. This ensures **exactly** that version is installed, which is useful if you want to **freeze** your environment so it’s 100% reproducible.

### More Flexible Versions

1. **Greater Than or Equal (>=)**  
   ```bash
   progressbar2>=3.47.0
   ```
   This means **at least** version `3.47.0`. Newer versions (3.47.1, 3.48, etc.) are allowed.

2. **Excluding Specific Versions (!=)**  
   ```bash
   progressbar2>=3.46,!=3.47.0
   ```
   This means “version **at least** 3.46, but **not** 3.47.0,” in case a bug exists in that specific release.

3. **Wildcards**  
   ```bash
   progressbar2==3.47.*
   ```
   This installs versions like `3.47.0`, `3.47.1`, etc., but **not** `3.48.0`.

4. **Compatible Release Operator (~=)**  
   ```bash
   progressbar2~=3.47.1
   ```
   This is shorthand for:
   ```bash
   progressbar2>=3.47.1,==3.47.*
   ```
   Meaning it installs **at least** `3.47.1`, but won’t upgrade to `3.48.x` or higher.

---

## 🏷 4. Example Use Cases

### Pinning Everything (Exact Versions)

**Pros**: Perfect reproducibility  
**Cons**: Potentially no security updates unless you manually bump the version

```bash
django==4.2
requests==2.31.0
progressbar2==3.47.0
```

### Partial Pinning (Lower Bound)

**Pros**: Gets security patches but ensures minimum tested version  
**Cons**: Could break in the future if a big update changes APIs

```bash
django>=4.2
requests>=2.0
progressbar2~=3.47.1
```

### Handling a Bad Version

If a release is broken:
```bash
progressbar2>=3.46,!=3.47.0
```
This means “3.46 or above, but skip exactly 3.47.0.”

---

## 💡 5. Advanced Tips

1. **Multiple Requirements Files**:  
   - You can have a `requirements.txt` and a separate `dev-requirements.txt` for developer tools and testing libraries.  
   - `pip3 install -r dev-requirements.txt -r requirements.txt`.

2. **Comments & Documentation**:  
   - Feel free to add **comments** explaining why certain versions are pinned:
     ```bash
     # We skip 3.47.0 due to a known bug
     progressbar2>=3.46,!=3.47.0
     ```

3. **Comparing Versions**:  
   - Use `pip freeze -r requirements.txt` to see newly added or changed packages.

---

#  **Installing Packages from Source Repositories** 📚

## 1. Installing Packages Directly from a Git Repository 🐙

Sometimes, a package fix **hasn’t** been officially released, but you need it right away. If the fix exists on a repository’s **development** branch (or any branch/tag/commit), you can install from source.

### Basic Example

```bash
pip3 install --editable \
  git+https://github.com/WoLpH/python-progressbar.git@develop#egg=progressbar2
```

**Detailed Explanation**:
- **`pip3 install`**: Standard pip installation command.
- **`--editable`** or `-e`:  
  - Tells pip to **clone** the repository into your environment’s `src/` folder.  
  - Allows you to **re-run** the command later to pull the latest changes from the repo (e.g., if more commits were made).  
  - Lets you **edit** the source code in place. Super handy for:
    - **Debugging** or exploring how the library works.  
    - **Contributing** a pull request back to the library.
- **`git+https://github.com/WoLpH/python-progressbar.git@develop#egg=progressbar2`**:  
  - `git+<URL>`: The **Git** protocol prefix so pip knows to treat it like a Git repo.  
  - `@develop`: Specifies which **branch** (or commit/tag) to install from.  
  - `#egg=progressbar2`: Tells pip the **package name**.

> **Tip**: The `@develop` part can be replaced with any **branch**, **tag**, or **commit hash** you want. Perfect for grabbing exactly the code you need! 💡

### Other Version Control Systems

Besides **Git**, pip supports installing from:
- **Mercurial** (`hg+<URL>`)
- **Subversion** (`svn+<URL>`)
- **Bazaar** (`bzr+<URL>`)

Syntax is similar; just replace `git+` with `hg+`, `svn+`, or `bzr+`. 🗃

---

## 2. Extras: Installing Optional Dependencies 🍱

Some packages provide **optional features** that require additional dependencies. These features are grouped under **“extras”**. Think of it like a buffet 🍛—you can pick and choose the extra pieces you want!

### Basic Syntax

```bash
pip3 install "package_name[extra1, extra2]"
```
- The **square brackets** follow the core package’s name.
- Separate multiple extras with commas.

### Example 1: `progressbar2`

```bash
pip3 install "progressbar2[docs,tests]"
```
- **docs** extra: Installs documentation-building tools (like `Sphinx`).  
- **tests** extra: Installs test framework dependencies (like `pytest`).

### Example 2: `requests`

```bash
pip3 install "requests[security]"
```
- The **security** extra includes additional libraries (e.g., `pyOpenSSL`) for more secure connections.

**Detailed Explanation**:
- Packages define **extras** in their setup or configuration files.  
- Installing with **extras** ensures those additional dependencies are fetched at the same time, so you don’t have to install them manually one by one. 🎉

---

## 3. Conditional Dependencies (Environment Markers) ⚙️

If your library **only** needs certain dependencies on **Windows** or if it **only** needs a special library for Python versions below 3.7, you can use **environment markers**. They let you conditionally specify dependencies based on factors like:

- Operating System  
- Python Version  
- CPU Architecture  
- …and more!

### Example 1: Windows-Only Dependency

```bash
pywin32!=226; platform_system == "Windows"
```

**Detailed Explanation**:
- `pywin32` is a package that provides Windows-specific functionalities.  
- `!=226`: Excludes version `226` due to a known bug. 🐞  
- `platform_system == "Windows"`: Only install `pywin32` if you’re on Windows.

### Example 2: Python Version Condition

```bash
dataclasses; python_version < '3.7'
```

**Detailed Explanation**:
- The `dataclasses` module is built into Python 3.7+.  
- If your project must run on older Python versions (3.6 or below), you need the backport from PyPI.  
- This marker ensures **only** Python 3.6 (or older) will install the `dataclasses` library.

### Common Markers

- **`platform_system`**: `'Windows'`, `'Linux'`, `'Darwin'`  
- **`python_version`**: e.g., `<= '3.6'`  
- **`platform_machine`**: e.g., `'x86_64'`  
- **`platform_python_implementation`**: e.g., `'CPython'`, `'PyPy'`  

> For more, see [PEP 508 (environment markers)](https://peps.python.org/pep-0508/) and [PEP 440 (versioning)](https://peps.python.org/pep-0440/). 📝

---

## 4. Storing These Dependencies in `requirements.txt` or Setup Files 📄

### In `requirements.txt`

You can specify extras or VCS installs **directly** in `requirements.txt`:

```txt
-e git+https://github.com/WoLpH/python-progressbar.git@develop#egg=progressbar2
progressbar2[docs,tests]
pywin32!=226; platform_system == "Windows"
dataclasses; python_version < '3.7'
```

Then install everything with:
```bash
pip3 install -r requirements.txt
```
(It’s that easy! ✨)

### In `setup.py` or `pyproject.toml`

If you’re building a **distributable** Python package, you can place these markers and extras in your **setup** configuration so that when others install your package, they also see these optional or conditional dependencies. Tools like **Poetry** or **pipenv** let you define these conditions in a structured format.

---