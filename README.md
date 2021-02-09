# rock-paper-scissors-exercise

Rock Paper Scissors Exercise

A game that allows a human user to play a game of Rock-Paper-Scissors against a computer (NPC) opponent.

Prerequisites

Anaconda 3.7+
Python 3.7+
Pip

Installation

Navigate to the repository from the command line (subsequent commands assume you are running them from the local repository's root directory) by using the following command:

    cd rock-paper-scissors-exercise

Use Anaconda to create and activate a new virtual environment, perhaps called "my-env":

    conda create -n my-env python=3.8
    conda activate my-env

From inside the virtual environment, install package dependencies:

    pip install -r requirements.txt

Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username and to change the default player's name of Player One (replace "John Snow" with the desired player's name):

    PLAYER_NAME="John Snow"

Usage

Run the game script:

    python game.py

(Adapted from from Professor Rossetti's markdown)