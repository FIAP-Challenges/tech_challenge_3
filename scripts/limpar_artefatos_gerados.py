"""Limpa artefatos regeneráveis do TC3 sem tocar nas fontes originais.

Uso seguro (apenas lista):
    python scripts/limpar_artefatos_gerados.py

Limpeza efetiva:
    python scripts/limpar_artefatos_gerados.py --executar
"""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FONTES_ORIGINAIS = (ROOT / "dados" / "fontes_originais").resolve()
ALVOS = (
    (ROOT / "dados" / "dados_processados").resolve(),
    (ROOT / "dados" / "dados_analiticos").resolve(),
    (ROOT / "resultados").resolve(),
    (ROOT / "modelos").resolve(),
    (ROOT / ".execucao_temporaria").resolve(),
)


def validar_estrutura() -> None:
    if not (ROOT / ".git").exists():
        raise RuntimeError(f"Raiz Git não encontrada em {ROOT}")
    if not (ROOT / "dados").is_dir():
        raise RuntimeError(f"Pasta de dados não encontrada em {ROOT}")
    for alvo in ALVOS:
        if ROOT not in alvo.parents:
            raise RuntimeError(f"Alvo fora do projeto: {alvo}")
        if alvo == FONTES_ORIGINAIS or FONTES_ORIGINAIS in alvo.parents:
            raise RuntimeError(f"A lista de limpeza alcançaria fontes originais: {alvo}")


def listar_conteudo(alvo: Path) -> list[Path]:
    """Lista apenas artefatos removíveis, preservando arquivos README.md."""
    if not alvo.exists():
        return []
    return sorted(
        (
            item for item in alvo.rglob("*")
            if (item.is_file() or item.is_symlink()) and item.name.lower() != "readme.md"
        ),
        key=lambda item: str(item).lower(),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--executar",
        action="store_true",
        help="remove o conteúdo dos diretórios regeneráveis; sem esta opção, apenas simula",
    )
    args = parser.parse_args()
    validar_estrutura()

    print(f"Raiz validada: {ROOT}")
    print(f"Fontes protegidas: {FONTES_ORIGINAIS}")
    print("Modo:", "LIMPEZA EFETIVA" if args.executar else "SIMULAÇÃO")

    encontrados = 0
    for alvo in ALVOS:
        itens = listar_conteudo(alvo)
        encontrados += len(itens)
        print(f"\n{alvo.relative_to(ROOT)}: {len(itens)} item(ns)")
        for item in itens:
            print(" -", item.relative_to(ROOT))
            if not args.executar:
                continue
            item.unlink()
        if args.executar:
            alvo.mkdir(parents=True, exist_ok=True)

    if not encontrados:
        print("\nNenhum artefato regenerável encontrado.")
    elif args.executar:
        print("\nLimpeza concluída. As pastas principais foram preservadas.")
    else:
        print("\nNada foi removido. Use --executar para confirmar a limpeza.")


if __name__ == "__main__":
    main()
