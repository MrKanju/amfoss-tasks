# PagePal: A Book Recommendation Telegram Bot
# Project Overview

PagePal is a Telegram bot designed to recommend books based on genre and provide detailed information, including the title, author, description, year of publication, language, and preview links. Additionally, users can manage their reading list directly within the bot. This project is perfect for book enthusiasts who want quick, personalized book suggestions.

## Features

    Book Recommendations: Get book suggestions by genre.
    Preview Links: Access preview links for selected books.
    Reading List Management: Add, view, and delete books from your reading list.
    Interactive Interface: Easy-to-use commands and inline buttons for seamless interaction.

## Installation
### Prerequisites

    Python 3.7+
    A Telegram account

#### Steps

    Clone the repository:

    
Install dependencies:

    
    pip install -r requirements.txt

Set up your Telegram bot:

    Create a new bot using the BotFather on Telegram.
    Obtain the API token for your bot.

Configure the bot:

  Open the main.py file and replace the placeholder API token with your own:

    
    application = Application.builder().token("user generated bot token").build()

Run the bot:

    python main.py

#### Usage
### Available Commands

    /start: Displays a welcome message and introduces the bot.
    /book <genre>: Get a list of recommended books for a specified genre.
    /preview <book name>: Get a preview link for the specified book.
    /list: Manage your reading list (add, view, delete books).
    /help: Display a list of available commands.
