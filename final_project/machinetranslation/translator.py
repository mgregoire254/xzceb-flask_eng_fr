import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

#Authentication
authenticator = IAMAuthenticator('0tg4E-rDltMvnAUt44xL_9GzldtVvW1OM4jxlSYyZUYm')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
#Creates instance of translation service
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/a77d6c32-5666-4c8b-8a71-8caa172aef0a')

def english_to_french(english_text):
    """translates english text to french"""
    frenchtranslation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    return frenchtranslation.get("translations")[0].get("translation")

def french_to_english(french_text):
    """Translates french text to english"""
    english_text = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    return english_text.get("translations")[0].get("translation")
