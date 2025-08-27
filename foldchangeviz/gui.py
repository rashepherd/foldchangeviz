import tkinter as tk
from tkinter import filedialog, messagebox
from foldchangeviz.visualizer import visualize_fold_change

def main():
    def run_tool():
        csv_path = csv_entry.get()
        wells = wells_entry.get().split()
        mz1 = "Area_" + mz1_entry.get().strip()
        mz2 = "Area_" + mz2_entry.get().strip()
        tolerance = float(tolerance_entry.get())
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if not save_path:
            return
        try:
            visualize_fold_change(csv_path, wells, mz1, mz2, tolerance, save_path)
            messagebox.showinfo("Success", f"Heatmap saved to {save_path}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def browse_csv():
        path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if path:
            csv_entry.delete(0, tk.END)
            csv_entry.insert(0, path)

    root = tk.Tk()
    root.title("Fold Change Heatmap Generator")

    tk.Label(root, text="CSV File:").grid(row=0, column=0, sticky="e")
    csv_entry = tk.Entry(root, width=50)
    csv_entry.grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_csv).grid(row=0, column=2)

    tk.Label(root, text="Template Wells (space-separated):").grid(row=1, column=0, sticky="e")
    wells_entry = tk.Entry(root, width=50)
    wells_entry.grid(row=1, column=1, columnspan=2)

    tk.Label(root, text="Background m/z (numeric only, e.g., 212.089):").grid(row=2, column=0, sticky="e")
    mz1_entry = tk.Entry(root, width=50)
    mz1_entry.grid(row=2, column=1, columnspan=2)

    tk.Label(root, text="Target m/z (numeric only, e.g., 212.0891):").grid(row=3, column=0, sticky="e")
    mz2_entry = tk.Entry(root, width=50)
    mz2_entry.grid(row=3, column=1, columnspan=2)

    tk.Label(root, text="Intensity Tolerance:").grid(row=4, column=0, sticky="e")
    tolerance_entry = tk.Entry(root, width=50)
    tolerance_entry.insert(0, "10000")
    tolerance_entry.grid(row=4, column=1, columnspan=2)

    tk.Button(root, text="Generate Heatmap", command=run_tool).grid(row=5, column=0, columnspan=3, pady=10)

    root.mainloop()