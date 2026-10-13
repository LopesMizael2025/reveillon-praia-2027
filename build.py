# Gera reveillon2027_mapa3d.html a partir do template + tables_min.json
import pathlib
d = pathlib.Path(__file__).parent
html = (d / 'template.html').read_text(encoding='utf-8')
html = html.replace('/*TABLES*/', (d / 'tables_min.json').read_text().strip())
(d / 'index.html').write_text(html, encoding='utf-8')
print('ok')
