from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

#apikey = os.environ['apikey']
#url = os.environ['url']
authenticator = IAMAuthenticator('VG0DoENjrAbnMKFqBIuaHOEuvjGwNv8EQ568d1IsMUjA')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(
    'https://api.us-south.language-translator.watson.cloud.ibm.com/instances/2b9b3714-b9fe-447a-b5e6-3a3e90fa76e5')

def english_to_french(english_text):
    '''Translate from English to French'''
    translate_response=language_translator.translate(
        text = english_text, model_id='en-fr').get_result()
    french_text = translate_response['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    '''Translate from French to English'''
    translate_response=language_translator.translate(
        text = french_text, model_id='fr-en').get_result()
    english_text = translate_response['translations'][0]['translation']
    return english_text