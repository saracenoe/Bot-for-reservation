#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os

from dotenv import load_dotenv

load_dotenv()


class DefaultConfig:
    """Configuration for the bot."""



    # PORT = 3978 # en local
    PORT = 8000
    APP_TYPE = os.environ.get("MicrosoftAppType", "MultiTenant")
    APP_ID = "315267ba-6800-4298-bb32-5dd8a7948435" #os.environ.get("MicrosoftAppId", "")
<<<<<<< HEAD
    APP_PASSWORD = "eaab3185-3119-45e7-9e9b-951b0dd92677" #os.environ.get("MicrosoftAppPassword", "")
=======
    APP_PASSWORD = "D5i8Q~TZ5~GkQ8pPeJI3tsR9tZYZ.8-qFmZYWahG" #os.environ.get("MicrosoftAppPassword", "")
>>>>>>> b113cdd4ab877742f584b904cf80d75a9a8edaec
    LUIS_APP_ID = os.environ.get("LuisAppId", "")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", ""
    )
