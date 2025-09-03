# foldchangeviz

**foldchangeviz** is a Python package and command-line tool for visualizing fold change heatmaps from screening data. It provides both a **GUI** for interactive use, or can be used as a command line tool. 

---

## Features

- Generate fold change heatmaps from CSV files
- Mark values within 3 standard deviations of template wells with a red `X`
- Mask low-intensity wells in black
- Supports both GUI and CLI usage
- Save plots as high-resolution PNGs

---

## Installation

1. Open a Command Prompt or powershell terminal. You should see something like this:
```
C:\Users\[your name]>
``` 

3. Clone the repository by copying and pasting this after the "C:\Users\[your name]>" in the command prompt:

```
git clone https://github.com/rashepherd/foldchangeviz.git
cd foldchangeviz
```

4. Create a Python virtual environment:

```
pyhton -m venv venv
```

5. Activate the virtual environment:

```
venv\Scripts\activate
```
6. Install in editable mode with pip (copy and paste this into the command prompt after cloning is complete):

```
pip install -e .
```

---

## Usage

**GUI Mode**

Simply run the command without any arguments:

```
foldchangeviz
```
It should look like this in the command prompt (click enter to start the GUI):

```
C:\Users\[your name]>foldchangeviz
```

The GUI should appear as shown:

<img width="610" height="196" alt="image" src="https://github.com/user-attachments/assets/1c52526a-d3c9-45d3-94b4-0def11a2679d" />


- Browse for your CSV file

- Enter template wells (space-separated)

- Enter background and target m/z values

- Set intensity tolerance (default 10000)

- Click Generate Heatmap and save as PNG

**Command Line**

```
foldchangeviz --csv <path_to_csv> --wells <well1> <well2> ... --mz1 <background_mz> --mz2 <target_mz> [--tolerance <value>] [--save <output_file.png>]
```
Example Usage:

```
foldchangeviz --csv data.csv --wells A1 B1 --mz1 212.089 --mz2 212.0891 --tolerance 10000 --save output.png
```
Inputs: 

- --csv: Path to the input CSV file

- --wells: List of template wells to calculate fold change

- --mz1: Background m/z (numeric only)

- --mz2: Target m/z (numeric only)

- --tolerance: Intensity threshold for black mask (default: 10000)

- --save: Optional output PNG file path. If omitted, the plot will display instead of saving

