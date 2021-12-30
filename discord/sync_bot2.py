#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sync Bot 2

Sync messages between 2 servers.
"""
import os

import aiohttp
import discord
from googletrans import Translator

client = discord.Client()

GUILD_1 = 925782569230954557
GUILD_2 = 925782642547363870
GUILD_1_WEBHOOK = "https://discord.com/api/webhooks/925788654541111296/RGuSmK6xx9KzReoRfu5vGN2MIJWXIY9P7jOG07FxxmxUDNY3s01ThnXrx_4HGtVfGymJ"
GUILD_2_WEBHOOK = "https://discord.com/api/webhooks/925784810163671050/IAAut0iTJ-eUMZtLoxPQa69RMPC-GlhcefqKhKOCBDBaWAZi2-T5-pU7pwFzEdTnKo7z"
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

client.run(os.environ["DISCORD_TOKEN"])
