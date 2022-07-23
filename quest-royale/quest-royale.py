import asyncio
import contextlib
import json
import logging
import os
import random
import re
import time
from copy import copy
from datetime import date, datetime, timedelta
from math import ceil
from operator import itemgetter
from types import SimpleNamespace
from typing import List, Literal, MutableMapping, Optional, Union
import redbot.core.config

import discord
from beautifultable import ALIGN_LEFT, BeautifulTable
from discord.ext.commands import CheckFailure
from discord.ext.commands.errors import BadArgument
from redbot.core import Config, commands
from redbot.core.bot import Red
from redbot.core.commands import check, get_dict_converter
from redbot.core.data_manager import bundled_data_path, cog_data_path
from redbot.core.errors import BalanceTooHigh
from redbot.core.i18n import Translator, cog_i18n
from redbot.core.utils import AsyncIter
from redbot.core.utils.chat_formatting import box, escape, humanize_list, humanize_number, humanize_timedelta, pagify
from redbot.core.utils.common_filters import filter_various_mentions
from redbot.core.utils.menus import DEFAULT_CONTROLS, menu, start_adding_reactions
from redbot.core.utils.predicates import MessagePredicate, ReactionPredicate

class QuestRoyale(commands.Cog):
    