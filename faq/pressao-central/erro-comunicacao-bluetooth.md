---
id: pressao-central-erro-comunicacao
categoria: Pressão Central
produtos: [Arteris AOP]
titulo: "O Arteris AOP não conecta ou dá erro de comunicação (Bluetooth)"
volume_suri: "140 casos em 3 meses"
fontes: ["Manual do Usuário ARTERIS AOP VER003-FEV2025 (seção 8.1 'Erro de comunicação')"]
status: pronto para revisão
---

## Resposta rápida (bot / primeira mensagem)

O Arteris AOP se conecta ao aplicativo por **Bluetooth** (a interface por infravermelho do aparelho existe fisicamente, mas não é utilizada). Quando o monitor mostra um erro de comunicação, ele exibe um código (Cod 1 a Cod 8) que já indica a causa provável:

- **Cod 1** — Erro durante o pareamento, ou o equipamento remoto (celular/tablet) foi desligado. Orientação: refazer o pareamento e religar o equipamento remoto.
- **Cod 2** — Bluetooth desligado ou fora de alcance. Orientação: verificar se o Bluetooth do equipamento remoto está ligado e por perto.
- **Cod 3** — Falha ao enviar as medidas. Orientação: fazer uma nova medição e verificar se ela é enviada.
- **Cod 4** — Erro de comunicação (genérico). Orientação: repetir o teste; se persistir, é caso de suporte técnico.
- **Cod 5** — Dado inválido na memória. Orientação: repetir o teste; se persistir, é caso de suporte técnico.
- **Cod 6** — Erro no circuito de comunicação. Orientação: repetir o teste; se persistir, é caso de suporte técnico.
- **Cod 7** — Memória cheia. Orientação: repetir o teste; se persistir, é caso de suporte técnico.
- **Cod 8** — Outro erro não classificado. Orientação: repetir o teste; se persistir, é caso de suporte técnico.

## Passo a passo para orientar o cliente

1. Peça o código exato do erro mostrado no visor do monitor (Cod 1 a 8).
2. Para Cod 1 ou Cod 2: oriente refazer o pareamento Bluetooth com o equipamento remoto e confirmar que ele está ligado, com Bluetooth ativo e por perto do monitor.
3. Para Cod 3: peça para repetir a medição e conferir se ela é transmitida normalmente desta vez.
4. Para Cod 4 a Cod 8: se o erro se repetir mais de uma vez mesmo após reiniciar o processo, é caso de encaminhar para o suporte técnico — o próprio manual orienta isso para esses códigos.

## Quando escalar para atendimento humano

- Qualquer código (Cod 4 a 8) que se repita após o cliente tentar novamente.
- Cod 1/2/3 que persistam mesmo depois de reparear e confirmar Bluetooth ligado — pode ser o mesmo padrão de defeito de conectividade já registrado publicamente para este equipamento.
- Cliente com prazo urgente de laudo.

## Fonte / observações

Códigos de erro extraídos literalmente da seção 8.1 "Erro de comunicação" do Manual do Usuário ARTERIS AOP (VER003-FEV2025). A interface infravermelho do aparelho (seção 2.6 do manual) está presente no hardware mas não é utilizada — a conexão real é sempre via Bluetooth.
