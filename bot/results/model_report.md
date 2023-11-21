
# Model health report
## Index
 - [Overview](#overview)
 - [Config](#configs)
 - [Intents](#intents)
 - [Entities](#entities)
 - [Core](#core)
 - [E2E Coverage](#e2e)


## Overview <a name='overview'></a>

### Bot info
|Bot Name|Creation date|Updated date|
|:-:|:-:|:-:|
|<span style='font-size:16px'>My project</span>|<span style='font-size:16px'>21/11/23 06:23:15</span>|<span style='font-size:16px'>21/11/23 06:23:21</span>|


### Score
|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>Overall</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|10            |-            |-            |10            |10            |<span style='font-size:20px'>**10**</span>|
🟢            |❌            |❌            |🟢            |🟢            |<span style='font-size:20px'>🟢</span>|
### Element count
Describe the number of elements in the chatbot.

|Element type|Total|
|:-:|:-:|
|Intents|59|
|Entities|0|
|Actions and Utters|71|
|Stories|54|
|Rules|8|



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
|#||intent|Precision|Recall|F1 Score|Examples|
|:-:|-|-|-|-|-|-|
|1|🟢|abnt|100.0%|100.0%|100.0%|14|
|2|🟢|revisao|100.0%|100.0%|100.0%|9|
|3|🟢|inciar_artigo|100.0%|100.0%|100.0%|10|
|4|🟢|avancar_estagio_artigo|100.0%|100.0%|100.0%|16|
|5|🟢|criacao|100.0%|100.0%|100.0%|16|
|6|🟢|menu|100.0%|100.0%|100.0%|9|
|7|🟢|checar_progresso_artigo|100.0%|100.0%|100.0%|10|
|8|🟢|originalidade|100.0%|100.0%|100.0%|16|
|9|🟢|plagio|100.0%|100.0%|100.0%|16|
|10|🟢|cumprimentar|100.0%|100.0%|100.0%|13|
|11|🟢|despedir|100.0%|100.0%|100.0%|4|
|12|🟢|saiba_mais|100.0%|100.0%|100.0%|14|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.

No confusions or errors of intent were found in this model.
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

|#||Response|Precision|Recall|F1 Score|Number of occurrences|
|:-:|-|-|-|-|-|-|
|1|🟢|utter_abnt/conceito|100.0%|100.0%|100.0%|1|
|2|🟢|utter_citacao_indireta_livro|100.0%|100.0%|100.0%|1|
|3|🟢|utter_referencia_internet|100.0%|100.0%|100.0%|1|
|4|🟢|utter_revisao/revisao_ortografia|100.0%|100.0%|100.0%|1|
|5|🟢|utter_google_scholar|100.0%|100.0%|100.0%|1|
|6|🟢|utter_web_of_science|100.0%|100.0%|100.0%|1|
|7|🟢|utter_saiba_mais|100.0%|100.0%|100.0%|1|
|8|🟢|utter_referencia_entrevista|100.0%|100.0%|100.0%|1|
|9|🟢|utter_originalidade/definicao_importancia|100.0%|100.0%|100.0%|1|
|10|🟢|action_iniciar_artigo|100.0%|100.0%|100.0%|1|
|11|🟢|utter_criacao|100.0%|100.0%|100.0%|1|
|12|🟢|utter_explicar_bibliografia|100.0%|100.0%|100.0%|1|
|13|🟢|utter_referencia_jornal|100.0%|100.0%|100.0%|1|
|14|🟢|utter_referencia_revista|100.0%|100.0%|100.0%|1|
|15|🟢|utter_abnt/margens|100.0%|100.0%|100.0%|1|
|16|🟢|utter_explicar_citacao_direta|100.0%|100.0%|100.0%|1|
|17|🟢|utter_explicar_citacao_indireta|100.0%|100.0%|100.0%|1|
|18|🟢|utter_abnt|100.0%|100.0%|100.0%|3|
|19|🟢|utter_plagio/detectar|100.0%|100.0%|100.0%|1|
|20|🟢|utter_revisao_bibliografica|100.0%|100.0%|100.0%|1|
|21|🟢|utter_arxiv|100.0%|100.0%|100.0%|1|
|22|🟢|utter_scopus|100.0%|100.0%|100.0%|1|
|23|🟢|utter_originalidade|100.0%|100.0%|100.0%|2|
|24|🟢|utter_citacao_direta_internet|100.0%|100.0%|100.0%|1|
|25|🟢|utter_navegador|100.0%|100.0%|100.0%|1|
|26|🟢|utter_fallback|100.0%|100.0%|100.0%|1|
|27|🟢|utter_originalidade/dicas|100.0%|100.0%|100.0%|1|
|28|🟢|utter_pesquisa_qualitativa|100.0%|100.0%|100.0%|1|
|29|🟢|utter_nature_research_journals|100.0%|100.0%|100.0%|1|
|30|🟢|action_avancar_estagio_artigo|100.0%|100.0%|100.0%|1|
|31|🟢|utter_fontes_confiaveis|100.0%|100.0%|100.0%|1|
|32|🟢|utter_pesquisa_empirica|100.0%|100.0%|100.0%|1|
|33|🟢|utter_citacao_indireta_entrevista|100.0%|100.0%|100.0%|1|
|34|🟢|utter_citacao_direta_jornal|100.0%|100.0%|100.0%|1|
|35|🟢|utter_citacao_indireta_doc_legal|100.0%|100.0%|100.0%|1|
|36|🟢|utter_referencia_dissertacao|100.0%|100.0%|100.0%|1|
|37|🟢|action_listen|100.0%|100.0%|100.0%|80|
|38|🟢|utter_menu|100.0%|100.0%|100.0%|1|
|39|🟢|utter_gerador_biblio_citacoes|100.0%|100.0%|100.0%|1|
|40|🟢|utter_referencia_doc_legal|100.0%|100.0%|100.0%|1|
|41|🟢|utter_citacao_direta_dissertacao|100.0%|100.0%|100.0%|1|
|42|🟢|utter_biblio_citacoes|100.0%|100.0%|100.0%|1|
|43|🟢|utter_citacao_indireta_jornal|100.0%|100.0%|100.0%|1|
|44|🟢|utter_referencia_livro|100.0%|100.0%|100.0%|1|
|45|🟢|utter_science_direct|100.0%|100.0%|100.0%|1|
|46|🟢|utter_citacao_indireta_dissertacao|100.0%|100.0%|100.0%|1|
|47|🟢|utter_pubmed|100.0%|100.0%|100.0%|1|
|48|🟢|utter_citacao_direta_doc_legal|100.0%|100.0%|100.0%|1|
|49|🟢|utter_abnt/consultar|100.0%|100.0%|100.0%|1|
|50|🟢|utter_revisao_sistematica|100.0%|100.0%|100.0%|1|
|51|🟢|utter_revisao|100.0%|100.0%|100.0%|3|
|52|🟢|utter_citacao_direta_entrevista|100.0%|100.0%|100.0%|1|
|53|🟢|utter_plagio/consequencias|100.0%|100.0%|100.0%|1|
|54|🟢|utter_citacao_indireta_revista|100.0%|100.0%|100.0%|1|
|55|🟢|utter_plagio|100.0%|100.0%|100.0%|4|
|56|🟢|utter_citacao_direta_revista|100.0%|100.0%|100.0%|1|
|57|🟢|utter_open_stax|100.0%|100.0%|100.0%|1|
|58|🟢|utter_cumprimentar|100.0%|100.0%|100.0%|1|
|59|🟢|utter_plagio/evitar|100.0%|100.0%|100.0%|1|
|60|🟢|utter_explicar_biblio_citacoes|100.0%|100.0%|100.0%|1|
|61|🟢|utter_estruturacao_artigos|100.0%|100.0%|100.0%|1|
|62|🟢|utter_revisao/revisao_gramatica|100.0%|100.0%|100.0%|1|
|63|🟢|utter_doaj|100.0%|100.0%|100.0%|1|
|64|🟢|utter_citacao_direta_livro|100.0%|100.0%|100.0%|1|
|65|🟢|utter_explorador|100.0%|100.0%|100.0%|1|
|66|🟢|utter_pesquisa_experimental|100.0%|100.0%|100.0%|1|
|67|🟢|utter_revisao/revisao_coesao|100.0%|100.0%|100.0%|1|
|68|🟢|utter_plagio/definicao|100.0%|100.0%|100.0%|1|
|69|🟢|utter_citacao_indireta_internet|100.0%|100.0%|100.0%|1|
|70|🟢|utter_explicar_citacao|100.0%|100.0%|100.0%|1|
|71|🟢|action_reportar_estagio_artigo|100.0%|100.0%|100.0%|1|
|72|🟢|utter_despedir|100.0%|100.0%|100.0%|1|
|73|🟢|utter_exploracao_inicial|100.0%|100.0%|100.0%|1|
### Confusion Matrix
![Confusion Matrix](.././results/story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents and responses that aren't covered by end-to-end tests.

### Not covered elements
List with not covered elements by end-to-end tests.

#### Intents
 - (no elements not covered)

#### Actions
 - (no elements not covered)

Total number of elements: 130

Total number of not covered elements: 0

Total number of excluded elements: 0

Coverage rate: 100.0% (🟢)


##### Generated by rasa-model-report v1.5.0, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).