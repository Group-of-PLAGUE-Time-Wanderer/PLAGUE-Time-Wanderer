#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync Bot 2

Sync messages between 2 servers.
"""
import json
import os

import aiohttp
from googletrans import Translator

import discord

client = discord.Client()

json_file = json.load(open("conf.json"))
GUILD_1 = json_file["guild1"]
GUILD_2 = json_file["guild2"]
GUILD_1_WEBHOOK = json_file["webhook1"]
GUILD_2_WEBHOOK = json_file["webhook2"]
translator = Translator()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content.startswith("$nsd"):
        message_guild = message.guild.id
        if message_guild == GUILD_1:
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(
                    GUILD_2_WEBHOOK, adapter=discord.AsyncWebhookAdapter(session))
                if message.content.startswith("$nts"):
                    text = message.content
                else:
                    text = translator.translate(
                        message.content, dest="fr").text
                await webhook.send(text, username=message.author.name, avatar_url=message.author.avatar_url)
        elif message_guild == GUILD_2:
            async with aiohttp.ClientSession() as session:
                webhook = discord.Webhook.from_url(
                    GUILD_1_WEBHOOK, adapter=discord.AsyncWebhookAdapter(session))
                if message.content.startswith("$nts"):
                    text = message.content
                else:
                    text = translator.translate(
                        message.content, dest="en").text
                await webhook.send(text, username=message.author.name, avatar_url=message.author.avatar_url)

client.run(json_file["token"])
