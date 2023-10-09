import logging
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
        UserUtteranceReverted, 
        SessionStarted, 
        ActionExecuted
)
from .postgresConnection import SessionLocal, UserInfo


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
      self, dispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        logging.basicConfig(level=logging.DEBUG)

        sender_id = tracker.sender_id
        
        with SessionLocal() as session:
            user = session.query(UserInfo).filter_by(id=sender_id).first()
            logging.warning("NOT USER")
            logging.warning(sender_id)
            if not user:
                new_user = UserInfo(id=sender_id)
                session.add(new_user)
                session.commit()
                dispatcher.utter_message(template="utter_apresentacao")
                dispatcher.utter_message(template="utter_menu")

        return [SessionStarted(), ActionExecuted("action_listen")]

    
class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_fallback")
        return [UserUtteranceReverted()]
