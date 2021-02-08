# rock-paper-scissors-exercise

Rock Paper Scissors Exercise

A game that allows a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent.

Prerequisites

Anaconda 3.7+
Python 3.7+
Pip

Installation

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory):

    cd rock-paper-scissors-exercise

Use Anaconda to create and activate a new virtual environment, perhaps called "my-env":

    conda create -n my-env python=3.8
    conda activate my-env

From inside the virtual environment, install package dependencies:

    pip install -r requirements.txt

NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial cd step above)

Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    PLAYER_NAME="John Snow"

NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the .gitignore file)

Usage

Run the game script:

    python game.py

