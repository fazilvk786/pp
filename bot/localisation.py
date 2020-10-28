#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) PublicLeech Author(s)
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from bot.get_cfg import get_config


class Localisation:
    START_TEXT = "WelCome..💌 , \n\n *I am only Bot in Telegram , who is able reduce size of video files by compressing them .* Send me any Telegram video , I will try till my last breath...❤️</b> \n\n Send /help to know how to guide and use  me.. \n\n"
   
    ABS_TEXT = " Don't be selfish...😐"
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Downloading your file....📥 \n"
    
    UPLOAD_START = "Uploading is in Progress ...🐝 \n"
    
    COMPRESS_START = "⚙️ Trying to Reduce File Size... 🗜️  \n Time will Vary According to your File compatiblity ."
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95 GB due to Telegram limitations. 🔒  "
    
    COMPRESS_SUCCESS = " @TGcompressBot 🐥\n\n 🐘 Downloaded in {}\n🗜️ Compressed in {} 👷\n🕊️ Uploaded in {}"

    COMPRESS_PROGRESS = "⏳ Estimated Time : {}\n🌱 Work Done : {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This image will be used in the video. " 
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully. 🚽 "
    
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully..✌️ "
    
    CUSTOM_CAPTION_UL_FILE = " "
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found. 💀 "
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you ... 😬\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "⚠️ Already One Process going on. \n or \n A media already exists. \n  Please send /cancel to delete existing media. ⚠️"
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        " Hey You Noobie .....👻\n\n Here is simple guide to use me 🤖 \n 1. Send me video which you want to compress ...😌 \n 2. Reply  '/compress Percentage' to the media file . [e.g. reply 'compress 50' to video if you want to reduce file size to half of previous size] \n\n 3. Now things are in my hands now . Don't worry i will do rest thing by my own . You just need to Wait ...😛 /n/n/n Made in INDIA with 💌  "
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
