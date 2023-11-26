#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from decouple import config

try:
    APP_ID = config("APP_ID", "3847632")
    API_HASH = config("API_HASH", "1a9708f807ddd06b10337f2091c67657")
    BOT_TOKEN = config("BOT_TOKEN", "6200331513:AAFcjwJdhu9zt4xje1MWod1LhvkXhHJ_3cM")
    DEV = 1322549723
    OWNER = config("OWNER", "5385471287")
    FFMPEG = config("FFMPEG", "ffmpeg ""{}""-i -preset veryfast -c:v libx265 -crf 27 -s 1280x720 -map 0:v -c:a aac ""{}""") 
    THUMB = config("THUMBNAIL", "https://graph.org/file/75ee20ec8d8c8bba84f02")
except Exception as e:
    print("Environment vars Missing")
    print("something went wrong")
    print(str(e))
    exit()
