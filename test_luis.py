from aiounittest.case import AsyncTestCase

from config import DefaultConfig

from botbuilder.ai.luis import LuisRecognizer

from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

class LuisRecognizerTest(AsyncTestCase):
    """
    This set of 3 tests will:
    - Check the endpoint construction of the LUIs recognizer.
    - check no arg for the LuisRecognizer.
    - Try to recognize intent and entities to the Luis app, assertions for intent and entities are checked.
    """
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


# def test_luis_recognizer_none_luis_app_arg(self):
#         with self.assertRaises(TypeError):
#             LuisRecognizer(application=None)