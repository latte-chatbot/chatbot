
# Model health report
## Index
 - [Overview](#overview)
 - [Config](#configs)
 - [Intents](#intents)
 - [Entities](#entities)
 - [Core](#core)
 - [E2E Coverage](#e2e)


## Overview <a name='overview'></a>
|Bot Name|Creation date|Updated date|
|:-:|:-:|:-:|
|<span style='font-size:16px'>My project</span>|<span style='font-size:16px'>21/11/23 05:48:06</span>|<span style='font-size:16px'>21/11/23 05:48:12</span>|

|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>General</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|7.71            |-            |-            |10            |8.63            |<span style='font-size:20px'>**8.08**</span>|
🟡            |❌            |❌            |🟢            |🟡            |<span style='font-size:20px'>🟡</span>|

## Configs <a name='configs'></a>
Settings that were used in the training *pipeline* and *policies*.
```yaml
recipe: default.v1

language: pt_br

pipeline:
- name: WhitespaceTokenizer
- name: RegexFeaturizer
- name: LexicalSyntacticFeaturizer
- name: CountVectorsFeaturizer
- name: CountVectorsFeaturizer
  analyzer: char_wb
  min_ngram: 1
  max_ngram: 4
- name: EntitySynonymMapper
- name: DIETClassifier
  epochs: 80
  constrain_similarities: true
- name: ResponseSelector
  epochs: 100
  retrieval_intent: abnt
  constrain_similarities: true
- name: ResponseSelector
  epochs: 100
  retrieval_intent: plagio
  constrain_similarities: true
- name: ResponseSelector
  epochs: 100
  retrieval_intent: originalidade
  constrain_similarities: true
- name: ResponseSelector
  epochs: 100
  retrieval_intent: revisao
  constrain_similarities: true
- name: FallbackClassifier
  threshold: 0.7
  ambiguity_threshold: 0.2

policies:
- name: MemoizationPolicy
- name: TEDPolicy
  max_history: 5
  epochs: 100
  constrain_similarities: true
- name: RulePolicy
  core_fallback_threshold: 0.7
  core_fallback_action_name: "action_default_fallback"
  enable_fallback_prediction: true

assistant_id: latte_chatbot

```

## Intents <a name='intents'></a>
Section that discusses metrics on model intents.

### Metrics
Table with the metrics of intentions.
||intent|Precision|Recall|F1 Score|Examples|
|-|-|-|-|-|-|
|🟢|google_scholar|100.0%|100.0%|100.0%|2|
|🟢|despedir|100.0%|100.0%|100.0%|4|
|🟢|pubmed|100.0%|100.0%|100.0%|2|
|🟢|web_of_science|100.0%|100.0%|100.0%|2|
|🟢|referencia_dissertacao|100.0%|100.0%|100.0%|2|
|🟢|cumprimentar|100.0%|100.0%|100.0%|13|
|🟢|gerador_biblio_citacoes|100.0%|100.0%|100.0%|2|
|🟢|explicar_citacao|100.0%|100.0%|100.0%|2|
|🟢|explorador|100.0%|100.0%|100.0%|2|
|🟢|pesquisa_qualitativa|100.0%|100.0%|100.0%|3|
|🟢|citacao_indireta_dissertacao|100.0%|100.0%|100.0%|2|
|🟢|science_direct|100.0%|100.0%|100.0%|2|
|🟢|originalidade|100.0%|100.0%|100.0%|16|
|🟢|scopus|100.0%|100.0%|100.0%|2|
|🟢|plagio|100.0%|100.0%|100.0%|16|
|🟢|fontes_confiaveis|100.0%|100.0%|100.0%|8|
|🟢|pesquisa_experimental|100.0%|100.0%|100.0%|3|
|🟢|abnt|100.0%|100.0%|100.0%|11|
|🟢|arxiv|100.0%|100.0%|100.0%|2|
|🟢|revisao|100.0%|100.0%|100.0%|9|
|🟢|explicar_biblio_citacoes|100.0%|100.0%|100.0%|2|
|🟢|menu|100.0%|100.0%|100.0%|9|
|🟢|navegador|100.0%|100.0%|100.0%|2|
|🟢|estruturacao_artigos|100.0%|100.0%|100.0%|3|
|🟢|referencia_livro|100.0%|100.0%|100.0%|2|
|🟢|iniciante|100.0%|100.0%|100.0%|2|
|🟢|revisao_bibliografica|100.0%|100.0%|100.0%|3|
|🟢|saiba_mais|100.0%|100.0%|100.0%|14|
|🟢|explicar_bibliografia|100.0%|100.0%|100.0%|2|
|🟢|open_stax|100.0%|100.0%|100.0%|2|
|🟢|nature_research_journals|100.0%|100.0%|100.0%|2|
|🟢|doaj|100.0%|100.0%|100.0%|2|
|🟢|referencia_doc_legal|100.0%|100.0%|100.0%|2|
|🟢|citacao_direta_dissertacao|100.0%|100.0%|100.0%|2|
|🟢|biblio_citacoes|100.0%|100.0%|100.0%|4|
|🟢|criacao|100.0%|100.0%|100.0%|16|
|🟡|revisao_sistematica|75.0%|100.0%|85.7%|3|
|🟡|citacao_indireta_internet|66.7%|100.0%|80.0%|2|
|🟡|pesquisa_empirica|100.0%|66.7%|80.0%|3|
|🟠|citacao_direta_jornal|50.0%|100.0%|66.7%|2|
|🟠|citacao_indireta_doc_legal|50.0%|100.0%|66.7%|2|
|🟠|citacao_direta_livro|50.0%|100.0%|66.7%|2|
|🟠|referencia_entrevista|100.0%|50.0%|66.7%|2|
|🟠|explicar_citacao_direta|50.0%|100.0%|66.7%|2|
|🟠|citacao_indireta_revista|33.3%|100.0%|50.0%|2|
|🟠|citacao_direta_entrevista|50.0%|50.0%|50.0%|2|
|🟠|referencia_internet|25.0%|100.0%|40.0%|2|
|❌|citacao_indireta_jornal|0.0%|0.0%|0.0%|2|
|❌|citacao_indireta_entrevista|0.0%|0.0%|0.0%|2|
|❌|citacao_indireta_livro|0.0%|0.0%|0.0%|2|
|❌|citacao_direta_revista|0.0%|0.0%|0.0%|2|
|❌|explicar_citacao_indireta|0.0%|0.0%|0.0%|2|
|❌|citacao_direta_doc_legal|0.0%|0.0%|0.0%|2|
|❌|citacao_direta_internet|0.0%|0.0%|0.0%|2|
|❌|referencia_jornal|0.0%|0.0%|0.0%|2|
|❌|referencia_revista|0.0%|0.0%|0.0%|2|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.
|Text|Intent|Predicted Intent|Confidence|
|-|-|-|-|
|artigo_pesquisa_empirica|pesquisa_empirica|revisao_sistematica|54.7%|
|Como fazer citações indiretas de livros|citacao_indireta_livro|citacao_direta_livro|21.5%|
|Explicar sobre citações indiretas|explicar_citacao_indireta|explicar_citacao_direta|20.1%|
|Como fazer citações diretas de revistas|citacao_direta_revista|citacao_indireta_revista|19.5%|
|Como fazer citações indiretas de jornal|citacao_indireta_jornal|citacao_direta_jornal|19.4%|
|Explicar sobre citações indiretas de entrevistas|citacao_indireta_entrevista|citacao_indireta_revista|19.4%|
|Como fazer citações indiretas|explicar_citacao_indireta|explicar_citacao_direta|19.3%|
|Explicar sobre citações indiretas de jornal|citacao_indireta_jornal|citacao_direta_jornal|18.9%|
|Explicar sobre citações indiretas de livros|citacao_indireta_livro|citacao_direta_livro|18.6%|
|Explicar sobre citações diretas de revistas|citacao_direta_revista|citacao_indireta_revista|18.5%|
|Como fazer citações diretas de documentos legais|citacao_direta_doc_legal|citacao_indireta_doc_legal|18.3%|
|Explicar sobre referências bibliográficas de jornal|referencia_jornal|referencia_internet|18.1%|
|Como fazer referências bibliográficas de jornal|referencia_jornal|referencia_internet|17.4%|
|Explicar sobre citações diretas de um documento legal|citacao_direta_doc_legal|citacao_indireta_doc_legal|17.3%|
|Explicar sobre referências bibliográficas de revistas|referencia_revista|referencia_internet|17.0%|
|Como fazer citações indiretas de um entrevista|citacao_indireta_entrevista|citacao_direta_entrevista|16.1%|
|Explicar sobre citações diretas de entrevistas|citacao_direta_entrevista|citacao_indireta_revista|15.6%|
|Como fazer referências bibliográficas de revistas|referencia_revista|referencia_internet|15.1%|
|Explicar sobre citações diretas de páginas da internet|citacao_direta_internet|referencia_internet|11.3%|
|Explicar sobre referências bibliográficas de entrevistas|referencia_entrevista|referencia_internet|8.9%|
|Como fazer citações diretas da internet|citacao_direta_internet|citacao_indireta_internet|7.2%|
### Histogram
![Histogram](.././results/intent_histogram.png 'Histogram')
### Confusion Matrix
![Confusion Matrix](.././results/intent_confusion_matrix.png 'Confusion Matrix')

## Entities <a name='entities'></a>
Section that discusses metrics about the model entities.

### Metrics
Table with entity metrics.


No entities were found in this model.

### Confused entities
Where all the confusing or wrong entities of the model are listed.

No confusions of entities were found in this model.

## Core <a name='core'></a>
Section that discusses metrics about bot responses and actions.

### Metrics
Table with bot core metrics.

||Response|Precision|Recall|F1 Score|Number of occurrences|
|-|-|-|-|-|-|
|🟢|utter_estruturacao_artigos|100.0%|100.0%|100.0%|1|
|🟢|utter_gerador_biblio_citacoes|100.0%|100.0%|100.0%|1|
|🟢|utter_explorador|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_livro|100.0%|100.0%|100.0%|1|
|🟢|utter_despedir|100.0%|100.0%|100.0%|1|
|🟢|utter_fallback|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_doc_legal|100.0%|100.0%|100.0%|1|
|🟢|utter_fontes_confiaveis|100.0%|100.0%|100.0%|1|
|🟢|utter_pubmed|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_internet|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_jornal|100.0%|100.0%|100.0%|1|
|🟢|utter_explicar_citacao|100.0%|100.0%|100.0%|1|
|🟢|utter_open_stax|100.0%|100.0%|100.0%|1|
|🟢|utter_pesquisa_qualitativa|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_dissertacao|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_revista|100.0%|100.0%|100.0%|1|
|🟢|utter_criacao|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_doc_legal|100.0%|100.0%|100.0%|1|
|🟢|utter_explicar_biblio_citacoes|100.0%|100.0%|100.0%|1|
|🟢|utter_web_of_science|100.0%|100.0%|100.0%|1|
|🟢|utter_navegador|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_livro|100.0%|100.0%|100.0%|1|
|🟢|utter_exploracao_inicial|100.0%|100.0%|100.0%|1|
|🟢|utter_scopus|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_jornal|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_entrevista|100.0%|100.0%|100.0%|1|
|🟢|utter_plagio|100.0%|100.0%|100.0%|4|
|🟢|utter_abnt|100.0%|100.0%|100.0%|3|
|🟢|utter_doaj|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_internet|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_revista|100.0%|100.0%|100.0%|1|
|🟢|utter_google_scholar|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_dissertacao|100.0%|100.0%|100.0%|1|
|🟢|utter_explicar_bibliografia|100.0%|100.0%|100.0%|1|
|🟢|utter_originalidade|100.0%|100.0%|100.0%|2|
|🟢|utter_arxiv|100.0%|100.0%|100.0%|1|
|🟢|utter_pesquisa_experimental|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_dissertacao|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_internet|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_direta_entrevista|100.0%|100.0%|100.0%|1|
|🟢|utter_science_direct|100.0%|100.0%|100.0%|1|
|🟢|utter_revisao_bibliografica|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_doc_legal|100.0%|100.0%|100.0%|1|
|🟢|utter_explicar_citacao_indireta|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_jornal|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_entrevista|100.0%|100.0%|100.0%|1|
|🟢|utter_saiba_mais|100.0%|100.0%|100.0%|1|
|🟢|action_listen|100.0%|100.0%|100.0%|64|
|🟢|utter_nature_research_journals|100.0%|100.0%|100.0%|1|
|🟢|utter_explicar_citacao_direta|100.0%|100.0%|100.0%|1|
|🟢|utter_referencia_livro|100.0%|100.0%|100.0%|1|
|🟢|utter_cumprimentar|100.0%|100.0%|100.0%|1|
|🟢|utter_revisao|100.0%|100.0%|100.0%|3|
|🟢|utter_revisao_sistematica|100.0%|100.0%|100.0%|1|
|🟢|utter_pesquisa_empirica|100.0%|100.0%|100.0%|1|
|🟢|utter_biblio_citacoes|100.0%|100.0%|100.0%|1|
|🟢|utter_citacao_indireta_revista|100.0%|100.0%|100.0%|1|
### Confusion Matrix
![Confusion Matrix](.././results/story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents, entities and responses that aren't covered by end-to-end tests.

### Not covered elements
List with not covered elements by end-to-end tests.

#### Intents
 - menu

#### Actions
 - utter_apresentacao
 - utter_menu
 - utter_abnt/consultar
 - utter_abnt/margens
 - utter_abnt/conceito
 - utter_plagio/definicao
 - utter_plagio/consequencias
 - utter_plagio/evitar
 - utter_plagio/detectar
 - utter_originalidade/definicao_importancia
 - utter_originalidade/dicas
 - utter_revisao/revisao_ortografia
 - utter_revisao/revisao_gramatica
 - utter_revisao/revisao_coesao
 - action_session_start
 - action_default_fallback

Total number of elements: 124

Total number of not covered elements: 17

Coverage rate: 86.3% (🟡)


##### Generated by rasa-model-report, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).