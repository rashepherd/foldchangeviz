from setuptools import setup, find_packages

setup(
    name="foldchangeviz",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "seaborn",
    ],
    entry_points={
        "console_scripts": [
            "foldchangeviz = foldchangeviz.__main__:main",  # <-- point to main()
        ],
    },
    author="Your Name",
    description="Command-line and GUI tool to visualize fold change heatmaps from screening data.",
    python_requires='>=3.8',
)


