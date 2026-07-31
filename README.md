# Do Lote à Cidade

Método de leitura preliminar de terreno, do projeto **Contexto Primeiro**, empacotado como skills para o Claude Code.

> **O terreno não termina na matrícula.**
>
> Nenhuma decisão sobre um terreno é responsável quando o contexto é tratado como detalhe.

---

## O problema

Uma arquiteta recebe um terreno e precisa descobrir o que é possível, quais são os riscos e o que ainda precisa ser validado. Ela abre uma ferramenta de IA e recebe, em segundos, um texto fluente, organizado e completo, com parâmetros urbanísticos, leitura de entorno e conclusão de viabilidade.

O texto tem três problemas que ele mesmo não declara: parte dos parâmetros foi inventada de forma plausível, a ausência de informação virou ausência de restrição, e a fluência foi lida como evidência.

**IA sem validação aumenta a aparência de certeza sem melhorar a decisão.** Essas skills existem para inverter isso.

---

## O que elas fazem de diferente

Não entregam mais números. Entregam **procedência**.

Toda informação produzida sob este método recebe um status e uma origem, em campos separados e obrigatórios:

| Status | Significa |
| --- | --- |
| **C** | Confirmado por documento, fonte oficial ou levantamento citável |
| **I** | Indício ou inferência a partir do que está disponível |
| **P** | Pendente, exige consulta, documento ou especialista |

E uma regra que não é negociável: **origem `IA` tem status máximo I**. Isso inclui tudo o que o modelo produzir na própria conversa. A IA é camada de investigação e organização, não é fonte.

Consequências práticas dentro de uma sessão:

- a conclusão nunca é "viável" ou "inviável", é um de cinco estados de saída, com nível de confiança calculado por regra;
- "não há restrição ambiental" é reescrito como "não foi encontrada informação sobre restrição ambiental", que é uma frase diferente e uma responsabilidade diferente;
- parâmetro urbanístico sem lei, artigo e anexo ao lado não entra como confirmado, ainda que esteja correto;
- toda pendência carrega por que importa, quem valida e qual decisão depende dela.

---

## Território

O método trata **legislação brasileira e prática brasileira**: Plano Diretor e leis complementares municipais, lei de uso e ocupação do solo, parcelamento do solo, matrícula e certidões, licenciamento ambiental, concessionárias, faixa de domínio, gleba e custo de urbanização.

Isso não é um recorte de mercado, é uma condição de funcionamento. Um método de análise de terreno que não sabe o que é uma averbação, uma certidão de uso do solo ou uma outorga onerosa não conduz uma leitura no Brasil.

---

## Skills

| Skill | O que faz |
| --- | --- |
| **`do-lote-a-cidade`** | conduz a leitura completa, em oito dimensões, do lote à região, e fecha em estado de saída com nível de confiança |
| **`protocolo-cip`** | classifica evidência, monta a matriz de procedência, trata pendências e audita texto pronto em busca de afirmação sem lastro |
| **`outorga-onerosa-goiania`** | dimensiona o custo do potencial construtivo adicional em Goiânia, com um calculador que devolve o valor junto da procedência de cada insumo |

### As oito dimensões

| | Dimensão | Pergunta |
| --- | --- | --- |
| **D1** | Enquadramento da decisão | O que estamos tentando decidir? |
| **D2** | Identidade e documentos | Que área é esta, e os documentos concordam entre si? |
| **D3** | Condições físicas | O que existe no terreno? |
| **D4** | Regras urbanísticas | O que pode ser feito aqui? |
| **D5** | Ambiente | O que protege, restringe ou condiciona? |
| **D6** | Infraestrutura e acessibilidade | O terreno é atendido e alcançável? |
| **D7** | Território e escalas | Como o terreno se conecta ao que está em volta? |
| **D8** | Mercado, riscos e encaminhamento | Para quem faz sentido, o que ameaça, qual o próximo passo? |

D2, D4 e D5 são dimensões críticas. Sem nenhuma evidência confirmada nelas, a leitura não sustenta conclusão além de "aprofundar antes de decidir" ou "suspender a análise". É regra, não julgamento.

---

## Instalação

Dentro do Claude Code:

```shell
/plugin marketplace add thaynarapeixoto/do-lote-a-cidade
/plugin install do-lote-a-cidade@contexto-primeiro
/reload-plugins
```

As skills passam a responder como `do-lote-a-cidade:do-lote-a-cidade`, `do-lote-a-cidade:protocolo-cip` e `do-lote-a-cidade:outorga-onerosa-goiania`. Elas também são acionadas sozinhas quando a conversa entra no assunto, sem precisar de comando.

Para testar sem instalar, clone o repositório e rode:

```bash
claude --plugin-dir ./do-lote-a-cidade
```

### O calculador

```bash
python3 skills/outorga-onerosa-goiania/scripts/outorga_goiania.py \
  --qsc 2500 --area adensavel \
  --cub 2350.00 --cub-data 06/2026 --percentual-cub 50
```

Sem dependências externas, Python 3.8+. Ele devolve a contrapartida estimada acompanhada do status de cada insumo, da lista de pendências e do motivo pelo qual o resultado não pode ser usado em proposta comercial. Foi escrito para não deixar o número sair limpo.

---

## O que este material não é

Não produz estudo conclusivo de viabilidade, laudo técnico, parecer jurídico, análise registral, estudo ambiental, avaliação imobiliária, projeto, consulta municipal, certidão, autorização ou recomendação de investimento.

Não substitui legislação vigente, certidões, levantamento de campo, visita técnica, consulta a órgãos, especialista nem responsabilidade técnica. Ver [`LIMITACOES.md`](LIMITACOES.md).

---

## Sobre

**Thaynara Peixoto Guimarães** é arquiteta e urbanista. Atua com gestão de empreendimentos imobiliários, parcelamento do solo, análise de terrenos e glebas, e estruturação de decisões territoriais por dados e processos.

Criadora do **Contexto Primeiro**, projeto de inteligência territorial para decisões antes do projeto.

Licença: ver [`LICENCA.md`](LICENCA.md). Conteúdo em CC BY 4.0, scripts em MIT.
