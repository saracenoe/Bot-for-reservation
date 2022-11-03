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
    APP_TYPE =  "MultiTenant"
    APP_ID = "315267ba-6800-4298-bb32-5dd8a7948435"
    APP_PASSWORD = "D5i8Q~TZ5~GkQ8pPeJI3tsR9tZYZ.8-qFmZYWahG"
    LUIS_APP_ID = "099431fb-d90d-44b6-a5cf-82a9d8f804e7"
    LUIS_API_KEY = "93d125472bfd46c5ae0e599fcb8207c8"
    LUIS_API_HOST_NAME = "westus.api.cognitive.microsoft.com"
    APPINSIGHTS_INSTRUMENTATION_KEY = "ba64b9c6-ff1a-4257-9823-01e764b831f5"
