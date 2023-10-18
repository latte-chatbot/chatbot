from rasa_sdk import Action
from .postgresConnection import SessionLocal, UserInfo


mensagensArtigo = [
    "🚀 Muito bem! Você iniciou sua jornada pelo mundo dos artigos. Comece com uma Introdução sólida para estabelecer uma base forte!\nNessa etapa, apresente seu tema, o problema de pesquisa e a relevância do estudo.\nProgresso atual: ░░░░░░░0%",
    "🎉 Ótimo progresso! Seguindo em frente, mergulhe na Revisão da Literatura.\nAqui, você discutirá trabalhos anteriores relacionados ao seu tema, identificando lacunas e construindo o contexto para seu estudo.\nProgresso atual: ▓░░░░░░15%",
    "📚 Está indo muito bem! Agora, vamos falar sobre a Metodologia.\nDescreva os métodos e ferramentas que você usará em sua pesquisa. Isso ajuda a dar credibilidade ao seu trabalho.\n Progresso atual: ▓▓░░░░░░30%",
    "🔍 Incrível! Com a Metodologia pronta, é hora de mostrar seus Resultados.\nApresente os dados coletados e as análises realizadas, mostrando as evidências de suas descobertas.\nProgresso atual: ▓▓▓░░░░45%",
    "🤔 Você está quase lá! Vamos à Discussão dos Resultados.\nNessa etapa, interprete e analise seus resultados, conectando-os de volta à revisão da literatura e destacando a importância de suas descobertas.\nProgresso atual: ▓▓▓▓░░░60%",
    "🎯 Quase concluindo! Agora, finalize com a Conclusão.\nReúna suas principais descobertas, discuta implicações e sugira direções para pesquisas futuras.Progresso atual: ▓▓▓▓▓░░75%",
    "📖 Último passo! Adicione suas Referências Bibliográficas.\nGaranta que todos os trabalhos citados estejam listados corretamente. Isso reforça a integridade e a qualidade do seu artigo.Progresso atual: ▓▓▓▓▓▓░90%"
]

class ActionIniciarArtigo(Action):

    def name(self):
        return "action_iniciar_artigo"

    def run(self, dispatcher, tracker, domain):
    
        sender_id = tracker.sender_id
        
        with SessionLocal() as session: 
            user = session.query(UserInfo).filter_by(id=sender_id).first()  
            if user.progresso_artigo == None:
                dispatcher.utter_message(text=f"Urru, vamos começar essa aventura pelo mundo dos artigos cinetíficos")
            else:
                dispatcher.utter_message(text=f"E lá vamos nós novamente, seu progresso foi reiniciado e vamos nos aventurar novamente")
            dispatcher.utter_message(text=f"Nessa jornada irei te guiar por cada etapa, explicando sobre cada uma delas, ao todo são 7 etapas:\n1. Introdução\n2. Revisão da literatura\n3. Metodologia\n4. Resultados\n5. Conclusão\n6. Referências Bibliográficas")
            dispatcher.utter_message(text=f"Ao finalizar uma fase me avise para que eu possa te ajudar na próxima!")
            dispatcher.utter_message(text=f"{mensagensArtigo[0]}")
            user.progresso_artigo = 0
            session.add(user)
            session.commit()
        return []

class ActionAvancarEstagioArtigo(Action):

    def name(self):
        return "action_avancar_estagio_artigo"

    def run(self, dispatcher, tracker, domain):
        
        sender_id = tracker.sender_id
        
        with SessionLocal() as session:
            user = session.query(UserInfo).filter_by(id=sender_id).first()
            if user.progresso_artigo is None:
                dispatcher.utter_message(text=f"Você ainda não iniciou a criação de artigos!")
            elif user.progresso_artigo == 5:
                dispatcher.utter_message(text=f"🏁 Progresso atual: ▓▓▓▓▓▓▓ 100%")
                dispatcher.utter_message(text=f"🎉🥳 Uau! Você cruzou a linha de chegada e completou sua jornada no mundo dos artigos científicos!")
                dispatcher.utter_message(text=f"📚 Foi uma honra te guiar por este caminho. Estou sempre aqui para te ajudar na próxima aventura acadêmica. Vamos juntos escrever mais capítulos dessa história!")
                user.progresso_artigo = None
            else:
                user.progresso_artigo += 1
                dispatcher.utter_message(text=f"{mensagensArtigo[user.progresso_artigo]}")
            session.add(user)
            session.commit()
        return []

class ActionReportarEstagioArtigo(Action):    
    
    def name(self):
        return "action_reportar_estagio_artigo"

    def run(self, dispatcher, tracker, domain):
        
        sender_id = tracker.sender_id
        
        with SessionLocal() as session:
            user = session.query(UserInfo).filter_by(id=sender_id).first()
            if user.progresso_artigo != None:
                dispatcher.utter_message(text=f"{mensagensArtigo[user.progresso_artigo]}")
            else:
                dispatcher.utter_message(text=f"Você ainda não iniciou a criação de artigos!")
        return []

