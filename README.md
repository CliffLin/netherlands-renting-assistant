# Netherlands Renting Assistant

Scrape renting website and send latest info to your telegram chat.

## Features
- Multiple provider, Funda and Pararius.
- Flexible callback function. Default is sending to telegram.
- Storing viewed data in local.

## How to use
1. Clone this repo. 
2. Modify some data in main.py
    - AREA (where you want to rent the house)
    - PRICE (price range)
    - HEADERS (you can fetch it from your browser)
    - CHATID (telegram chat id)
    - TOKEN (telegram bot id)
3. create virtual env.
4. install python library from requirements.txt
5. Run main.py
