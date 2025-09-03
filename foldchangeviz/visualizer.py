import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def visualize_fold_change(csv, wells, mz1, mz2, tolerance=10000, save=None):
    df = pd.read_csv(csv)
    df['row'] = df['Well ID'].str.extract('([A-Za-z]+)')
    df['column'] = df['Well ID'].str.extract('(\d+)').astype(int)
    df['rel_abundance'] = df[mz2] / (df[mz1] + df[mz2])
    df['total_area'] = df[mz1] + df[mz2]
    df['fold_change'] = df['rel_abundance'] / df[df['Well ID'].isin(wells)]['rel_abundance'].mean()
    df['fold_change'].fillna(0, inplace=True)

    heatmap_data = df.pivot(index='row', columns='column', values='fold_change')
    row_order = sorted(heatmap_data.index, key=lambda x: (x[0], x))
    row_order.reverse()
    heatmap_data = heatmap_data.reindex(row_order)

    avg_fc = df[df['Well ID'].isin(wells)]['fold_change'].mean()
    std_fc = df[df['Well ID'].isin(wells)]['fold_change'].std()
    lower, upper = avg_fc - (3 * std_fc), avg_fc + (3 * std_fc)

    mask_within = ((heatmap_data >= lower) & (heatmap_data <= upper)) | (heatmap_data == 0)
    total_area_pivot = df.pivot(index='row', columns='column', values='total_area').reindex(index=heatmap_data.index, columns=heatmap_data.columns)
    mask_black = (total_area_pivot < tolerance) & ~total_area_pivot.isna()

    plt.figure(figsize=(10, 6))
    x, y = heatmap_data.columns, heatmap_data.index
    X, Y = np.meshgrid(x, y)
    x_flat, y_flat, z_flat = X.flatten(), Y.flatten(), heatmap_data.values.flatten()
    scatter = plt.scatter(x_flat, y_flat, s=600, c=z_flat, cmap=plt.cm.Blues, alpha=0.6,
                          edgecolors='w', linewidth=1, vmin=0, vmax=heatmap_data.max().max())

    row_idx_map = {label: i for i, label in enumerate(heatmap_data.index)}
    col_idx_map = {label: i for i, label in enumerate(heatmap_data.columns)}

    # Black overlay for low total area
    for idx, val in enumerate(z_flat):
        row, col = y_flat[idx], int(x_flat[idx])
        ri, ci = row_idx_map[row], col_idx_map[col]
        if mask_black.iat[ri, ci]:
            plt.scatter(x_flat[idx], y_flat[idx], s=600, c='black', edgecolors='w', linewidth=1, alpha=0.9)

    # Mark within ±3SD and print values
    for idx, val in enumerate(z_flat):
        row, col = y_flat[idx], int(x_flat[idx])
        ri, ci = row_idx_map[row], col_idx_map[col]
        if mask_within.iat[ri, ci] and not mask_black.iat[ri, ci]:
            plt.text(x_flat[idx], y_flat[idx], 'X', color='red', fontsize=12, ha='center', va='center')
        if not np.isnan(val):
            plt.text(x_flat[idx], row_idx_map[row] - 0.52, f'{val:.2f}', color='black', fontsize=10, ha='center')

    # Outline template wells with red circles
    template_df = df[df['Well ID'].isin(wells)]
    for _, r in template_df.iterrows():
        plt.scatter(r['column'], r['row'], s=600, facecolors='none', edgecolors='red', linewidth=2)

    plt.text(0.5, 1.02, f'Average Template Fold Change: {avg_fc:.2f}', fontsize=10,
             ha='center', transform=plt.gca().transAxes)
    plt.text(0.5, 1.07, f'Standard Deviation of Template Fold Change: {std_fc:.2f}', fontsize=10,
             ha='center', transform=plt.gca().transAxes)
    plt.xlabel('Column')
    plt.ylabel('Row')
    plt.grid(False)
    plt.xticks(ticks=x, labels=x)
    plt.yticks(ticks=y, labels=y)
    plt.colorbar(scatter, label='Fold Change')
    plt.ylim(-0.7, len(heatmap_data.index) - 0.5)

    if save:
        plt.savefig(save, dpi=300, bbox_inches='tight')
    else:
        plt.show()
