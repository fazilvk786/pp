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
    START_TEXT = "Namaste .\n      I am Video Compress Bot . Works only HERE @CompressZONE "
   
    ABS_TEXT = "<b> My father - @priyanshu_bhardwaj </b> \n\n Compress Your File here :- @CompressZone \n Source :- https://github.com/bhardwajjEE/tgvideoCompress"
    
    FORMAT_SELECTION = "Select the desired format: <a href='{}'>file size might be approximate</a> \nIf you want to set custom thumbnail, send photo before or quickly after tapping on any of the below buttons.\nYou can use /deletethumbnail to delete the auto-generated thumbnail."
    
    
    DOWNLOAD_START = "Downloading ...🦏   "
    
    UPLOAD_START = "Uploading ...🐝  "
    
    COMPRESS_START = "Compressing ...🔧  "
    
    RCHD_BOT_API_LIMIT = "size greater than maximum allowed size (50MB). Neverthless, trying to upload."
    
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry. But, I cannot upload files greater than 1.95 GB due to Telegram limitations. 🔒  "
    
    COMPRESS_SUCCESS = "By @TGcompressBot 🐥\n\n 🐘 Downloaded in {}\n🗜️ Compressed in {} 👷\n🕊️ Uploaded in {}"

    COMPRESS_PROGRESS = "⏳ Estimated Time : {}\n🌱 Work Done : {}%"

    SAVED_CUSTOM_THUMB_NAIL = "Custom thumbnail saved. This image will be used in the video. " 
    
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully. 🚽 "
    
    SAVED_RECVD_DOC_FILE = "Downloaded Successfully..✌️ "
    
    CUSTOM_CAPTION_UL_FILE = "say Thanks to @tgcompressbot"
    
    NO_CUSTOM_THUMB_NAIL_FOUND = "No Custom ThumbNail found. 💀 "
    
    NO_VOID_FORMAT_FOUND = "no-one gonna help you ... 😬\n{}"
    
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "<b> I am Not Free Now ; Another process is GoiNg Now....🚕 "
    
    HELP_MESSAGE = get_config(
        "STRINGS_HELP_MESSAGE",
        "Here is simple guide to use me 🤖 \n\n1. Send me video which you want to compress ...🔧 \n\n2. Reply <b> '/compress@tgcompressbot Percentage' </b> to video...💡 \n\n3. I will do Rest Things ..🐾\n\n\n <b> Made in BHARAT with 💌</b> "
    )
    WRONG_MESSAGE = get_config(
        "STRINGS_WRONG_MESSAGE",
        "current CHAT ID: <code>{CHAT_ID}</code>"
    )
