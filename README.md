# foldchangeviz

**foldchangeviz** is a Python package and command-line tool for visualizing fold change heatmaps from screening data. It provides both a **GUI** for interactive use and a **CLI** for scripting and automation.

---

## Features

- Generate fold change heatmaps from CSV files
- Mark values within 3 standard deviations of template wells with a red `X`
- Mask low-intensity wells in black
- Supports both GUI and CLI usage
- Save plots as high-resolution PNGs

---

## Installation

1. Clone the repository:

```
git clone https://github.com/rashepherd/foldchangeviz.git
cd foldchangeviz
```

2. Install in editable mode with pip:

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
Browse for your CSV file

Enter template wells (space-separated)

Enter background and target m/z values

Set intensity tolerance (default 10000)

Click Generate Heatmap and save as PNG

**Command Line**

```
foldchangeviz --csv <path_to_csv> --wells <well1> <well2> ... --mz1 <background_mz> --mz2 <target_mz> [--tolerance <value>] [--save <output_file.png>]
```
Example Usage:

```
foldchangeviz --csv data.csv --wells A1 B1 --mz1 212.089 --mz2 212.0891 --tolerance 10000 --save output.png
```
Inputs: 

--csv: Path to the input CSV file

--wells: List of template wells to calculate fold change

--mz1: Background m/z (numeric only)

--mz2: Target m/z (numeric only)

--tolerance: Intensity threshold for black mask (default: 10000)

--save: Optional output PNG file path. If omitted, the plot will display instead of saving

