---
id: ecg-instalacao-preparacao
categoria: ECG
produtos: [CardioSeven, Dynamis]
titulo: "Como preparar o paciente e instalar corretamente o CardioSeven ou o Dynamis"
volume_suri: "92 casos em 3 meses"
fontes: ["Manual do Usuário CardioSeven VER003-DEZ2024", "Manual do Usuário Dynamis ECG VER003-FEV2025"]
status: pronto para revisão
---

## O que é cada produto (contexto para quem for responder)

Os dois equipamentos da categoria ECG são bem diferentes entre si — confirme qual o cliente está usando antes de orientar:

- **CardioSeven** — gravador ambulatorial (tipo Holter) de até 7 dias, com cartão SD, que o paciente carrega consigo.
- **Dynamis** — eletrocardiógrafo de repouso, conectado ao computador do cliente por **cabo USB**, sem cartão de memória.

## Resposta rápida (bot / primeira mensagem) — CardioSeven

A instalação segue os mesmos princípios do Holter comum, em 9 passos: preparar o cartão SD no CardioSmart, encaixar o cartão (respeitando a orientação — nunca invertido), preparar a pele do paciente, colocar os eletrodos, fixar os fios, conectar o cabo de paciente, inserir a pilha (polo negativo primeiro), e então a gravação começa (pelo botão multifuncional ou automaticamente após 5 minutos).

Preparação da pele (a etapa que mais gera dúvida):
1. **Depilação** da área — necessária mesmo com pouco pelo.
2. **Limpeza da pele** com gaze e álcool etílico 70%, para remover a gordura superficial que isola o sinal.
3. **Escarificação leve** com lixa d'água nº 400, no máximo 3 vezes no mesmo local, para melhorar a condutividade.

Os eletrodos devem ficar sobre superfícies ósseas — nunca em espaços intercostais ou dobras de pele.

## Resposta rápida (bot / primeira mensagem) — Dynamis

O Dynamis não usa cartão de memória — ele transmite o exame ao vivo para o computador via cabo USB, então a maior parte dos problemas é de conexão, não de gravação:

- **Requisitos mínimos do computador**: Windows 10 (a partir da versão 21H1) ou Windows 11, processador dual core ou superior, 4 GB de RAM, 500 GB de disco, porta USB 2.0 ou superior.
- **"O ECG não liga" ou "o software não reconhece o equipamento"**: verificar se o cabo USB está bem encaixado nas duas pontas (computador e aparelho) e se não está danificado; testar outra porta USB do computador.
- **Mensagens como "não foi possível encontrar a porta de comunicação" ou "não foi possível conectar o eletrocardiógrafo"**: fechar o aplicativo, reconectar o cabo USB, e abrir o aplicativo novamente.
- Os eletrodos (fornecidos pelo próprio cliente, não pela Cardios) seguem um código de cores por posição — perna direita (preto), braço direito (vermelho), e os demais nas posições torácicas indicadas nas etiquetas do próprio cabo.

## Quando escalar para atendimento humano

- CardioSeven: erro persistente mesmo com cartão original, pele bem preparada e cabo/pilha corretos.
- Dynamis: mensagem de erro de conexão que persiste mesmo depois de reconectar o cabo USB e reabrir o aplicativo — o próprio manual já orienta acionar a assistência técnica nesse ponto.
- Qualquer suspeita de defeito de hardware (cabo, gravador ou eletrocardiógrafo).

## Fonte / observações

Passo a passo de preparação de pele e instalação extraído da seção "4. Instalação e Operação do Gravador" do Manual do Usuário CardioSeven. Requisitos de sistema e tabela de resolução de problemas do Dynamis extraídos das seções "5.2. Requisitos do Sistema" e "8.3. Resolução de problemas" do Manual do Usuário Dynamis ECG. Código de cores dos eletrodos extraído da seção "7.1. Preparação do paciente" do mesmo manual.
