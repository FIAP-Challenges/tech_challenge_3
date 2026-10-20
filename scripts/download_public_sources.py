"""Baixa arquivos públicos oficiais e registra sua integridade.

As URLs variáveis devem ser fornecidas explicitamente. Isso evita que uma
atualização silenciosa do portal substitua a edição usada no trabalho.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCES = {
    "censo_escolar_2023": {
        "url": "https://download.inep.gov.br/dados_abertos/microdados_censo_escolar_2023.zip",
        "destination": "dados/complementar/microdados_ed_basica_2023.zip",
    },
    "pib_municipios_2022": {
        "url": "https://ftp.ibge.gov.br/Pib_Municipios/2022_2023/xlsx/tabelas_completas_2022.xlsx",
        "destination": "dados/origem_publica/pib/tabelas_completas_2022.xlsx",
    },
    "pib_municipios_2023": {
        "url": "https://ftp.ibge.gov.br/Pib_Municipios/2022_2023/xlsx/tabelas_completas_2023.xlsx",
        "destination": "dados/origem_publica/pib/tabelas_completas_2023.xlsx",
    },
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def download(url: str, destination: Path, overwrite: bool) -> dict:
    if destination.exists() and not overwrite:
        status = "existing"
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_name(destination.name + ".part")
        request = Request(url, headers={"User-Agent": "TC3-academic-reproducibility/1.0"})
        with urlopen(request, timeout=120) as response, temporary.open("wb") as output:
            while block := response.read(1024 * 1024):
                output.write(block)
        temporary.replace(destination)
        status = "downloaded"
    return {
        "url": url,
        "local_path": destination.relative_to(ROOT).as_posix(),
        "bytes": destination.stat().st_size,
        "sha256": sha256(destination),
        "status": status,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Baixa fontes públicas oficiais do TC3.")
    parser.add_argument("--list", action="store_true", help="Lista as fontes automatizadas.")
    parser.add_argument("--source", action="append", choices=sorted(DEFAULT_SOURCES))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if args.list:
        print(json.dumps(DEFAULT_SOURCES, ensure_ascii=False, indent=2))
        return 0
    if not args.source:
        parser.error("Informe --source ou use --list.")

    try:
        records = []
        for name in args.source:
            spec = DEFAULT_SOURCES[name]
            record = download(spec["url"], ROOT / spec["destination"], args.overwrite)
            record["source"] = name
            records.append(record)
            print(f"{record['status']}: {name} -> {record['local_path']}")
        manifest = {
            "generated_at_utc": datetime.now(timezone.utc).isoformat(),
            "downloads": records,
        }
        path = ROOT / "dados" / "origem_publica" / "manifesto_download_publico.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Manifesto: {path}")
        return 0
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
