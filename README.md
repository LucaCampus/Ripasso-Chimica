# Ripasso Chimica

Python scripts for reviewing chemistry topics through simple interactive quizzes.

The repository contains command-line quiz tools for memorizing chemical elements, mnemonic concepts, and physical quantities. Questions and answers are stored in text files, so the datasets can be edited or extended without changing the Python code.

## Contents

- `Ripasso_concetti_mnemonici/` - quiz for mnemonic chemistry concepts.
- `Ripasso_elementi/` - quizzes for chemical elements, divided by groups and categories.
- `Ripasso_grandezze/` - quiz for physical quantities, units of measure, symbols, and primitive quantities.
- `Ripasso_elementi_grafica/` - early graphical version built with Pygame.

## Requirements

- Python 3
- Pygame, only for the graphical version:

```bash
pip install pygame
```

The command-line quizzes use only the Python standard library.

## How to Run

Run each script from its own folder, because the scripts read the question and answer `.txt` files using relative paths.

Example:

```bash
cd Ripasso_concetti_mnemonici
python concetti_mnemonici.py
```

Element quizzes:

```bash
cd Ripasso_elementi
python elementi_tot.py
```

Physical quantities quiz:

```bash
cd Ripasso_grandezze
python grandezze.py
```

Graphical version:

```bash
cd Ripasso_elementi_grafica
python main.py
```

## Data Files

Each quiz uses paired text files:

- one file contains the questions;
- the matching response file contains the answers;
- each question and answer should be placed on the same line number in their respective files.

For example, the first line of a questions file corresponds to the first line of its answers file.

## Features

- Random question selection.
- Immediate answer checking.
- Text-file based quiz databases.
- Option to add new questions in some scripts.
- Experimental Pygame interface for graphical review.

## Repository Description

Python chemistry revision quizzes for elements, mnemonic concepts, and physical quantities.
