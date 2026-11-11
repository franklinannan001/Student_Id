# MKSU Student ID Generator

A lightweight Python command-line utility that automatically generates formatted student identification numbers based on a student's full name and enrollment year.

## 📋 Overview

This script takes a student's first and last name along with their four-digit enrollment year, extracts their initials, and outputs a standardized ID in the format `MKSU/F.L./YY`. 

*(Note: Designed for Machakos University (MKSU) ID formatting).*

## ✨ Features

- **Automatic Initial Extraction:** Converts full names to uppercase and extracts the first and last initials.
- **Year Formatting:** Automatically converts a four-digit enrollment year (e.g., `2026`) into a two-digit suffix (`26`).
- **Input Error Handling:** Safely handles non-integer inputs for the enrollment year without crashing.

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** installed on your system. No external libraries or dependencies are required.

### Installation

1. Clone the repository or download the Python script (`main.py`):
   ```bash
   git clone https://github.com
   cd mksu-student-id-generator
   ```

## 💻 Usage

Run the script from your terminal or command prompt:

```bash
python main.py
```

### Example

```text
Full Name: Jane Doe
Enrollment Year: 2026
Your student ID is: MKSU/J.D./26
```

## 🛠️ Code Structure

- `main()`: Handles user prompts, validates integer input for the year, and prints the final student ID.
- `get_initials(name)`: Splits a two-part name string and returns formatted initials (e.g., `J.D.`).
- `generate_id(initials, enrollment_year)`: Combines the institution prefix, initials, and the last two digits of the enrollment year.

## ⚠️ Known Limitations

- **Two-Name Requirement:** The `get_initials()` function expects strictly two space-separated names (First and Last). Entering a single name or three names (e.g., including a middle name) will raise a `ValueError`.
- **Silent Failure on Invalid Year:** Entering text instead of numbers for the enrollment year currently exits silently without notifying the user.
- **Single-Digit Year Padding:** Years ending in `00`–`09` (e.g., `2005`) will output as single digits (`5` instead of `05`) due to standard modulo arithmetic (`% 100`).
