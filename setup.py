from setuptools import setup, find_packages

setup(
    name="matrix_notify",
    version="0.1.0",
    description="Simple tool to send a message to a matrix chat room.",
    author="Moritz Schillinger",
    author_email="moritz.schillinger@fau.de",
    packages=find_packages(include=["matrix_notify", "matrix_notify.*"]),
    install_requires=["matrix-nio", "beautifulsoup4"],
    entry_points={
        "console_scripts": [
            "matrix-notify = matrix_notify.notify:main",
        ],
    },
)
