# Overwatch 2 Statistics Project

## Overview
This project is a web application designed to display Overwatch 2 player statistics and compare hero data. It is currently abandoned due to limitations with the Overwatch API not updating statistics in real-time.

## Technologies Used
 - Python
 - Django
 - HTML/CSS
- JavaScript
- Bootstrap

## Features

- Profile Search: Users can search for player profiles using their BattleTag to view summary and statistical data.
- Profile Search Via Battle.net auth: not fully implemented.
- Mini Game: Guess which of two randomly selected Overwatch 2 heroes is older based on their age displayed on their profile.


## Limitations
- Outdated Data: The Overwatch API used in this project does not update player statistics in real-time. As a result, the displayed data may not reflect current gameplay or recent matches.
- Incomplete Features: Certain features, such as the ability to view detailed player statistics via log in with Battle.net.

## Getting Started
To run the project locally:

- Clone the repository:
```bash
git clone https://github.com/121mlvin/OW2Stats
```
- Install dependencies: 
```bash
pip install -r requirements.txt
```
- Run the development server:
```bash 
python manage.py runserver
```