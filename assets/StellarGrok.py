"""StellarGrok chart styling for matplotlib.

Usage in a post (hidden setup chunk):
    import sys; sys.path.insert(0, "../../../assets")
    import StellarGrok; StellarGrok.use()
"""
from cycler import cycler
import matplotlib as mpl

FOREST = "#08251a"
FOREST_500 = "#197050"
LIME = "#abff44"
LEAF = "#3ab533"
SAGE_50 = "#eff6e9"
SAGE_200 = "#d8e4cb"
SAGE_500 = "#717863"
MINT = "#2f9b99"
PINK = "#c96384"
GOLD = "#e0a526"

# Categorical order chosen for contrast on white (lime is for highlights, not lines)
PALETTE = [FOREST_500, MINT, PINK, GOLD, LEAF, FOREST]


def use() -> None:
    """Apply the StellarGrok look to all subsequent matplotlib figures."""
    mpl.rcParams.update({
        "figure.facecolor": "white",
        "figure.figsize": (8, 4.5),
        "axes.facecolor": "white",
        "axes.edgecolor": SAGE_200,
        "axes.labelcolor": FOREST,
        "axes.titlecolor": FOREST,
        "axes.titleweight": "bold",
        "axes.titlesize": 15,
        "axes.titlelocation": "left",
        "axes.titlepad": 14,
        "axes.labelsize": 11,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "axes.grid.axis": "y",
        "axes.prop_cycle": cycler(color=PALETTE),
        "grid.color": SAGE_200,
        "grid.linewidth": 0.8,
        "xtick.color": SAGE_500,
        "ytick.color": SAGE_500,
        "xtick.labelcolor": FOREST,
        "ytick.labelcolor": FOREST,
        "legend.frameon": False,
        "lines.linewidth": 2.4,
        "font.family": "sans-serif",
        "savefig.bbox": "tight",
    })
