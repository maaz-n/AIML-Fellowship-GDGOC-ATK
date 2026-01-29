## Task 4

This repository contains small Python programs that I created while practicing Python modules, packages and virtual environments.

---

### 1. module.py

This file demonstrates how I used my own modules for **file handling** and
**basic arithmetic operations**.

#### What this program does:
- Writes text to a file (`test.txt`)
- Reads and displays the file content
- Performs basic calculations on two numbers (7 and 2)

#### How to run:
```bash
python3 module.py
````

---

### 2. requirements.txt

This file contains the external dependencies used in the project.

I created a virtual environment in the same directory and installed the **discord** package.

#### Install dependencies:

```bash
pip install -r requirements.txt
```

---

### 3. Decimal ➡️ Binary Converter Package

This is a custom Python package I created to practice building and installing
my own packages using pip.

#### Features:

* Converts decimal numbers to binary

#### Example usage:

```python
from dec_bin_converter import dec_to_bin

print(dec_to_bin(10))      # Output: 1010
```

### Local installation:

```bash
pip install -e .
```

---

### What I learned

* This project helped me understand Python package structure and imports better
* Make sure the virtual environment is activated before running the code

