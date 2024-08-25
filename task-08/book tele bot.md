# Uniting Gopal with PagePal: Building a Book Recommendation Telegram Bot


## Introduction

Meet Gopal, a passionate book lover with an insatiable appetite for literature. However, Gopal faced a challenge: he struggled to locate books that matched his preferences. This inspired the idea of a chatbot that could recommend books based on genre, complete with all the necessary details. While Gopal had the vision, he lacked the programming skills to bring "PagePal" to life. That’s where I stepped in, taking on the challenge to create a Telegram bot that could serve as Gopal’s digital librarian.

In this blog post, I’ll walk you through the process of developing PagePal, a Telegram bot that provides book recommendations, previews, and even manages a reading list.

## The Idea Behind PagePal

The concept was simple yet powerful: a chatbot that could recommend books by genre, provide preview links, and allow users to manage their reading lists. The bot needed to be user-friendly, with easy commands that even non-tech-savvy users could navigate.

  #### Core Features:

      Book Recommendations: Users can request book recommendations by genre.
      Preview Links: Users can get preview links for books.
      Reading List Management: Users can add, view, and delete books from their reading list.
      Help Command: Provides a list of available commands for users.

## Technical Implementation

To bring PagePal to life, I used Python along with the python-telegram-bot library to handle the bot’s functionality. I also used the pandas library for handling book data and python-docx for potential future enhancements involving document generation. Here's how I did it:


#### Step 1: Setting Up the Bot

First, I created a new bot using the Telegram Bot API and got a unique token to authenticate requests. Then, I set up the bot’s basic commands, including /start, /book, /preview, /list, and /help.

      from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
      from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler
      import pandas as pd
      from docx import Document

      
#### Step 2: Handling Book Recommendations

I created a dictionary of sample book data organized by genre. The /book command allows users to input a genre and receive a list of books in that genre. The data is converted into a CSV file and sent to the user.

      async def book(update: Update, context: CallbackContext):
      genre = ' '.join(context.args).capitalize()
      if genre in books_data:
          df = pd.DataFrame(books_data[genre])
          df.to_csv('books.csv', index=False)
          with open('books.csv', 'rb') as f:
              await update.message.reply_document(document=f)
      else:
          await update.message.reply_text("No books found for this genre.")

#### Step 3: Providing Preview Links

Users can get a preview link of a specific book using the /preview command. The bot searches through the book data and returns the preview link if the book is found.

    async def preview(update: Update, context: CallbackContext):
        book_name = ' '.join(context.args).title()
        for genre, books in books_data.items():
            for book in books:
                if book['title'] == book_name:
                    await update.message.reply_text(f"Preview link: {book['preview']}")
                    return
        await update.message.reply_text("Book not found.")

#### Step 4: Managing the Reading List

PagePal also includes a reading list management feature. Using inline buttons, users can add books to their reading list, delete books, or view their list.

    async def list_books(update: Update, context: CallbackContext):
        keyboard = [
            [InlineKeyboardButton("Add a book", callback_data='add')],
            [InlineKeyboardButton("Delete a book", callback_data='delete')],
            [InlineKeyboardButton("View Reading List", callback_data='view')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text('Manage your reading list:', reply_markup=reply_markup)

        
#### Step 5: Handling Inline Button Responses

To manage user interactions with the inline buttons, I implemented a callback handler that processes the user's selection.

    async def button(update: Update, context: CallbackContext):
        query = update.callback_query
        await query.answer()
        await query.message.reply_text(f"Button {query.data} pressed")

## Challenges and Solutions

The creation of the bot with required functionality was quite challenging for me as this was my first time creating a bot, but the bot created has all the functionalities, exept the add, delete and preview part where the buttons dont work this would be rectified soon.

## conclusion

the bot enables us to find pre set books of diffrent genre and allows us to delete and preview books in the form of a csv file. thus this indeed a perfect partner for our reading journey.
