# Como contribuir

Contribuições são bem-vindas quando aumentam a clareza, a rastreabilidade ou a utilidade pública do método.

## As contribuições mais úteis

1. **Preencher um `[FONTE NECESSÁRIA]`.** Vários pontos das skills apontam para uma fonte que ainda não foi confirmada na publicação oficial. Cada um deles é um pedido de ajuda explícito.
2. **Corrigir uma afirmação sobre legislação.** Se uma skill descreve um procedimento, um documento ou um instrumento de forma imprecisa, isso é o erro mais grave possível aqui.
3. **Trazer a prática do seu município.** O método é nacional, a legislação é local. Relatar como funciona a certidão de uso do solo, o rito de parcelamento ou o licenciamento ambiental na sua cidade ajuda a manter o método honesto sobre o que varia.
4. **Apontar um sinal de alerta que faltou.** As listas de sinais de alerta vêm de prática. Elas são incompletas por natureza.

## Padrão de fonte

Toda inclusão que sustente afirmação técnica precisa trazer:

nome, instituição, link oficial, data de consulta, cobertura, escala quando aplicável, e limitação principal.

Três regras que costumam ser esquecidas:

- **Legislação se cita pela publicação oficial**, não por compilador privado nem por portal de notícia. Compilador serve para localizar, não para citar.
- **Parâmetro urbanístico nunca é universal.** Ele pertence a um município, a uma lei, a um artigo e a um anexo.
- **Cobertura é o recorte real da fonte**, não o recorte desejado.

## Não envie

- dados pessoais, documentos de clientes ou casos sigilosos;
- caso real identificável, ainda que você o considere anonimizado;
- número sem data e sem origem;
- parâmetro apresentado como universal;
- recomendação de compra ou investimento;
- conteúdo copiado de material protegido;
- alteração que enfraqueça as regras do Protocolo C/I/P.

Esta última merece explicação. Propostas que tornem o protocolo mais permissivo, em especial as que permitiriam promover saída de IA a Confirmado, não serão aceitas. Essa restrição é o objeto do projeto, não um detalhe de implementação.

## Scripts

Python 3.8+, biblioteca padrão apenas. Um script que produza número em contexto de decisão precisa devolver a procedência junto, no mesmo formato dos demais. Número limpo é lido como confirmado, e é isso que o método existe para impedir.

## Discussões

Sugestões metodológicas devem explicar o problema que resolvem e a dimensão afetada. Para exposição indevida de dado sensível, não abra issue pública. Ver `SECURITY.md`.
