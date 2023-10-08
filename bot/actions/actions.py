import os
from sqlalchemy import create_engine, Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
        UserUtteranceReverted, 
        SessionStarted, 
        ActionExecuted, 
        EventType
)


PG_DB = os.environ['PG_DB']
PG_USERNAME = os.environ['PG_USERNAME']
PG_PASSWORD = os.environ['PG_PASSWORD']


Base = declarative_base()


class UserInfo(Base):
    __tablename__ = "usuario_info"

    id = Column(String, primary_key=True)


print("[INFO] Connecting to Postgres...")
DATABASE_URL = f"postgresql+psycopg2://{PG_USERNAME}:{PG_PASSWORD}@postgres:5432/{PG_DB}"
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)
print("[INFO] Connected to Postgres!")


class ActionSessionStart(Action):
    def name(self) -> Text:
        return "action_session_start"

    async def run(
        self, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        sender_id = tracker.sender_id
        
        with SessionLocal() as session:
            user = session.query(UserInfo).filter_by(id=sender_id).first()
            
            if not user:
                new_user = UserInfo(id=sender_id)
                session.add(new_user)
                session.commit()
                dispatcher.utter_message(template="utter_apresentacao")

        return [SessionStarted(), ActionExecuted("action_listen")]

    
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
