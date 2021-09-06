#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | gautamajay52

import io
import logging
import os
import sys
import traceback

from pyrogram import Client, filters, idle
from pyrogram.raw import functions, types
from pyrogram.handlers import CallbackQueryHandler, MessageHandler

from tobrot import *
from tobrot.plugins.heroku import gib_restart
from tobrot.helper_funcs.download import down_load_media_f
from tobrot.plugins.call_back_button_handler import button
# the logging things
from tobrot.plugins.choose_rclone_config import rclone_command_f
from tobrot.plugins.custom_thumbnail import clear_thumb_nail, save_thumb_nail
from tobrot.plugins.incoming_message_fn import (g_clonee, g_yt_playlist,
                                                incoming_message_f,
                                                incoming_purge_message_f,
                                                incoming_youtube_dl_f,
                                                rename_tg_file)
from tobrot.plugins.new_join_fn import help_message_f, new_join_f
from tobrot.plugins.rclone_size import check_size_g, g_clearme
from tobrot.plugins.status_message_fn import (
    cancel_message_f,
    eval_message_f,
    exec_message_f,
    status_message_f,
    upload_document_f,
    upload_log_file,
    upload_as_doc,
    upload_as_video
)

if __name__ == "__main__":
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    # Starting The Bot
    app.start()
    ##############################################################################
    bu = f"@{(app.get_me()).username}"
    ##############################################################################
         ## Only For Heroku ####
    reboot_handler = MessageHandler(
        gib_restart,
        filters.command(["reboot", f"reboot{bu}"]) & filters.user(OWNER_ID)
    )
    app.add_handler(reboot_handler)
    ##############################################################################
    incoming_message_handler = MessageHandler(
        incoming_message_f,
        filters=filters.command(
            [
                f"{LEECH_COMMAND}",
                f"{LEECH_COMMAND}{bu}",
                f"{LEECH_UNZIP_COMMAND}",
                f"{LEECH_UNZIP_COMMAND}{bu}",
                f"{LEECH_ZIP_COMMAND}", 
                f"{LEECH_ZIP_COMMAND}{bu}",
                f"{GLEECH_COMMAND}",
                f"{GLEECH_COMMAND}{bu}",
                f"{GLEECH_UNZIP_COMMAND}",
                f"{GLEECH_UNZIP_COMMAND}{bu}",
                f"{GLEECH_ZIP_COMMAND}",
                f"{GLEECH_ZIP_COMMAND}{bu}"
            ]
        )
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_message_handler)
    ##############################################################################
    incoming_telegram_download_handler = MessageHandler(
        down_load_media_f,
        filters=filters.command([f"{TELEGRAM_LEECH_COMMAND}", f"{TELEGRAM_LEECH_UNZIP_COMMAND}", f"{TELEGRAM_LEECH_COMMAND}{bu}", f"{TELEGRAM_LEECH_UNZIP_COMMAND}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_telegram_download_handler)
    ##############################################################################
    incoming_purge_message_handler = MessageHandler(
        incoming_purge_message_f,
        filters=filters.command(["purge"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_purge_message_handler)
    ##############################################################################
    incoming_clone_handler = MessageHandler(
        g_clonee,
        filters=filters.command([f"{CLONE_COMMAND_G}", f"{CLONE_COMMAND_G}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_clone_handler)
    ##############################################################################
    incoming_size_checker_handler = MessageHandler(
        check_size_g,
        filters=filters.command([f"{GET_SIZE_G}", f"{GET_SIZE_G}{bu}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_size_checker_handler)
    ##############################################################################
    incoming_g_clear_handler = MessageHandler(
        g_clearme,
        filters=filters.command([f"{RENEWME_COMMAND}", f"{RENEWME_COMMAND}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_g_clear_handler)
    ##############################################################################
    incoming_youtube_dl_handler = MessageHandler(
        incoming_youtube_dl_f,
        filters=filters.command([f"{YTDL_COMMAND}{bu}", f"{GYTDL_COMMAND}{bu}", f"{YTDL_COMMAND}", f"{GYTDL_COMMAND}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_youtube_dl_handler)
    ##############################################################################
    incoming_youtube_playlist_dl_handler = MessageHandler(
        g_yt_playlist,
        filters=filters.command([f"{PYTDL_COMMAND}{bu}", f"{GPYTDL_COMMAND}{bu}", f"{PYTDL_COMMAND}", f"{GPYTDL_COMMAND}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(incoming_youtube_playlist_dl_handler)
    ##############################################################################
    status_message_handler = MessageHandler(
        status_message_f,
        filters=filters.command([f"{STATUS_COMMAND}", f"{STATUS_COMMAND}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(status_message_handler)
    ##############################################################################
    cancel_message_handler = MessageHandler(
        cancel_message_f,
        filters=filters.command([f"{CANCEL_COMMAND_G}", f"{CANCEL_COMMAND_G}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(cancel_message_handler)
    ##############################################################################
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command(["exec"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(exec_message_handler)
    ##############################################################################
    eval_message_handler = MessageHandler(
        eval_message_f,
        filters=filters.command(["eval"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(eval_message_handler)
    ##############################################################################
    rename_message_handler = MessageHandler(
        rename_tg_file,
        filters=filters.command([f"{RENAME_COMMAND}", f"{RENAME_COMMAND}{bu}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(rename_message_handler)
    ##############################################################################
    upload_document_handler = MessageHandler(
        upload_document_f,
        filters=filters.command([f"{UPLOAD_COMMAND}", f"{UPLOAD_COMMAND}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_document_handler)
    ##############################################################################
    upload_log_handler = MessageHandler(
        upload_log_file,
        filters=filters.command([f"{LOG_COMMAND}", f"{LOG_COMMAND}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_log_handler)
    ##############################################################################
    help_text_handler = MessageHandler(
        help_message_f,
        filters=filters.command([f"{HELP_COMMAND}", f"{HELP_COMMAND}{bu}"]) & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(help_text_handler)
    ##############################################################################
    new_join_handler = MessageHandler(
        new_join_f, filters=~filters.chat(chats=AUTH_CHANNEL)
    )
    app.add_handler(new_join_handler)
    ##############################################################################
    '''
    group_new_join_handler = MessageHandler(
        help_message_f,
        filters=filters.chat(chats=AUTH_CHANNEL) & filters.new_chat_members,
    )
    app.add_handler(group_new_join_handler)
    '''
    ##############################################################################
    call_back_button_handler = CallbackQueryHandler(button)
    app.add_handler(call_back_button_handler)
    ##############################################################################
    save_thumb_nail_handler = MessageHandler(
        save_thumb_nail,
        filters=filters.command([f"{SAVE_THUMBNAIL}", f"{SAVE_THUMBNAIL}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(save_thumb_nail_handler)
    ##############################################################################
    clear_thumb_nail_handler = MessageHandler(
        clear_thumb_nail,
        filters=filters.command([f"{CLEAR_THUMBNAIL}", f"{CLEAR_THUMBNAIL}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(clear_thumb_nail_handler)
    ##############################################################################
    rclone_config_handler = MessageHandler(
        rclone_command_f, filters=filters.command([f"{RCLONE_COMMAND}", f"{RCLONE_COMMAND}{bu}"])
        & filters.user(OWNER_ID),
    )
    app.add_handler(rclone_config_handler)
    ##############################################################################
    upload_as_doc_handler = MessageHandler(
        upload_as_doc,
        filters=filters.command([f"{TOGGLE_DOC}", f"{TOGGLE_DOC}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_as_doc_handler)
    ##############################################################################
    upload_as_video_handler = MessageHandler(
        upload_as_video,
        filters=filters.command([f"{TOGGLE_VID}", f"{TOGGLE_VID}{bu}"])
        & filters.chat(chats=AUTH_CHANNEL),
    )
    app.add_handler(upload_as_video_handler)
    ##############################################################################
    app.send(
      functions.bots.SetBotCommands (
        commands=[
          types.BotCommand(command=f"{LEECH_COMMAND}", description="🌠 Leech Files To Telegram"),
          types.BotCommand(command=f"{LEECH_UNZIP_COMMAND}", description="📂 Extract Archives & Upload To Telegram"),
          types.BotCommand(command=f"{LEECH_ZIP_COMMAND}", description="🤐 Archives & Upload To Telegram"),
          types.BotCommand(command=f"{STATUS_COMMAND}", description="Get Download Status ✍🏻"),
          types.BotCommand(command=f"{SAVE_THUMBNAIL}", description="🎆 Saves Custom Thumbnail For Your Uploads"),
          types.BotCommand(command=f"{CLEAR_THUMBNAIL}", description="❌ Clears Custom Thumbnail To Default"),
          types.BotCommand(command=f"{RENAME_COMMAND}", description="📝 To Rename A Telegram File")
        ]
      )
    )
    logging.info(f"All Commands Set Fot @{(app.get_me()).username}")
    ##############################################################################
  
    logging.info(f"@{(app.get_me()).username} Has Started Running...🏃💨💨")
    
    idle()
    
    app.stop()