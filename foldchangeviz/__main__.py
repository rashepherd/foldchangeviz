import sys
import argparse
from foldchangeviz.gui import main as gui_main
from foldchangeviz.visualizer import visualize_fold_change

def main():
    if len(sys.argv) == 1:
        gui_main()
        return

    parser = argparse.ArgumentParser(description="Visualize fold change heatmap from screening data.")
    parser.add_argument("--csv", required=True, help="Path to input CSV file")
    parser.add_argument("--wells", nargs="+", required=True, help="List of template well IDs")
    parser.add_argument("--mz1", required=True, help="Background m/z (numeric only, e.g., 212.089)")
    parser.add_argument("--mz2", required=True, help="Target m/z (numeric only, e.g., 212.0891)")
    parser.add_argument("--tolerance", type=float, default=10000, help="Intensity threshold for black mask")
    parser.add_argument("--save", help="Output file to save plot (PNG)")

    args = parser.parse_args()
    mz1 = "Area_" + args.mz1.strip()
    mz2 = "Area_" + args.mz2.strip()

    visualize_fold_change(args.csv, args.wells, mz1, mz2, args.tolerance, args.save)
