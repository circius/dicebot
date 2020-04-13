import setuptools
from glob import glob
from os.path import basename
from os.path import splitext

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dicebot",
    version="0.1",
    author="circius",
    author_email="circius@posteo.de",
    description="dice-rolling bot for discord",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/circius/dicebot-py",
    download_url="",
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
    ],
    keywords=["rpg", "diceroller, ""bot", "discord"],
    python_requires=">=3.6",
    setup_requires=["pytest-runner",],
    install_requires=[
        "discord.py",
        "dice",
    ],
    entry_points="""
    [console_scripts]
    dicebot=dicebot.daemon:main
""",
)

