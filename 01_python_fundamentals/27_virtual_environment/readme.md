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


# 🚀 **Automatic project management using poetry** 🐍

Poetry is a powerful and user-friendly tool for managing Python projects. It simplifies tasks like dependency management, virtual environments, and project configuration, making it an excellent choice for developers. This detailed guide explains how to use Poetry to create, manage, and share Python projects, with a focus on building a Django web application. Let’s dive in! 🎉

---

## 📖 What is Poetry?

Poetry is a modern Python dependency management tool that automates repetitive tasks, allowing you to focus on coding. It:

- 📦 Manages project dependencies (libraries) and their versions.
- 🌐 Creates and manages virtual environments automatically.
- 📝 Generates a `pyproject.toml` file to store project metadata.
- 🔒 Uses a `poetry.lock` file to ensure consistent library versions across systems.
- ⚡ Speeds up workflows with intuitive commands.

Whether you're building a small script or a complex web app, Poetry keeps your project organized and reproducible. Let’s explore how to use it step by step! 🚀

---

## 🛠️ Step-by-Step Guide to Using Poetry

### 1️⃣ **Creating a New Poetry Project**

To start a Python project, use the `poetry init` command. This launches an interactive wizard that helps you configure your project.

**Command:**

```bash
poetry init
```

**What Happens?**

- Poetry generates a `pyproject.toml` file, which serves as the central configuration file for your project.
- It prompts you to provide details such as:
  - **Package name**: The name of your project (defaults to the current directory name).
  - **Version**: The initial version (defaults to `0.1.0`).
  - **Description**: A brief summary of your project.
  - **Author**: Your name and email (pulled from Git settings if available).
  - **License**: The license for your project (e.g., MIT).
  - **Python version**: The minimum Python version required (e.g., `>=3.12`).
  - **Dependencies**: Whether to add libraries interactively (you can skip this and add them later).

**Example Interaction:**

```bash
$ poetry init
Package name [my_project]: my_project
Version [0.1.0]: 
Description []: A Django-based web application
Author [Jane Doe <jane@example.com>, n to skip]: 
License []: MIT
Compatible Python versions [>=3.12]: 

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
```

**Output:** `pyproject.toml`Poetry creates a `pyproject.toml` file with the provided details:

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A Django-based web application"
authors = [
    {name = "Jane Doe", email = "jane@example.com"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

**💡 Tip**: If Poetry doesn’t auto-fill your author details, set them in Git:

```bash
git config --global user.name "Jane Doe"
git config --global user.email "jane@example.com"
```

---

### 2️⃣ **Adding Dependencies**

Once your project is set up, you can add libraries (dependencies) like Django for a web app.

**Command:**

```bash
poetry add django
```

**What Happens?**

- Poetry:
  - Creates a **virtual environment** if one doesn’t exist (a separate space for your project’s libraries).
  - Installs the latest compatible version of Django and its dependencies (e.g., `asgiref`, `sqlparse`).
  - Updates the `pyproject.toml` file to include Django in the `dependencies` section.
  - Generates or updates the `poetry.lock` file to lock the exact versions of all installed libraries.

**Example Output:**

```bash
$ poetry add django
Creating virtualenv my_project-puycRGil-py3.12 in C:\Users\YourName\AppData\Local\pypoetry\Cache\virtualenvs
Using version ^5.2 for django

Package operations: 4 installs, 0 updates, 0 removals
  - Installing asgiref (3.8.1)
  - Installing sqlparse (0.5.3)
  - Installing tzdata (2025.2)
  - Installing django (5.2)

Writing lock file
```

**Updated** `pyproject.toml`**:**

```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A Django-based web application"
authors = [
    {name = "Jane Doe", email = "jane@example.com"}
]
license = {text = "MIT"}
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "django (>=5.2,<6.0)"
]

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"
```

**The** `poetry.lock` **File**:The `poetry.lock` file records:

- **Exact versions** of all libraries (e.g., `django == 5.2`).
- **File hashes** for security (to verify the downloaded files).
- **Sub-dependencies** required by Django.

Example snippet:

```toml
[[package]]
name = "django"
version = "5.2"
description = "A high-level Python web framework..."
python-versions = ">=3.10"
groups = ["main"]
files = [
    {file = "Django-5.2-py3-none-any.whl", hash = "sha256:91ceed..."},
    {file = "Django-5.2.tar.gz", hash = "sha256:1a47f..."},
]
```

This ensures that anyone using your project gets the same library versions, preventing version conflicts. 🔐

---

### 3️⃣ **Activating the Virtual Environment**

Poetry automatically manages a virtual environment for your project, keeping its libraries isolated from other projects.

**Command:**

```bash
poetry env activate
```

**What Happens?**

- Activates the virtual environment, so commands like `python` or `pip` use the project’s isolated environment.
- Your terminal prompt changes to show you’re inside the virtual environment.

**Alternative**:Run commands without activating the environment using:

```bash
poetry run <command>
```

Example:

```bash
poetry run python --version
```

**💡 Tip**: Use `poetry shell` for interactive work (e.g., running multiple commands) and `poetry run` for one-off commands.

---

### 4️⃣ **Creating a Django Project**

With Django installed, let’s create a Django project.

**Command:**

```bash
poetry run django-admin startproject myproject .
```

**What Happens?**

- Creates a Django project named `myproject` in the current directory (the `.` ensures it uses the current folder).
- Generates core Django files like:
  - `manage.py`: The command-line utility for managing your project.
  - `myproject/settings.py`: Configuration settings.
  - `myproject/urls.py`: URL routing.

**Note**: Use `poetry run` to ensure the command runs in the virtual environment where Django is installed.

---

### 5️⃣ **Creating a Django App**

Django projects are modular, with “apps” handling specific features (e.g., a blog or user authentication).

**Command:**

```bash
poetry run python manage.py startapp myapp
```

**What Happens?**

- Creates a folder called `myapp` with files like:
  - `models.py`: For defining database models.
  - `views.py`: For handling HTTP requests and responses.
  - `apps.py`: For app configuration.
- The app is ready to be added to your project.

---

### 6️⃣ **Registering the App**

To use the app, register it in your Django project’s settings.

**Steps:**

1. Open `myproject/settings.py`.
2. Add `myapp` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Add your app here
]
```

**What Happens?**

- Django recognizes `myapp` and includes it in the project’s functionality.

---

### 7️⃣ **Running Migrations**

Django uses migrations to set up and update your database based on your app’s models.

**Commands:**

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

**What Happens?**

- `makemigrations`: Scans your `models.py` files for changes and creates migration files (instructions for updating the database).
- `migrate`: Applies those instructions to create or update database tables (e.g., for Django’s built-in user system).

**💡 Tip**: Always run migrations after modifying models to keep your database in sync.

---

### 8️⃣ **Running the Django Server**

Start the Django development server to see your project in action.

**Command:**

```bash
poetry run python manage.py runserver
```

**What Happens?**

- Launches a local web server at `http://127.0.0.1:8000/`.
- Open this URL in your browser to view your Django project (you’ll see a default “Welcome to Django” page unless you’ve customized it).

**💡 Tip**: Press `Ctrl+C` to stop the server.

---

### 9️⃣ **Rebuilding the Project on Another System**

To share your project or set it up on another computer, Poetry ensures the exact same environment is recreated.

**Command:**

```bash
poetry install --no-root
```

**What Happens?**

- Poetry reads the `pyproject.toml` and `poetry.lock` files.
- Installs the exact versions of libraries specified in `poetry.lock`.
- Sets up the virtual environment to match the original setup.
- The `--no-root` flag skips installing the project itself as a package (common for most workflows).

**💡 Tip**: Share the `pyproject.toml` and `poetry.lock` files with your code to ensure others can replicate your setup.

---

## 🌟 Why Use Poetry?

Poetry transforms Python project management by:

- **Automating Virtual Environments** 🛠️: No need to manually create or manage them.
- **Simplifying Dependency Management** 📦: Add, update, or remove libraries with a single command.
- **Ensuring Consistency** 🔒: The `poetry.lock` file guarantees the same library versions everywhere.
- **Streamlining Collaboration** 🤝: Share your project easily with reproducible setups.
- **Boosting Productivity** ⚡: Fast, intuitive commands save time.

---

## 📋 Summary of Key Commands

| Task | Command |
| --- | --- |
| Start a new project | `poetry init` |
| Add a library | `poetry add <library>` (e.g., `poetry add django`) |
| Activate virtual environment | `poetry shell` or `poetry run <command>` |
| Create a Django project | `poetry run django-admin startproject myproject .` |
| Create a Django app | `poetry run python manage.py startapp myapp` |
| Register an app | Add to `INSTALLED_APPS` in `settings.py` |
| Run migrations | `poetry run python manage.py makemigrations` and `migrate` |
| Start the server | `poetry run python manage.py runserver` |
| Rebuild project on new system | `poetry install --no-root` |

---

## 🛠️ Additional Tips

- **Update Dependencies** 🔄: Run `poetry update` to upgrade libraries to the latest compatible versions.
- **Remove a Library** 🗑️: Use `poetry remove <library>` to uninstall a library and update the configuration files.
- **Check Poetry Version** ℹ️: Run `poetry --version` to ensure you’re using the latest version.
- **Custom Python Version** 🐍: Specify a Python version during setup with `poetry init --python=3.11`.
- **Sharing Projects** 📤: Include `pyproject.toml`, `poetry.lock`, and your code when sharing your project.

---