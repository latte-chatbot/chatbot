# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class action_falar_nome(Action):
    def name(self) -> Text:
        return "action_falar_nome"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get.slot("nome")
        dispatcher.utter_message(text=f"A partir de agora irei chamá-lo de {nome}!")
        return []

class action_falar_tema_pesquisa(Action):
    def name(self) -> Text:
        return "action_falar_tema_pesquisa"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        tema_pesquisa = tracker.get.slot("tema_pesquisa")
        dispatcher.utter_message(text=f"Anotado! A partir de agora irei ajudá-lo em sua pesquisa sobre {tema_pesquisa}!")
        return []
