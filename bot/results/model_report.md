
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
|<span style='font-size:16px'>My project</span>|<span style='font-size:16px'>21/11/23 06:40:32</span>|<span style='font-size:16px'>21/11/23 06:40:38</span>|


### Score
|Intent|Entity|NLU|Core|E2E Coverage|<span style='font-size:20px'>Overall</span>|
|:-:|:-:|:-:|:-:|:-:|:-:|
|8.49            |-            |-            |10            |8.95            |<span style='font-size:20px'>**8.71**</span>|
🟡            |❌            |❌            |🟢            |🟡            |<span style='font-size:20px'>🟡</span>|
### Element count
Describe the number of elements in the chatbot.

|Element type|Total|
|:-:|:-:|
|Intents|56|
|Entities|0|
|Actions and Utters|68|
|Stories|51|
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
|1|🟢|arxiv|100.0%|100.0%|100.0%|2|
|2|🟢|navegador|100.0%|100.0%|100.0%|2|
|3|🟢|despedir|100.0%|100.0%|100.0%|4|
|4|🟢|science_direct|100.0%|100.0%|100.0%|2|
|5|🟢|saiba_mais|100.0%|100.0%|100.0%|14|
|6|🟢|explicar_citacao_direta|100.0%|100.0%|100.0%|2|
|7|🟢|fontes_confiaveis|100.0%|100.0%|100.0%|8|
|8|🟢|google_scholar|100.0%|100.0%|100.0%|2|
|9|🟢|web_of_science|100.0%|100.0%|100.0%|2|
|10|🟢|abnt|100.0%|100.0%|100.0%|11|
|11|🟢|pubmed|100.0%|100.0%|100.0%|2|
|12|🟢|gerador_biblio_citacoes|100.0%|100.0%|100.0%|2|
|13|🟢|pesquisa_qualitativa|100.0%|100.0%|100.0%|3|
|14|🟢|citacao_direta_revista|100.0%|100.0%|100.0%|2|
|15|🟢|revisao|100.0%|100.0%|100.0%|9|
|16|🟢|nature_research_journals|100.0%|100.0%|100.0%|2|
|17|🟢|open_stax|100.0%|100.0%|100.0%|2|
|18|🟢|citacao_direta_jornal|100.0%|100.0%|100.0%|2|
|19|🟢|referencia_livro|100.0%|100.0%|100.0%|2|
|20|🟢|doaj|100.0%|100.0%|100.0%|2|
|21|🟢|originalidade|100.0%|100.0%|100.0%|16|
|22|🟢|cumprimentar|100.0%|100.0%|100.0%|13|
|23|🟢|revisao_bibliografica|100.0%|100.0%|100.0%|3|
|24|🟢|pesquisa_experimental|100.0%|100.0%|100.0%|3|
|25|🟢|estruturacao_artigos|100.0%|100.0%|100.0%|3|
|26|🟢|criacao|100.0%|100.0%|100.0%|16|
|27|🟢|biblio_citacoes|100.0%|100.0%|100.0%|4|
|28|🟢|explicar_citacao_indireta|100.0%|100.0%|100.0%|2|
|29|🟢|explorador|100.0%|100.0%|100.0%|2|
|30|🟢|explicar_citacao|100.0%|100.0%|100.0%|2|
|31|🟢|explicar_biblio_citacoes|100.0%|100.0%|100.0%|2|
|32|🟢|referencia_dissertacao|100.0%|100.0%|100.0%|2|
|33|🟢|referencia_internet|100.0%|100.0%|100.0%|2|
|34|🟢|citacao_indireta_jornal|100.0%|100.0%|100.0%|2|
|35|🟢|iniciante|100.0%|100.0%|100.0%|2|
|36|🟢|scopus|100.0%|100.0%|100.0%|2|
|37|🟢|plagio|100.0%|100.0%|100.0%|16|
|38|🟢|menu|81.8%|100.0%|90.0%|9|
|39|🟡|pesquisa_empirica|75.0%|100.0%|85.7%|3|
|40|🟡|citacao_indireta_dissertacao|66.7%|100.0%|80.0%|2|
|41|🟡|referencia_jornal|66.7%|100.0%|80.0%|2|
|42|🟡|revisao_sistematica|100.0%|66.7%|80.0%|3|
|43|🟡|referencia_revista|66.7%|100.0%|80.0%|2|
|44|🟡|citacao_direta_doc_legal|66.7%|100.0%|80.0%|2|
|45|🟡|referencia_doc_legal|66.7%|100.0%|80.0%|2|
|46|🟠|citacao_direta_dissertacao|100.0%|50.0%|66.7%|2|
|47|🟠|explicar_bibliografia|100.0%|50.0%|66.7%|2|
|48|🟠|citacao_direta_internet|50.0%|100.0%|66.7%|2|
|49|🟠|citacao_indireta_livro|50.0%|100.0%|66.7%|2|
|50|🟠|referencia_entrevista|100.0%|50.0%|66.7%|2|
|51|🟠|citacao_indireta_entrevista|50.0%|100.0%|66.7%|2|
|52|❌|citacao_direta_livro|0.0%|0.0%|0.0%|2|
|53|❌|citacao_direta_entrevista|0.0%|0.0%|0.0%|2|
|54|❌|citacao_indireta_doc_legal|0.0%|0.0%|0.0%|2|
|55|❌|citacao_indireta_internet|0.0%|0.0%|0.0%|2|
|56|❌|citacao_indireta_revista|0.0%|0.0%|0.0%|2|

### Confused intentions
Where all the confusing or wrong sentences of the model are listed.
|#|Text|Intent|Predicted Intent|Confidence|
|:-:|-|-|-|-|
|1|artigo_pesquisa_empirica|revisao_sistematica|pesquisa_empirica|51.3%|
|2|Como fazer citações diretas de dissertação|citacao_direta_dissertacao|citacao_indireta_dissertacao|36.6%|
|3|Explicar sobre referências bibliográficas de entrevistas|referencia_entrevista|referencia_revista|28.1%|
|4|Explicar sobre citações indiretas de páginas da internet|citacao_indireta_internet|citacao_direta_internet|27.0%|
|5|Como fazer uma referência bibliográfica|explicar_bibliografia|referencia_jornal|23.4%|
|6|Como fazer citações indiretas da internet|citacao_indireta_internet|citacao_direta_internet|21.2%|
|7|Como fazer citações indiretas de documentos legais|citacao_indireta_doc_legal|referencia_doc_legal|14.0%|
|8|Como fazer citações diretas de um entrevista|citacao_direta_entrevista|citacao_indireta_entrevista|13.3%|
|9|Explicar sobre citações diretas de entrevistas|citacao_direta_entrevista|citacao_indireta_entrevista|13.2%|
|10|Explicar sobre citações indiretas de um documento legal|citacao_indireta_doc_legal|citacao_direta_doc_legal|11.8%|
|11|Como fazer citações indiretas de revistas|citacao_indireta_revista|menu|10.6%|
|12|Explicar sobre citações indiretas de revistas|citacao_indireta_revista|menu|8.7%|
|13|Como fazer citações diretas de livros|citacao_direta_livro|citacao_indireta_livro|7.4%|
|14|Explicar sobre citações diretas de livros|citacao_direta_livro|citacao_indireta_livro|7.1%|
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
|1|🟢|utter_scopus|100.0%|100.0%|100.0%|1|
|2|🟢|utter_revisao|100.0%|100.0%|100.0%|3|
|3|🟢|utter_explicar_citacao_direta|100.0%|100.0%|100.0%|1|
|4|🟢|utter_open_stax|100.0%|100.0%|100.0%|1|
|5|🟢|utter_citacao_indireta_jornal|100.0%|100.0%|100.0%|1|
|6|🟢|utter_citacao_direta_entrevista|100.0%|100.0%|100.0%|1|
|7|🟢|utter_estruturacao_artigos|100.0%|100.0%|100.0%|1|
|8|🟢|utter_citacao_indireta_internet|100.0%|100.0%|100.0%|1|
|9|🟢|utter_nature_research_journals|100.0%|100.0%|100.0%|1|
|10|🟢|utter_abnt|100.0%|100.0%|100.0%|3|
|11|🟢|utter_referencia_entrevista|100.0%|100.0%|100.0%|1|
|12|🟢|utter_referencia_doc_legal|100.0%|100.0%|100.0%|1|
|13|🟢|utter_referencia_revista|100.0%|100.0%|100.0%|1|
|14|🟢|utter_fallback|100.0%|100.0%|100.0%|1|
|15|🟢|utter_science_direct|100.0%|100.0%|100.0%|1|
|16|🟢|utter_pesquisa_experimental|100.0%|100.0%|100.0%|1|
|17|🟢|utter_revisao_bibliografica|100.0%|100.0%|100.0%|1|
|18|🟢|utter_explicar_citacao_indireta|100.0%|100.0%|100.0%|1|
|19|🟢|utter_referencia_dissertacao|100.0%|100.0%|100.0%|1|
|20|🟢|utter_exploracao_inicial|100.0%|100.0%|100.0%|1|
|21|🟢|utter_explicar_bibliografia|100.0%|100.0%|100.0%|1|
|22|🟢|utter_gerador_biblio_citacoes|100.0%|100.0%|100.0%|1|
|23|🟢|utter_explicar_biblio_citacoes|100.0%|100.0%|100.0%|1|
|24|🟢|utter_doaj|100.0%|100.0%|100.0%|1|
|25|🟢|utter_pesquisa_empirica|100.0%|100.0%|100.0%|1|
|26|🟢|utter_citacao_direta_dissertacao|100.0%|100.0%|100.0%|1|
|27|🟢|utter_originalidade|100.0%|100.0%|100.0%|2|
|28|🟢|utter_despedir|100.0%|100.0%|100.0%|1|
|29|🟢|utter_saiba_mais|100.0%|100.0%|100.0%|1|
|30|🟢|utter_explicar_citacao|100.0%|100.0%|100.0%|1|
|31|🟢|utter_citacao_indireta_dissertacao|100.0%|100.0%|100.0%|1|
|32|🟢|utter_pubmed|100.0%|100.0%|100.0%|1|
|33|🟢|utter_fontes_confiaveis|100.0%|100.0%|100.0%|1|
|34|🟢|utter_criacao|100.0%|100.0%|100.0%|1|
|35|🟢|utter_explorador|100.0%|100.0%|100.0%|1|
|36|🟢|utter_referencia_internet|100.0%|100.0%|100.0%|1|
|37|🟢|utter_citacao_direta_internet|100.0%|100.0%|100.0%|1|
|38|🟢|utter_citacao_indireta_livro|100.0%|100.0%|100.0%|1|
|39|🟢|utter_biblio_citacoes|100.0%|100.0%|100.0%|1|
|40|🟢|utter_citacao_direta_jornal|100.0%|100.0%|100.0%|1|
|41|🟢|utter_citacao_indireta_doc_legal|100.0%|100.0%|100.0%|1|
|42|🟢|utter_citacao_indireta_revista|100.0%|100.0%|100.0%|1|
|43|🟢|utter_revisao_sistematica|100.0%|100.0%|100.0%|1|
|44|🟢|action_listen|100.0%|100.0%|100.0%|64|
|45|🟢|utter_citacao_direta_livro|100.0%|100.0%|100.0%|1|
|46|🟢|utter_referencia_livro|100.0%|100.0%|100.0%|1|
|47|🟢|utter_web_of_science|100.0%|100.0%|100.0%|1|
|48|🟢|utter_citacao_direta_revista|100.0%|100.0%|100.0%|1|
|49|🟢|utter_citacao_direta_doc_legal|100.0%|100.0%|100.0%|1|
|50|🟢|utter_plagio|100.0%|100.0%|100.0%|4|
|51|🟢|utter_pesquisa_qualitativa|100.0%|100.0%|100.0%|1|
|52|🟢|utter_referencia_jornal|100.0%|100.0%|100.0%|1|
|53|🟢|utter_arxiv|100.0%|100.0%|100.0%|1|
|54|🟢|utter_google_scholar|100.0%|100.0%|100.0%|1|
|55|🟢|utter_citacao_indireta_entrevista|100.0%|100.0%|100.0%|1|
|56|🟢|utter_navegador|100.0%|100.0%|100.0%|1|
|57|🟢|utter_cumprimentar|100.0%|100.0%|100.0%|1|
### Confusion Matrix
![Confusion Matrix](.././results/story_confusion_matrix.png 'Confusion Matrix')

## E2E Coverage <a name='e2e'></a>
Section that shows data from intents and responses that aren't covered by end-to-end tests.

### Not covered elements
List with not covered elements by end-to-end tests.

#### Intents
 - menu

#### Actions
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

Total number of elements: 124

Total number of not covered elements: 13

Total number of excluded elements: 0

Coverage rate: 89.5% (🟡)


##### Generated by rasa-model-report v1.5.0, collaborative open-source project for Rasa projects. Github repository at this [link](https://github.com/brunohjs/rasa-model-report).