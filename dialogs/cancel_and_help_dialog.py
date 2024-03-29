# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Handle cancel and help intents."""

from botbuilder.core import BotTelemetryClient, NullTelemetryClient
from botbuilder.dialogs import (
    ComponentDialog,
    DialogContext,
    DialogTurnResult,
    DialogTurnStatus,
)
from botbuilder.schema import ActivityTypes


class CancelAndHelpDialog(ComponentDialog):
    """Implementation of handling cancel and help."""

    def __init__(
        self,
        dialog_id: str,
        telemetry_client: BotTelemetryClient = NullTelemetryClient(),
    ):
        """Initialize a new CancelAndHelpDialog instance."""
        super().__init__(dialog_id)
        self.telemetry_client = telemetry_client

    async def on_begin_dialog(
        self, inner_dc: DialogContext, options: object
    ) -> DialogTurnResult:
        """Handle the begin dialog event."""
        result = await self.interrupt(inner_dc)
        if result is not None:
            return result

        return await super().on_begin_dialog(inner_dc, options)

    async def on_continue_dialog(self, inner_dc: DialogContext) -> DialogTurnResult:
        """Handle the continue dialog event."""
        result = await self.interrupt(inner_dc)
        if result is not None:
            return result

        return await super().on_continue_dialog(inner_dc)

    async def interrupt(self, inner_dc: DialogContext) -> DialogTurnResult:
        """Detect interruptions."""
        if inner_dc.context.activity.type == ActivityTypes.message:
            text = inner_dc.context.activity.text.lower()

            if "help" in text or "?" in text:
                await inner_dc.context.send_activity(
                    """
Just tell me **where** you want to travel to (cities of origin and destination).
Ex. : _'I want to travel from Seattle to San Francisco'_\n

I will also need to know **when** you want to travel (dates of departure and return).
Ex. : _'I want to travel on May 1, 2020 and return on May 5, 2020'_\n

Finally, you can give me a **budget** for your trip.
Ex. : _'I want to travel for $500'_\n

🪃 We can sart over from scratch anytime if you just say _'Cancel'_"""
                )
                return DialogTurnResult(DialogTurnStatus.Waiting)

            if text in ("cancel", "quit"):
                await inner_dc.context.send_activity("Cancelling")
                return await inner_dc.cancel_all_dialogs()

        return None
