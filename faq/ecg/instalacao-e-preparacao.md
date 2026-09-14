---
id: ecg-instalacao-preparacao
categoria: ECG
produtos: [Dynamis]
titulo: "Como preparar o paciente e instalar corretamente o Dynamis (ECG de repouso)"
volume_suri: "92 casos em 3 meses"
fontes: ["Manual do Usuário Dynamis ECG VER003-FEV2025"]
status: pronto para revisão
---

## O que é o Dynamis (contexto para quem for responder)

O Dynamis é o eletrocardiógrafo de repouso da Cardios, conectado ao computador do cliente por **cabo USB** — diferente dos gravadores ambulatoriais (Holter) como CardioLight/CardioLoop/CardioSeven, que o paciente carrega consigo por dias. O Dynamis não usa cartão de memória: ele transmite o exame ao vivo para o computador durante a coleta, então a maior parte dos problemas relatados é de conexão/reconhecimento do equipamento, não de gravação.

## Resposta rápida (bot / primeira mensagem)

- **Requisitos mínimos do computador**: Windows 10 (a partir da versão 21H1) ou Windows 11, processador dual core ou superior, placa de vídeo compatível com DirectX 9/OpenGL (mínimo 256 MB), 4 GB de RAM, 500 GB de disco, resolução mínima 1280x1024 (desktop) ou 1336x768 (notebook), porta USB 2.0 ou superior. O Dynamis é alimentado só pelo cabo USB — não tem fonte de alimentação própria.
- **"O ECG não liga" ou "o software não reconhece o equipamento"**: verificar se o cabo USB está bem encaixado nas duas pontas (computador e aparelho) e se não está danificado; testar outra porta USB do computador.
- **Mensagens como "não foi possível encontrar a porta de comunicação" ou "não foi possível conectar o eletrocardiógrafo"**: fechar o aplicativo, reconectar o cabo USB, e abrir o aplicativo novamente.
- **Preparação do paciente**: deitado, monitor em ângulo de 90°, tórax/pulsos/braços livres de joias — a Cardios não fornece os eletrodos, são de responsabilidade do cliente.
- **Código de cores dos eletrodos** (12 derivações): preto = perna direita (ou parte inferior direita do abdômen); vermelho = braço direito; branco/vermelho = 4º espaço intercostal direito junto ao esterno; branco/amarelo = 4º espaço intercostal junto ao esterno; branco/verde = ponto médio entre C2 e C4; branco/marrom = espaço intercostal esquerdo.

## Passo a passo para orientar o cliente

1. Confirmar que o cabo USB está firme nas duas pontas e testar outra porta USB do computador caso o equipamento não ligue.
2. Se aparecer mensagem de erro de porta de comunicação ou de conexão com o eletrocardiógrafo: orientar fechar o aplicativo, reconectar o cabo USB e abrir o aplicativo de novo.
3. Confirmar que o computador atende aos requisitos mínimos (Windows 10 21H1+/11, 4 GB RAM, USB 2.0+) — softwares desatualizados ou hardware abaixo do requisito também podem causar falha de reconhecimento.
4. Para dúvida de posicionamento de eletrodos, usar o código de cores acima; reforçar que o paciente deve estar deitado, com o monitor a 90° e sem joias no tórax/pulsos/braços.

## Quando escalar para atendimento humano

- Mensagem de erro de conexão que persiste mesmo depois de reconectar o cabo USB e reabrir o aplicativo — o próprio manual já orienta acionar a assistência técnica nesse ponto.
- Suspeita de defeito de hardware (cabo ou eletrocardiógrafo).

## Fonte / observações

Requisitos de sistema e tabela de resolução de problemas extraídos das seções "5.2. Requisitos do Sistema" e "8.3. Resolução de problemas" do Manual do Usuário Dynamis ECG. Código de cores dos eletrodos extraído da seção "7.1. Preparação do paciente" do mesmo manual.

**Nota de categorização**: o CardioSeven, apesar do nome, é um gravador ambulatorial (Holter) de até 7 dias — como o CardioLight/CardioLoop, só que com duração maior — e não um eletrocardiógrafo de repouso. Por isso não é tratado neste artigo; sua instalação já é coberta no artigo de instalação de Holter (categoria Holter, junto com CardioLight/CardioLight+/CardioLoop).
