from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from more_itertools import chunked
import os, shelve

db = shelve.open("channels.db")

def albums():
    albums_list = os.listdir("albums")
    chunked_keys = list(chunked(albums_list, 1))
    albums = []
    for chunk in chunked_keys:
        row_buttons = [InlineKeyboardButton(pre, callback_data=pre) for pre in chunk]
        albums.append(row_buttons)
    return InlineKeyboardMarkup(album)

def album(name):
    db = shelve.open(f"albums/{name}.album")
    allkeys = list(db.keys())
    chunked_keys = list(chunked(allkeys, 3))
    album = []
    for chunk in chunked_keys:
        row_buttons = [InlineKeyboardButton(pre, callback_data=pre) for pre in chunk]
        album.append(row_buttons)
    album.append([InlineKeyboardButton("Quay lại bộ sưu tập", callback_data="back-button"))
    return InlineKeyboardMarkup(album)
    
def add_media(name, media):
    db = shelve.open(f"albums/{name}.album")
    db[media[0]]=media[1]
    
def del_media(name, media):
    db = shelve.open(f"albums/{name}.album")
    del db[media]
    
def get_media(name, media):
    db = shelve.open(f"albums/{name}.album")
    return db[media]