# Réveillon Praia 2027 — Mapa 3D de mesas

Mapa 3D interativo do Praia Hall (Praia Clube) para a venda de mesas do Réveillon 2026/2027,
baseado no layout de Leo Bione (versão 5): 200 mesas de 4 lugares, 8 lounges centrais e
8 lounges de pufes — 880 lugares.

**Abrir o mapa:** https://lopesmizael2025.github.io/reveillon-praia-2027/

## Numeração

| Setor | Local | Números |
|---|---|---|
| A | Palco esquerda | 1–20 |
| B | Palco direita | 21–40 |
| C | Deck lateral | 41–92 |
| D | Salão esquerda | 93–136 |
| E | Salão central | 137–180 |
| F | Jardim entrada | 181–200 |
| Lounges centrais | junto ao bar | L1–L8 |
| Lounges pufes | backdrop e área externa | P1–P8 |

## Uso

- Clique numa mesa para marcar livre / reservada / vendida (o status fica salvo no navegador de quem usa).
- Busca por número, destaque por setor, vistas prontas e exportação de PNG e CSV.
- Imagens prontas em `saidas/`.

## Editar

`template.html` é a fonte; `python build.py` injeta `tables_min.json` e gera `index.html`.
`python serve.py` serve a pasta em http://127.0.0.1:8765 e grava PNGs enviados por POST em `saidas/`.
