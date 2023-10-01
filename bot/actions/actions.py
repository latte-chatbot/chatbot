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

class ActionUtterFontesConfiaveis(Action):
    def name(self) -> Text:
        return "action_utter_fontes_confiaveis"

    async def run(
        self, 
        dispatcher: CollectingDispatcher, 
        tracker: Tracker, 
        domain):

        dispatcher.utter_message(text="Teste Nesta funcionalidade, você terá acesso a uma variedade de fontes confiáveis para suas pesquisas. Explore as melhores bases acadêmicas para conduzir suas investigações!", parse_mode='Markdown')
        dispatcher.utter_message(text="**Selecione o seu estágio de pesquisa:**", parse_mode='Markdown')
        dispatcher.utter_message(text="1. **Exploração Inicial:** Acesse bases acadêmicas de fácil acesso com conteúdo geral, perfeitas para iniciantes em pesquisas (/iniciante).", parse_mode='Markdown')
        dispatcher.utter_message(text="2. **Navegando pelo Conhecimento:** Descubra bases acadêmicas detalhadas disponíveis para estudantes que desejam aprofundar suas pesquisas (/navegador).", parse_mode='Markdown')
        dispatcher.utter_message(text="3. **Explorando Conteúdos Avançados:** Explore bases acadêmicas altamente especializadas e detalhadas, que podem ter restrições de acesso. Este desafio é ideal para pesquisadores experientes que desejam se especializar ainda mais (/explorador).", parse_mode='Markdown')

        return [UserUtteranceReverted()]
