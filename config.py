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
    APP_PASSWORD = "eaab3185-3119-45e7-9e9b-951b0dd92677" #os.environ.get("MicrosoftAppPassword", "")
    LUIS_APP_ID = "099431fb-d90d-44b6-a5cf-82a9d8f804e7" #os.environ.get("LuisAppId", "")
    LUIS_API_KEY = "93d125472bfd46c5ae0e599fcb8207c8"#os.environ.get("LuisAPIKey", "")
    LUIS_API_HOST_NAME = "westus.api.cognitive.microsoft.com"#os.environ.get("LuisAPIHostName", "")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get(
        "AppInsightsInstrumentationKey", ""
    )
