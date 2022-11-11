import json

import aiounittest
from botbuilder.core import ConversationState, MemoryStorage, TurnContext
from botbuilder.core.adapters import TestAdapter

from booking_details import BookingDetails  # type: ignore
from config import DefaultConfig  # type: ignore
from dialogs import BookingDialog, MainDialog  # type: ignore
from flight_booking_recognizer import FlightBookingRecognizer  # type: ignore
from helpers.luis_helper import LuisConstants, LuisHelper  # type: ignore

import sys
from main import main

from aiounittest.case import AsyncTestCase

from config import DefaultConfig

from botbuilder.ai.luis import LuisRecognizer

from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

"""Tests for the main module"""
class MainTest(AsyncTestCase):
    def test_main(self):
        assert main() == 0, "Should be 0"


    def test_python_version(self):
        assert sys.version_info >= (
            3,
            8,
        ), "Python version should be >= 3.8"


        if __name__ == "__main__":
            test_main()
            test_python_version()
            print("Everything passed")

"""Test for check the endpoint construction of the LUIs recognizer."""

class LuisRecognizerTest(AsyncTestCase):

    CONFIG = DefaultConfig()
    _luisAppId: str = CONFIG.LUIS_APP_ID
    _subscriptionKey: str = CONFIG.LUIS_API_KEY
    _endpoint: str = "https://" + CONFIG.LUIS_API_HOST_NAME


    def test_luis_recognizer_construction(self):
        # Arrange
        endpoint = (
            LuisRecognizerTest._endpoint + "/luis/v0.1/apps/"
            + LuisRecognizerTest._luisAppId + "?verbose=true&timezoneOffset=-360"
            "&subscription-key=" + LuisRecognizerTest._subscriptionKey + "&q="
        )

        # Act
        recognizer = LuisRecognizer(endpoint)

        # Assert
        app = recognizer._application
        self.assertEqual(LuisRecognizerTest._luisAppId, app.application_id)
        self.assertEqual(LuisRecognizerTest._subscriptionKey, app.endpoint_key)
        self.assertEqual("https://westus.api.cognitive.microsoft.com", app.endpoint)


"""Tests for the bot module"""
class TestLuisHelper(aiounittest.AsyncTestCase):
    """Tests for the LUIS helper class"""

    async def test_execute_luis_query(self):
        """Tests the execute_luis_query method"""
        CONFIG = DefaultConfig()
        RECOGNIZER = FlightBookingRecognizer(CONFIG)

        async def exec_test(turn_context: TurnContext):
            """Executes the test"""
            # Call LUIS and gather any potential booking details. (Note the TurnContext has the response to the prompt.)
            intent, luis_result = await LuisHelper.execute_luis_query(
                RECOGNIZER, turn_context
            )
            await turn_context.send_activity(
                json.dumps(
                    {
                        "intent": intent,
                        "booking_details": luis_result.__dict__,
                    }
                )
            )

        adapter = TestAdapter(exec_test)

        await adapter.test(
            "Hello",
            json.dumps(
                {
                    "intent": LuisConstants.INFO_INTENT,
                    "booking_details": BookingDetails().__dict__,
                }
            ),
        )

        await adapter.test(
            "I want to go from Paris to London.",
            json.dumps(
                {
                    "intent": LuisConstants.BOOK_INTENT,
                    "booking_details": BookingDetails(
                        or_city="Paris",
                        dst_city="London",
                    ).__dict__,
                }
            ),
        )

        await adapter.test(
            "I want leave on the first of January 2023 and come back on the \
                17th of january 2023.",
            json.dumps(
                {
                    "intent": LuisConstants.INFO_INTENT,
                    "booking_details": BookingDetails(
                        str_date="2023-01-01",
                        end_date="2023-01-17",
                    ).__dict__,
                }
            ),
        )

        await adapter.test(
            "The trip should cost less than $100.",
            json.dumps(
                {
                    "intent": LuisConstants.INFO_INTENT,
                    "booking_details": BookingDetails(
                        budget="$100",
                    ).__dict__,
                }
            ),
        )

