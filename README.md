# GameLauncher
it a launcher to launch games


This Python program is a simple desktop game launcher built using the Tkinter GUI library. It allows the user to manage and launch games or programs from a single window.

The application provides a graphical interface where users can:

Add games by selecting executable (.exe) files from their computer.

View a list of added games in a scrollable list.

Launch a selected game directly from the launcher.

Delete games from the list.

The launcher stores game information (name and file path) in a local JSON file (games_simple.json), allowing the game list to persist between application launches. When the program starts, it loads the saved games from this file and displays them in the interface.

The interface includes buttons for adding, playing, and deleting games, along with message dialogs to inform the user about successful actions or errors. Games are launched using the subprocess module.

Overall, this code demonstrates how to build a basic GUI application in Python that integrates file handling, persistent storage, and external program execution.
