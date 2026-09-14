---
id: cardionet-instalacao
categoria: CardioNet
produtos: [CardioNet Client, CardioNet Server]
titulo: "Como instalar o CardioNet (Client/Server) e principais erros de instalação"
volume_suri: "208 casos em 3 meses — 2º maior tema depois do cartão do Holter"
fontes: ["Anexo_SW CardioNET-CNC (ficha técnica)", "Anexo_SW CardioNET-CNS (ficha técnica)", "Folheto CardioNet"]
video: "https://www.youtube.com/watch?v=Onu59nKFLc4"
status: "⚠️ rascunho — triagem completa, mas passo a passo técnico do instalador ainda depende do Filipe"
---

## O que é o CardioNet (contexto para quem for responder)

O CardioNet é o software de transmissão de exames de Holter e MAPA via Internet, dispensando a troca física de cartão de memória entre quem grava o exame e quem analisa (central de análise). Ele transmite exames gravados nos aparelhos CardioLight, CardioLoop, CardioSeven, CardioMapa, Dyna-MAPA AOP, Dyna-MAPA NG, ARTERIS AOP e Dynamis ECG. Existem duas pontas do software:

- **CardioNet Client** — instalado no local que grava e envia o exame (consultório, clínica, hospital).
- **CardioNet Server** — instalado na central de análise, que recebe os exames enviados.

Ambos dependem também do **Portal CardioNet** (área web) para consulta de relatórios e estatísticas de transmissão. Existem ainda duas variantes que **não** seguem este mesmo passo a passo e merecem ser identificadas logo no início do atendimento, para não gerar diagnóstico errado:

- **CardioNet Mobile** — acesso a laudos por celular/tablet, não faz a transmissão do exame em si.
- **CardioNet DICOM** — integração com sistemas PACS de clínicas/hospitais (exporta o exame em formato DICOM); é um fluxo de integração de TI, não uma instalação padrão de posto de coleta.

## Resposta rápida (bot / primeira mensagem) — versão preliminar

1. Confirmar qual dos dois o cliente está instalando: **Client** (quem grava/envia) ou **Server** (quem recebe/analisa) — os instaladores e o fluxo de configuração inicial são diferentes. Se o cliente mencionar PACS/DICOM ou app de celular, é um fluxo diferente (ver acima) — não tentar resolver como instalação padrão.
2. Confirmar que o computador tem acesso à Internet liberado para o software (portas/URLs do CardioNet não devem estar bloqueadas por firewall/antivírus corporativo). CardioNet não exige IP fixo — se o cliente estiver tentando configurar IP fixo por conta própria, isso não é um requisito do software.
3. Confirmar que o cliente tem as credenciais do Portal CardioNet em mãos — são as mesmas usadas para a conta do serviço de saúde no portal.

## Quando escalar para atendimento humano

- Qualquer erro de instalação que não seja "sem internet", "sem credencial" ou "produto errado (Mobile/DICOM confundido com instalação padrão)" — nível 1 não deve tentar diagnosticar erros de instalador sem checklist validado.
- Qualquer menção a integração DICOM/PACS — encaminhar direto para o time técnico, é fora do escopo de instalação padrão.
- Se não resolver por chat/bot: SSC (Serviço de Suporte ao Cliente) 11 3883-3010, ou Geral/WhatsApp 11 3883-3000.

## ⚠️ Pontos que ainda precisam de confirmação técnica com o Filipe antes de publicar

- Passo a passo exato do instalador atual (tela a tela) — os anexos técnicos disponíveis são fichas comerciais, não um guia de instalação passo a passo.
- Requisitos de sistema operacional/hardware atualizados (o que está documentado é antigo).
- Lista de URLs/portas que precisam estar liberadas no firewall, para orientar o TI do cliente.

Não incluímos números ou passos específicos para esses três pontos porque não há fonte confiável disponível ainda — preferimos deixar em aberto a arriscar uma instrução técnica incorreta.

## Fonte / observações

Baseado nas fichas técnicas comerciais do CardioNet Client/Server e no Folheto CardioNet (que também é a fonte dos telefones de contato). **Este artigo precisa de uma passada com o Filipe** para o passo a passo do instalador virar um guia completo — hoje cobre bem a triagem (o quê, qual variante, quando escalar), mas não o "como instalar tela a tela".
