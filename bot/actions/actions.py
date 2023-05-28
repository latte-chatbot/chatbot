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

# Informações do usuário
#class ActionInformouNome(Action):
#    def name(self) -> Text:
#        return "action_informou_nome"
#    
#    def run(self, 
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        nome_usuario = tracker.get_slot("nome_usuario")
#        dispatcher.utter_message(text=f"A partir de agora irei chamá-lo de {nome_usuario}!")
#        return []
#
#class ActionInformouTemaPesquisa(Action):
#    def name(self) -> Text:
#        return "action_informou_tema_pesquisa"
#    
#    def run(self, 
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        tema_pesquisa = tracker.get_slot("tema_pesquisa")
#        dispatcher.utter_message(text=f"Anotado! Pesquisaremos juntos sobre {tema_pesquisa}!")
#        return []
#    
#class ActionInformouStringBuscas(Action):
#    def name(self) -> Text:
#        return "action_informou_string_buscas"
#    
#    def run(self, 
#            dispatcher: CollectingDispatcher,
#            tracker: Tracker,
#            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#        tema_pesquisa = tracker.get_slot("tema_pesquisa")
#        string_buscas = tracker.get_slot("string_buscas")
#        dispatcher.utter_message(text=f"Feito, defini a string de busca de sua pesquisa sobre {tema_pesquisa} \"como {string_buscas}\"!")
#        return []

# Demais ações
class ActionCumprimentarNovamente(Action):
    def name(self) -> Text:
        return "action_cumprimentar_novamente"
    
    def run(self, 
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        nome = tracker.get_slot("nome")
        if not nome:
            dispatcher.utter_message(text=f"Bem-vindo novamente, caro pesquisador!")
        else:
            dispatcher.utter_message(text=f"Quanto tempo {nome}, tudo bem?!")
        return []
