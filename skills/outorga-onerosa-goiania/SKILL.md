---
name: outorga-onerosa-goiania
description: >-
  Estima a contrapartida de outorga onerosa do direito de construir em Goiania
  e explica como o potencial construtivo adicional e adquirido do municipio.
  Use quando o usuario analisa terreno em Goiania e pretende area construida
  acima do coeficiente basico nao oneroso, quando precisa dimensionar o custo
  do potencial adicional dentro da viabilidade, ou quando encontra referencias
  a solo criado, OODC, coeficiente de aproveitamento ou outorga em Goiania.
  Tambem use para distinguir outorga onerosa do direito de construir de
  outorga onerosa de alteracao de uso, que sao instrumentos diferentes e
  frequentemente confundidos.
---

# Outorga onerosa do direito de construir em Goiânia

Skill municipal do método **Do Lote à Cidade**. Aplicada dentro de D4, regras urbanísticas.

---

## 1. O que muda a conta

Em Goiânia, o Plano Diretor vigente, Lei Complementar 349/2022, fixa um **coeficiente básico não oneroso** e trata o que passa dele como potencial adquirido do município, por meio da outorga onerosa do direito de construir.

A consequência prática é a que costuma faltar na conta de viabilidade:

> **O direito de construir acima do coeficiente básico não vem junto com o terreno. Ele é comprado.**

Isso desloca um custo relevante para dentro da decisão de compra, e não para a fase de aprovação. Um terreno avaliado pelo potencial máximo teórico, sem a contrapartida embutida, está avaliado errado.

### O termo que não existe

**"Coeficiente de aproveitamento máximo" não é um termo da LC 349/2022.** A lei trabalha com coeficiente básico não oneroso e com potencial adquirido por outorga.

Quando o usuário trouxer um "CA máximo" para Goiânia, isso indica fonte secundária que traduziu a lei para um vocabulário que ela não usa. Trate o valor como **P** e peça a origem.

### Os dois instrumentos que se confundem

| Instrumento | O que onera |
| --- | --- |
| Outorga onerosa do **direito de construir**, OODC | área construída acima do coeficiente básico |
| Outorga onerosa de **alteração de uso**, OOAU | a mudança de classificação da área, tipicamente a incorporação à macrozona urbana |

São fatos geradores diferentes, com bases de cálculo diferentes. Valores de arrecadação divulgados para um **não** são do outro, e essa troca já circula em material público sobre Goiânia. Ao encontrar um valor de arrecadação atribuído à OODC, verifique se não é da OOAU.

---

## 2. A fórmula

Conforme a Lei Complementar 373/2024, art. 4:

```
VOO = Vm × Vi × Qsc
```

| Termo | O que é | De onde vem |
| --- | --- | --- |
| **VOO** | valor da contrapartida | resultado |
| **Vm** | valor do metro quadrado | percentual do CUB R-16, variável por grupo |
| **Vi** | índice da área de aplicação | fixado por área no Plano Diretor |
| **Qsc** | quantidade de solo criado | área construída adicional pretendida, em m² |

### Estado de verificação destes parâmetros

> **Aviso.** Os índices por área e os percentuais do CUB usados por esta skill foram lidos em **compilador privado de legislação**, e não no Diário Oficial do Município. Eles entram como status **I**, origem `técnica secundária`.

**Nenhuma saída desta skill pode ser apresentada como confirmada enquanto essa verificação não for feita.** Isso não é excesso de cautela: parâmetro de outorga entra direto no preço máximo pagável por um terreno, e um índice errado propaga para a decisão inteira.

O que falta, de forma concreta:

1. Localizar a LC 373/2024 publicada no Diário Oficial do Município de Goiânia.
2. Conferir cada índice Vi por área de aplicação.
3. Conferir o enquadramento de cada grupo no percentual do CUB.
4. Verificar se houve alteração posterior à LC 373/2024.

---

## 3. Como conduzir

1. **Confirme o município.** Esta skill vale para Goiânia. Nenhum índice daqui é transferível para outro município.
2. **Estabeleça o coeficiente básico do lote.** Isso exige a certidão de uso do solo emitida pela prefeitura. Sem ela, o Qsc é uma hipótese, e o resultado é **P**, não **I**.
3. **Identifique a área de aplicação** em que o lote se encontra, no Plano Diretor.
4. **Obtenha o CUB R-16 do mês de referência**, publicado pelo Sinduscon-GO. O CUB é mensal, e a estimativa envelhece com ele.
5. **Confirme o percentual do CUB** aplicável ao grupo do empreendimento. A skill não deduz o enquadramento, porque deduzir enquadramento tributário é exatamente o tipo de inferência que o Protocolo C/I/P existe para impedir.
6. **Rode a estimativa** e apresente sempre com a matriz de procedência, nunca como número solto.

### O script

```bash
python3 scripts/outorga_goiania.py \
  --qsc 2500 \
  --area adensavel \
  --cub 2350.00 --cub-data 06/2026 \
  --percentual-cub 50
```

Áreas aceitas: `adensavel`, `adensamento-basico`, `desaceleracao`, `ocupacao-sustentavel`, `patrimonio`. Use `--vi` para informar o índice diretamente, quando você já o confirmou na lei. Use `--json` para saída estruturada.

O script devolve o valor **com o status e a origem de cada insumo**, a lista de pendências e os alertas. Ele foi escrito para não permitir que a contrapartida saia dele como um número limpo, porque um número limpo é lido como confirmado.

---

## 4. Como apresentar o resultado

Sempre com estas três informações juntas, e nesta ordem:

1. o valor estimado;
2. o status **I** e o motivo;
3. o que precisa ser confirmado para que ele vire **C**.

**Nunca** apresente a contrapartida estimada em proposta comercial, carta de intenção ou laudo. A estimativa serve para dimensionar ordem de grandeza e decidir se vale a pena investigar. O valor exigível é o que o município emite.

### Frase padrão de saída

> Contrapartida estimada de R$ [valor], status I, origem própria sobre índices de origem secundária. O valor depende de três confirmações ainda em aberto: os índices no Diário Oficial, o CUB do mês de referência e o coeficiente básico do lote na certidão de uso do solo. Não use este número em proposta.

---

## 5. Sinais de alerta

- Terreno precificado pelo potencial máximo, sem a contrapartida embutida na conta.
- Vendedor ou anúncio informando potencial construtivo sem a certidão de uso do solo. Origem `terceiro`, status máximo **I**.
- Uso de "CA máximo" para Goiânia, o que indica fonte secundária.
- Valor de arrecadação de outorga citado sem distinguir OODC de OOAU.
- Índice de outorga obtido de portal de corretora ou de compilador privado, tratado como confirmado.
- Estimativa feita com CUB de meses ou anos anteriores.

---

## 6. Fontes

| Fonte | Situação |
| --- | --- |
| LC 349/2022, Plano Diretor de Goiânia | texto oficial disponível no Sistema de Legislação da Prefeitura |
| LC 373/2024, fórmula e índices da outorga | `[FONTE NECESSÁRIA]` obter o texto oficial no Diário Oficial do Município |
| CUB R-16 | publicação mensal do Sinduscon-GO, informada pelo usuário |
| Certidão de uso do solo | emitida pela Secretaria Municipal de Planejamento, por lote |

Para o catálogo de bases públicas de Goiânia, com a ficha de metadados de cada fonte, ver o repositório `dados-abertos-goiania` do projeto Contexto Primeiro.

---

<sub>Do Lote à Cidade, método do projeto Contexto Primeiro, por Thaynara Peixoto Guimarães.</sub>
