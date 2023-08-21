from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
        UserUtteranceReverted, 
        SessionStarted, 
        ActionExecuted, 
        EventType, 
        Restarted, 
        FollowupAction
)


#Ações Padrão
class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        dispatcher.utter_message(template="utter_apresentacao")
        return [SessionStarted(), ActionExecuted("action_listen")]

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        return [Restarted(), FollowupAction("action_session_start")]
    
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_core_fallback")
        return [UserUtteranceReverted()]


# Gamificação

## Barra de progressão

class ActionCalculateLevel(Action):
    def name(self):
        return "action_calculate_level"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]):
        experience = tracker.get_slot("experience")  # Recupera a experiência atual do usuário
        level = experience // 100  # Cada 100 pontos de experiência, o usuário aumenta 1 nível
        dispatcher.utter_message(text=f"Parabéns! Você atingiu o nível {level}.")
        return []

