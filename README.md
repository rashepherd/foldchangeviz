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

```bash
pip install -e .
