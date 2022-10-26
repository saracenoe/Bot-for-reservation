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
    APP_ID = os.environ.get("MicrosoftAppId", "315267ba-6800-4298-bb32-5dd8a7948435")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "eaab3185-3119-45e7-9e9b-951b0dd92677")
    LUIS_APP_ID = os.environ.get("LuisAppId", "099431fb-d90d-44b6-a5cf-82a9d8f804e7")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "93d125472bfd46c5ae0e599fcb8207c8")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "westus.api.cognitive.microsoft.com")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", ""
    )
