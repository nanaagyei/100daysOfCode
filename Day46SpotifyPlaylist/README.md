# Billboard Spotify Playlist Creator

## Overview
The Billboard Spotify Playlist Creator is a Python application that creates Spotify playlists based on historical Billboard Hot 100 charts. It combines web scraping techniques to gather song data from Billboard and uses the Spotify API to create playlists in the user's Spotify account. Users can specify a date to retrieve the top songs from that time and have a corresponding playlist created in Spotify.

## Files in the Project
- `main.py`: The main script that handles web scraping from Billboard, interacts with Spotify's API, and creates playlists.

## How to Set Up
1. Ensure Python is installed on your system, along with the `requests`, `bs4` (BeautifulSoup), and `spotipy` modules.
2. Register an application with Spotify to obtain `CLIENT_ID` and `CLIENT_SECRET`.
3. Set the `CLIENT_ID`, `CLIENT_SECRET`, and your `SPOTIFY_USERNAME` as environment variables.
4. Download the `main.py` file.
5. Run `main.py` and input the desired date when prompted.

## Using the Application
- Upon running, the script asks for a date to travel back to in the format YYYY-MM-DD.
- It scrapes the top 100 songs from the Billboard chart for that date.
- The script then interacts with Spotify's API to search for these songs and creates a playlist in your Spotify account.
- Relive the music from any specific date in Billboard's history!

## Dependencies
- Python 3.x
- `requests` and `bs4` (BeautifulSoup) for web scraping
- `spotipy` for interacting with the Spotify API

## Credits
Developed by Prince Agyei Tuffour. This application is perfect for music enthusiasts who want to explore and relive historical music charts.

