# ISM2411 — Python for Business

**Name:** Pedro Mortari

**Semester:** Fall 2026

**Instructor:** Markum Reed

## About This Repo

This repository contains my weekly lab submissions for ISM2411.
Each folder corresponds to one module.

## Modules

- `week08/` — Git: first GitHub submission

## How to Run

Each script is standalone. Open a terminal and run:

    python weekXX/filename.py

## Reflection

**1. Commit history**

Looking at this history, a hiring manager would see that I work in small, incremental steps instead of making one giant change at the end. Most of my messages say what changed (for example, "add lab 8 reflection to README"), so someone could follow the project without opening the code. Where I could improve is consistency: a few messages are vague, and clearer ones would make it easier to find a specific change later.

**2. How Git changes my approach to editing a working script**

Before this module, I would edit a working script directly and hope I didn't break anything, with no easy way back if I did. Now I commit whenever the script is in a working state, so I can experiment freely and use `git diff` or roll back to the last good version if something goes wrong. I also try to make one logical change per commit so each step is easy to understand and undo.

**3. One addition to my .gitignore**

I would add `*:Zone.Identifier`. I work in WSL with VS Code on Windows, and when I copy files from Windows into my Linux folders, Windows creates these hidden metadata files next to the originals. They only record where a file was downloaded from on my machine, so they mean nothing to anyone else and would just clutter the repo.
