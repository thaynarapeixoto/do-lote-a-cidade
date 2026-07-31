---
name: protocolo-cip
description: >-
  Classifica evidência em análises técnicas segundo o Protocolo C/I/P, que
  separa o que está Confirmado do que é Indício ou inferência e do que está
  Pendente, registrando também a origem de cada dado. Use quando o usuário
  precisa organizar informações de procedência mista, montar matriz de
  evidências, tratar dado informado por terceiro, decidir se uma informação
  pode ser afirmada, estruturar pendências com responsável, ou auditar um
  relatório em busca de afirmações sem lastro. Também use sempre que uma
  análise misturar documento oficial, observação de campo, informação de
  corretor e saída de ferramenta de IA no mesmo texto.
---

# Protocolo C/I/P

Protocolo de evidências do projeto **Contexto Primeiro**.

O problema que ele resolve é específico: em análise técnica, informação de origens muito diferentes chega ao mesmo parágrafo e sai dele com a mesma aparência de fato. Matrícula, print de satélite, fala de corretor e resposta de IA viram todas frases afirmativas. O leitor perde a capacidade de saber o que está sustentado.

O protocolo torna a procedência **um campo obrigatório**, não uma nota de rodapé.

---

## 1. Os dois campos

Todo dado relevante recebe **um status** e **uma origem**. São campos distintos, e nenhum dos dois é opcional.

### Status

| Letra | Nome | Definição |
| --- | --- | --- |
| **C** | Confirmado | Comprovado por documento, fonte oficial, levantamento ou evidência verificável e citável. |
| **I** | Indício ou inferência | Interpretação preliminar baseada nos elementos disponíveis. |
| **P** | Pendente | Ainda não comprovado. Exige consulta, documento, levantamento ou especialista. |

O que cai em **I**, e costuma ser tratado erradamente como C: leitura de imagem de satélite ou aerofotogrametria, observação de campo não instrumentada, dedução a partir de dado adjacente, e informação declarada por terceiro sem comprovação.

### Origem

Campo separado, registrado ao lado do status:

| Origem | O que é |
| --- | --- |
| `própria` | levantamento, medição ou observação feita por quem assina |
| `oficial` | órgão público, cartório, concessionária, publicação institucional |
| `técnica secundária` | literatura técnica, base de dados de terceiro, publicação especializada |
| `terceiro` | corretor, vendedor, proprietário, anúncio, relato |
| `IA` | qualquer saída de ferramenta de inteligência artificial |

---

## 2. Regras de acoplamento

1. **Origem `terceiro` ou `IA` tem status máximo I.** Nunca C, em nenhuma hipótese, por mais convincente que seja o conteúdo.
2. **Nada que saia de uma ferramenta de IA entra como C.** A IA não é fonte. Ela é camada de investigação e organização, e opera sobre o material que recebe.
3. **Promover I para C exige registrar o que sustentou a mudança:** documento, artigo, página, camada, anexo, data. Sem esse registro, a promoção não aconteceu, ainda que a informação esteja correta.
4. **Todo P carrega três campos obrigatórios:** por que importa, quem valida, qual decisão depende dele.
5. **Campo em branco é P, nunca N/A.** "Não aplicável" exige justificativa escrita.

### Por que informação de terceiro não é uma categoria própria

Uma versão anterior deste protocolo usava "I" para "informado por terceiro". Isso criava uma categoria confortável demais: o dado do corretor ficava a meio caminho de confirmado sem nunca ser tratado como o que é, uma alegação.

Movendo a procedência para o campo origem, o protocolo fica com três estados memorizáveis, e a informação de terceiro passa a carregar o mesmo peso de prova que qualquer outra leitura não validada. Isso não é desconfiança da pessoa. É a natureza da alegação.

---

## 3. Matriz de evidências

Formato de saída padrão. Uma linha por informação relevante.

| Informação | Valor | Status | Origem | Fonte | Data | O que falta |
| --- | --- | --- | --- | --- | --- | --- |
| Área da matrícula | 1.240,00 m² | C | oficial | Matrícula 12.345, 1º CRI, av. 3 | 12/06/2026 | |
| Área medida em campo | ~1.190 m² | I | própria | trena a laser, sem topógrafo | 20/06/2026 | levantamento com ART |
| Declividade | acentuada no fundo | I | IA | leitura de imagem de satélite | 21/06/2026 | topografia planialtimétrica |
| Zona e parâmetros | | P | | | | certidão de uso do solo |
| Rede de esgoto na testada | declarada existente | I | terceiro | informação do vendedor | 18/06/2026 | viabilidade da concessionária |

Duas coisas que essa matriz torna visíveis de imediato: existe uma divergência de 50 m² entre a área registral e a medida, e a única informação sobre esgoto veio de quem está vendendo.

---

## 4. Registro de pendência

Toda pendência usa este formato. Pendência sem os três campos é anotação, não pendência.

```
P-01 · Parâmetros urbanísticos do lote
  Por que importa: define o produto possível e o preço máximo pagável.
  Quem valida: Secretaria Municipal de Planejamento, via certidão de uso do solo.
  Decisão que depende: a proposta de compra não pode ser emitida antes.
  Prazo estimado: [P]
```

### Pendência crítica

É crítica quando a decisão não pode ser tomada sem ela, ou quando o resultado dela pode inviabilizar a hipótese.

Pendência crítica sem responsável definido rebaixa o nível de confiança da análise inteira para **baixa**, e confiança baixa não autoriza prosseguir.

---

## 5. Auditoria de um texto pronto

Para revisar um relatório, laudo preliminar ou apresentação em busca de afirmação sem lastro, procure:

| Padrão no texto | O que provavelmente é |
| --- | --- |
| "não há restrição" | ausência de informação apresentada como ausência de restrição |
| "o terreno permite" seguido de número | parâmetro sem lei, artigo e anexo ao lado |
| "segundo o mercado" | fonte setorial não nomeada, ou nenhuma fonte |
| "aproximadamente", "cerca de", sem origem | inferência com aparência de medição |
| número com precisão alta e sem metodologia | cálculo de terceiro reproduzido sem verificação |
| "conforme informado" | origem `terceiro` prestes a ser lida como C |
| "viável" ou "inviável" | conclusão que o método não autoriza |

Para cada ocorrência, devolva a frase, o status real e o que seria preciso para promovê-la.

---

## 6. O erro que este protocolo existe para impedir

**IA sem validação pode aumentar a aparência de certeza sem melhorar a decisão.**

Um texto gerado por ferramenta de IA é fluente, organizado e completo. Essas três qualidades são exatamente os sinais que um leitor técnico usa, inconscientemente, para calibrar confiança. O resultado é que a saída de IA tende a ser lida como mais confiável do que a anotação manuscrita de quem esteve no terreno, quando a relação correta é a inversa.

Marcar origem `IA` em todo dado produzido por ferramenta não é formalidade. É o que impede que a fluência seja lida como evidência.

---

<sub>Protocolo C/I/P, do projeto Contexto Primeiro, por Thaynara Peixoto Guimarães.</sub>
