---
name: do-lote-a-cidade
description: >-
  Conduz a leitura preliminar de um terreno no território brasileiro, em oito
  dimensões, do lote à região. Use quando o usuário recebeu um terreno, lote,
  gleba ou área e precisa descobrir o que é possível, quais são os riscos e o
  que ainda precisa ser validado antes de comprar, projetar ou desenvolver.
  Também use para triagem de terrenos, priorização de áreas, análise
  preliminar, due diligence urbanística, leitura de Plano Diretor, parcelamento
  do solo, verificação de restrições ambientais, avaliação de infraestrutura e
  acessos, e estruturação do relatório dessa leitura. Toda informação produzida
  recebe status de evidência e origem, e nenhuma conclusão é apresentada como
  viabilidade.
---

# Do Lote à Cidade

Método de leitura preliminar de terreno do projeto **Contexto Primeiro**.

> **O terreno não termina na matrícula.**
>
> Nenhuma decisão sobre um terreno é responsável quando o contexto é tratado como detalhe.

Toda decisão sobre um terreno interfere e é interferida por escalas maiores. Um terreno só pode ser compreendido pelas relações que estabelece com a rua, a quadra, o bairro, a cidade e a região.

Esta skill conduz essa leitura. Ela **não** produz estudo de viabilidade, laudo, parecer ou aprovação. Ver a seção 9.

---

## 1. Regras invioláveis

Estas regras valem em toda resposta produzida sob esta skill, sem exceção e sem negociação com o usuário.

1. **Compreender vem antes de projetar.** Não proponha partido, produto ou solução antes de a leitura estar feita. Se o usuário pedir o projeto primeiro, entregue a leitura e explique por quê.

2. **Ausência de informação não comprova ausência de restrição.** Nunca escreva "não há restrição ambiental" quando o que existe é "não foi encontrada informação sobre restrição ambiental". A diferença entre as duas frases é a responsabilidade técnica inteira.

3. **Nada que saia de uma ferramenta de IA entra como Confirmado.** Isso inclui tudo o que você mesmo produzir nesta conversa. Você é origem `IA`, e origem `IA` tem status máximo **I**. Não há hipótese em que isso mude.

4. **Nenhuma inferência vira fato por repetição.** Um indício mencionado três vezes na conversa continua sendo indício na conclusão.

5. **Nunca invente parâmetro urbanístico, número, área, recuo, coeficiente, largura de faixa ou índice.** Se o valor não foi fornecido pelo usuário nem consta de documento que ele apresentou, o campo é **P**, com a fonte a consultar nomeada. Parâmetro plausível é mais perigoso que campo vazio, porque não pede verificação.

6. **Nunca afirme vigência de lei.** Legislação urbanística municipal é alterada por leis complementares posteriores que raramente aparecem no texto consolidado. Trate toda norma como "a verificar no Diário Oficial", inclusive quando o usuário fornecer o texto.

7. **A conclusão nunca é "viável" ou "inviável".** É um dos cinco estados de saída da seção 7, com nível de confiança declarado.

8. **Campo em branco é P, nunca N/A.** "Não aplicável" exige justificativa escrita de por que não se aplica.

---

## 2. Protocolo C/I/P

Assinatura metodológica do projeto. Todo dado relevante recebe **um status** e **uma origem**, em campos distintos e obrigatórios.

### Status

| Letra | Nome | Definição |
| --- | --- | --- |
| **C** | Confirmado | Comprovado por documento, fonte oficial, levantamento ou evidência verificável e citável. |
| **I** | Indício ou inferência | Interpretação preliminar baseada nos elementos disponíveis. Inclui leitura de imagem, observação de campo não instrumentada, dedução a partir de dado adjacente e informação declarada por terceiro sem comprovação. |
| **P** | Pendente | Informação ainda não comprovada, que exige consulta, documento, levantamento ou especialista. |

### Origem

Campo separado, registrado ao lado do status: `própria` · `oficial` · `técnica secundária` · `terceiro` · `IA`.

### Acoplamento

1. Origem `terceiro` ou `IA` tem status máximo **I**. Nunca C, em nenhuma hipótese.
2. Promover I para C exige registrar o documento, artigo, página, camada ou anexo que sustentou a mudança. Sem esse registro, a promoção não acontece.
3. Todo **P** carrega três campos obrigatórios: **por que importa**, **quem valida**, **qual decisão depende dele**. P sem os três é anotação, não pendência.

> Informação de corretor, de vendedor, de proprietário ou de anúncio é origem `terceiro`. Ela carrega o mesmo peso de prova que qualquer leitura não validada, que é zero. Isso não é desconfiança da pessoa, é a natureza da alegação.

Para o tratamento detalhado, use a skill `protocolo-cip`.

---

## 3. Como conduzir a leitura

**Sequência obrigatória.** D1 vem sempre primeiro. Identificação do estudo é metadado de capa, não dimensão.

1. **Enquadre a decisão.** Sem D1, as sete dimensões seguintes viram coleta de dados sem destino.
2. **Levante o que o usuário já tem**, e classifique cada item com status e origem antes de qualquer análise.
3. **Percorra D2 a D8 na ordem.** Não pule dimensão por parecer irrelevante. Registre por que ela não se aplica.
4. **Acione o modo gleba** se o imóvel não for lote urbano consolidado. Ver seção 6.
5. **Verifique as dimensões críticas.** D2, D4 e D5. Ver seção 8.
6. **Feche em estado de saída, com nível de confiança.** Ver seção 7.

### O que perguntar antes de começar

Se o usuário não informou, pergunte, e não presuma:

- o que ele está tentando decidir, e em que prazo;
- se o imóvel é lote urbano consolidado ou gleba;
- o município e o estado, porque o método é o mesmo e a legislação não;
- que documentos ele tem em mãos;
- se ele já esteve no terreno;
- quem decide, e com base em quê.

### Padrão de cada dimensão

Estrutura recorrente. A repetição é o que torna o método reconhecível, e é o que permite comparar dois terrenos:

1. O que investigar
2. Por que isso interfere na decisão
3. Informações e documentos necessários
4. Fontes possíveis
5. Perguntas de investigação
6. Como a IA pode apoiar
7. O que exige validação obrigatória
8. Sinais de alerta
9. Como registrar a evidência
10. Resultado esperado da etapa

---

## 4. As oito dimensões

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

### D1 · Enquadramento da decisão

**O que investigar:** qual decisão está sobre a mesa, quem decide, qual o prazo, qual o custo de errar, qual hipótese de produto ou uso está em teste, e qual o orçamento disponível para investigar.

**Por que interfere:** a mesma área produz leituras diferentes conforme a decisão. Comprar, permutar, projetar, priorizar entre cinco terrenos e responder a um cliente são perguntas distintas, e a profundidade proporcional a cada uma também.

**Validação obrigatória:** a hipótese em teste precisa ser declarada por escrito. Uma leitura sem hipótese não tem como concluir "reformular a hipótese", que é um dos cinco estados de saída.

**Sinais de alerta:** o usuário não sabe dizer o que quer decidir; o prazo é incompatível com as consultas obrigatórias; a decisão já foi tomada e a análise está sendo pedida para justificá-la.

**Resultado esperado:** uma frase que declara a decisão, o decisor, o prazo e a hipótese.

### D2 · Identidade e documentos

**O que investigar:** que área é esta juridicamente, e se os documentos concordam entre si.

**Documentos:** matrícula atualizada no Cartório de Registro de Imóveis competente, certidão de ônus reais, certidão de ações reipersecutórias, cadastro municipal e IPTU, planta aprovada quando existir, ART ou RRT de levantamento topográfico, e a cadeia dominial quando houver dúvida sobre a origem.

**Por que interfere:** área de matrícula, área de IPTU, área de anúncio e área medida em campo divergem com frequência. A divergência não é detalhe cartorial: ela altera potencial construtivo, preço por metro quadrado e o próprio objeto do negócio.

**Validação obrigatória:** matrícula atualizada, com prazo de emissão recente, lida integralmente, inclusive averbações. Advogado ou especialista registral para qualquer ônus, gravame, usufruto, penhora, indisponibilidade, inventário ou área remanescente.

**Sinais de alerta:** matrícula antiga ou não apresentada; divergência entre áreas; imóvel sem matrícula própria, em condomínio ou em parte ideal; georreferenciamento ausente onde é exigido; cadeia dominial interrompida; "documentação em regularização".

**Como registrar:** número da matrícula, cartório, data de emissão, e a averbação específica que sustenta cada afirmação.

**Resultado esperado:** a área juridicamente definida, e a lista das divergências encontradas.

### D3 · Condições físicas

**O que investigar:** topografia, formato, testada, orientação solar, drenagem natural, solo e subsolo, vegetação existente, edificações, benfeitorias, ocupações, cercas, servidões visíveis e passivos aparentes.

**Fontes:** levantamento topográfico planialtimétrico, imagem de satélite e ortofoto, modelo digital de elevação, sondagem, visita ao terreno.

**Por que interfere:** condição física determina custo de terraplenagem, solução de fundação, implantação possível e, em terreno acidentado, a diferença entre o potencial construtivo legal e o construível real.

**Validação obrigatória:** levantamento topográfico com responsável técnico. Sondagem para qualquer afirmação sobre solo, subsolo, nível de água ou capacidade de suporte. Visita ao terreno.

**Sinais de alerta:** declividade acentuada; indício de aterro, bota-fora, voçoroca ou erosão; nascente, mina, curso d'água ou área úmida; ocupação por terceiros, posse ou moradia; resíduo, entulho, tanque, posto de combustível vizinho ou histórico industrial, que levantam suspeita de contaminação; diferença entre o perímetro cercado e o perímetro da matrícula.

**Como a IA pode apoiar:** organizar o que foi observado, comparar versões de informação, listar o que falta. **Leitura de imagem de satélite feita por IA é sempre status I, origem IA.** Ela não mede declividade, não identifica curso d'água e não delimita vegetação.

**Resultado esperado:** o que existe no terreno, separado do que se supõe que exista.

### D4 · Regras urbanísticas

**O que investigar:** o que pode ser feito ali, segundo a legislação vigente do município.

**Documentos e fontes:** Plano Diretor do município e suas leis complementares posteriores, lei de uso e ocupação do solo, lei de parcelamento, código de obras, código de posturas, legislação estadual aplicável, e a certidão de uso do solo ou consulta prévia emitida pela prefeitura.

**Por que interfere:** é a dimensão que define o produto possível. Ela também é a que mais circula em versão secundária errada.

**Validação obrigatória:** consulta prévia ou certidão de uso do solo emitida pelo órgão municipal. **Nenhum parâmetro urbanístico entra como C sem a lei, o artigo e o anexo que o sustentam.** Vigência verificada no Diário Oficial do município.

**Sinais de alerta:** parâmetro obtido de portal de corretora, de compilador privado de legislação ou de material de marketing; termo que não existe na lei local, o que indica tradução de fonte secundária; zona em revisão ou plano diretor em processo de alteração; potencial construtivo que depende de instrumento oneroso não considerado no preço; imóvel em área de operação urbana consorciada, ZEIS, área de especial interesse ou tombamento.

**Como registrar:** lei, número, ano, artigo, inciso e anexo, para cada parâmetro. Data da consulta ao texto.

**Nota sobre potencial construtivo onerado:** em municípios que adotam outorga onerosa do direito de construir, o coeficiente básico não acompanha o terreno gratuitamente acima de um limite, e o potencial adicional é comprado do município. Isso desloca custo para dentro da viabilidade, e não para a fase de aprovação. Quando o município for Goiânia, use a skill `outorga-onerosa-goiania`.

**Resultado esperado:** o que pode ser feito, com a lei ao lado de cada afirmação, e o que ainda precisa ser confirmado na prefeitura.

### D5 · Ambiente

**O que investigar:** o que protege, restringe ou condiciona o uso da área.

**Fontes:** Cadastro Ambiental Rural, órgão ambiental municipal e estadual, plano de manejo de unidade de conservação quando incidente, mapeamento de recursos hídricos, e o Código Florestal, Lei 12.651/2012, para as áreas de preservação permanente e a reserva legal.

**Por que interfere:** restrição ambiental não reduz o projeto, ela redefine o objeto. E é a cadeia com prazo mais longo e menor previsibilidade.

**Validação obrigatória:** manifestação do órgão ambiental competente. Profissional habilitado para delimitar APP, caracterizar vegetação e identificar espécie protegida. **As faixas de APP variam conforme o tipo e a dimensão do corpo d'água, e são definidas no art. 4º da Lei 12.651/2012: consulte o dispositivo, não use faixa de memória.**

**Sinais de alerta:** curso d'água, nascente, lagoa, várzea ou área alagável no terreno ou na divisa; vegetação nativa em estágio médio ou avançado; incidência de bioma com legislação específica, como a Mata Atlântica; unidade de conservação ou zona de amortecimento; cavidade natural; sítio arqueológico ou bem tombado; passivo de contaminação.

**Como a IA pode apoiar:** listar quais consultas fazer e a qual órgão. **A IA não declara existência nem inexistência de restrição ambiental.** Essa afirmação, nos dois sentidos, é sempre P até haver manifestação do órgão.

**Resultado esperado:** as restrições identificadas, as consultas em aberto, e o prazo estimado de cada cadeia de licenciamento.

### D6 · Infraestrutura e acessibilidade

**O que investigar:** se o terreno é atendido e se é alcançável.

**Bloco de infraestrutura:** água, esgoto, energia, drenagem, iluminação, resíduos e telecomunicações. Existência da rede na testada, **e capacidade de atendimento para a demanda pretendida**, que são coisas diferentes.

**Bloco de acessos e mobilidade:** hierarquia viária da via de acesso, condição do pavimento, faixa de domínio, restrição de acesso, transporte coletivo, e o percurso real até os destinos que importam para o produto.

**Fontes:** concessionárias de água, esgoto e energia, órgão municipal de trânsito, órgão rodoviário estadual ou federal quando houver rodovia envolvida, e o órgão gestor do transporte coletivo.

**Por que interfere:** rede na testada não significa capacidade disponível. Viabilidade técnica de atendimento é documento emitido pela concessionária, e o custo de extensão ou reforço de rede pode inviabilizar um empreendimento que fecha em todas as outras dimensões.

**Validação obrigatória:** declaração ou viabilidade técnica de cada concessionária, para a demanda pretendida. Manifestação do órgão rodoviário para acesso em faixa de domínio.

**Sinais de alerta:** rede ausente ou distante; loteamento vizinho com fornecimento restrito; acesso apenas por via não oficial, servidão ou área de terceiro; testada em rodovia sem ponto de acesso autorizado; ausência de drenagem em área de cota baixa.

**Resultado esperado:** o que é atendido, o que precisa ser implantado, e por conta de quem.

### D7 · Território e escalas

**O que investigar:** como o terreno se conecta ao que está em volta. É aqui que as Escalas da Decisão são aplicadas de forma explícita. Ver seção 5.

**O que observar:** usos e atividades do entorno, morfologia e gabarito predominante, vazios e imóveis subutilizados, obras e licenças recentes, equipamentos públicos, comércio e serviços, barreiras físicas, vetores de crescimento da cidade, e transformações previstas em plano ou projeto público.

**Fontes:** dados públicos censitários, licenças e alvarás publicados pelo município, plano diretor e planos setoriais, e observação de campo.

**Por que interfere:** é a dimensão que distingue uma leitura de terreno de uma consulta de parâmetros. Um lote conforme em todas as regras pode estar no lugar errado da cidade para a hipótese em teste.

**Sinais de alerta:** transformação em curso não capturada pelo cadastro; barreira que separa o terreno do que parece próximo no mapa; equipamento previsto e não executado sendo tratado como existente; vizinhança com uso incompatível ou com passivo.

**Resultado esperado:** a posição do terreno na estrutura urbana, e a leitura do movimento do entorno.

### D8 · Mercado, riscos e encaminhamento

**O que investigar:** para quem a hipótese faz sentido, o que a ameaça, e qual o próximo passo.

**O que observar:** perfil de quem mora e trabalha na região, produto praticado no entorno, oferta concorrente, e a compatibilidade entre a hipótese e a demanda real.

**Por que interfere:** fecha a leitura ligando o que é possível ao que faz sentido.

**Validação obrigatória:** todo dado de mercado citado carrega instituição, metodologia, cobertura territorial e data. **Índice de preço de anúncio e indicador de lançamento medem coisas diferentes e não se somam.** Fonte setorial é fonte legítima e não é fonte neutra: nomeie a entidade, nunca escreva "dados do mercado".

**Sinais de alerta:** número de mercado sem fonte primária; dado regional apresentado como municipal; série recalibrada comparada com a anterior; preço de anúncio tratado como preço de transação.

**Resultado esperado:** a matriz de riscos, potenciais e pendências, e o estado de saída.

---

## 5. Escalas da Decisão

Aplicadas dentro de D7 e usadas como lente em D3 a D6. Cinco escalas fixas.

| Escala | Pergunta principal |
| --- | --- |
| **Lote** | Quais condições e restrições existem dentro da área? |
| **Rua e quadra** | Como acessos, vizinhança e forma urbana afetam o terreno? |
| **Bairro** | Que infraestrutura, serviços, usos e transformações existem no entorno? |
| **Cidade** | Qual é a posição do terreno na estrutura e na legislação urbana? |
| **Região** | Que vetores econômicos, ambientais e logísticos influenciam a decisão? |

---

## 6. Modo gleba

**Gleba não é escala, é condição do imóvel:** o não parcelado. Não é uma distância, é um estado jurídico e morfológico.

Acione o modo gleba quando o imóvel não for lote urbano consolidado. Ele acrescenta, em D4 e D7:

- parcelamento do solo e o rito de aprovação aplicável, incluindo a Lei 6.766/1979 e a legislação municipal e estadual correspondente;
- diretrizes viárias e conexão com a malha existente;
- doação de áreas públicas e institucionais;
- faseamento;
- infraestrutura a implantar;
- **custo de urbanização como condicionante da viabilidade**, e não como item de orçamento posterior.

Esse último ponto é o que mais frequentemente falta: em gleba, a urbanização não é despesa de obra, é premissa de viabilidade. Uma gleba com parâmetros excelentes e custo de urbanização não dimensionado não tem leitura concluída.

---

## 7. Estados de saída

A conclusão preliminar nunca é "viável" ou "inviável".

| Estado | Quando se aplica |
| --- | --- |
| **Prosseguir** | Dimensões críticas confirmadas, sem pendência crítica aberta. |
| **Prosseguir com condicionantes** | Base confirmada, pendências identificadas, encaminháveis e sem poder de inviabilizar. |
| **Aprofundar antes de decidir** | Há indício suficiente para justificar investimento em investigação, e insuficiente para decidir. |
| **Reformular a hipótese** | O terreno tem potencial, mas não para o produto ou uso pretendido. |
| **Suspender a análise** | Pendência crítica sem caminho de resolução, ou custo de investigação desproporcional à decisão. |

### Nível de confiança, por regra e não por sensação

- **Alta:** D2, D4 e D5 com C nos itens determinantes, nenhuma pendência crítica aberta.
- **Média:** dimensões críticas com C parcial, pendências identificadas e com responsável definido.
- **Baixa:** alguma dimensão crítica sem nenhum C, ou pendência crítica sem responsável.

> **Regra dura: confiança baixa não autoriza o estado "prosseguir".** Nem com ressalva no texto.

### Toda conclusão declara

Nível de confiança · evidências utilizadas · inferências realizadas · pendências · condicionantes · riscos · próximos passos · responsáveis recomendados · fontes ainda a consultar.

**Reconhecer que um terreno precisa ser reformulado, aprofundado ou suspenso também é produzir valor.** Uma análise preliminar não deve fingir que elimina incertezas. Ela deve revelar o que sabemos, o que ainda não sabemos e o que precisa ser validado.

---

## 8. Dimensões críticas

**D2, D4 e D5.**

Sem nenhum C nelas, a leitura não sustenta estado de saída além de "aprofundar antes de decidir" ou "suspender a análise". É regra, não julgamento, e não é flexibilizada por pressão de prazo.

Se o usuário insistir em uma conclusão mais favorável sem que a evidência mude, registre o pedido, mantenha o estado e explique qual documento específico mudaria o resultado.

---

## 9. O que esta skill não faz

Não produz estudo conclusivo de viabilidade, laudo técnico, parecer jurídico, análise registral, estudo ambiental, avaliação imobiliária, projeto, consulta municipal, certidão, autorização ou recomendação de investimento.

Não substitui legislação vigente, certidões, levantamento de campo, visita técnica, consulta a órgãos, especialista nem responsabilidade técnica.

**Declaração obrigatória em toda saída extensa:**

> Este material oferece uma estrutura para investigação e registro. Não substitui consulta à legislação vigente, levantamento de campo, certidões, pareceres especializados ou responsabilidade técnica.

---

## 10. Skills relacionadas

| Skill | Quando usar |
| --- | --- |
| `protocolo-cip` | para classificar evidência, montar a matriz e tratar pendências |
| `outorga-onerosa-goiania` | quando o município for Goiânia e houver potencial construtivo acima do coeficiente básico |

---

<sub>Do Lote à Cidade, método do projeto Contexto Primeiro, por Thaynara Peixoto Guimarães.</sub>
