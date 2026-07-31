#!/usr/bin/env python3
"""Estimativa da contrapartida de outorga onerosa do direito de construir em Goiania.

Formula: VOO = Vm * Vi * Qsc  (LC 373/2024, art. 4)

Este script nao devolve um numero solto. Toda saida carrega o status e a origem
de cada insumo, segundo o Protocolo C/I/P do projeto Contexto Primeiro:

    C = confirmado por fonte oficial citavel
    I = indicio ou inferencia
    P = pendente de verificacao

O resultado e sempre I, no maximo, porque depende de indices ainda nao
confirmados no Diario Oficial do Municipio. Uma estimativa com status I nao
autoriza decisao de compra nem entra em proposta comercial.

Sem dependencias externas. Python 3.8+.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, asdict, field
from typing import Dict, List, Optional

FORMULA = "VOO = Vm * Vi * Qsc"
LEI = "Lei Complementar Municipal 373/2024, art. 4"


def fmt(valor: float, casas: int = 2) -> str:
    """Formata numero no padrao brasileiro: milhar com ponto, decimal com virgula."""
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "@").replace(".", ",").replace("@", ".")


@dataclass
class Insumo:
    """Um valor de entrada, com procedencia obrigatoria."""

    nome: str
    valor: Optional[float]
    unidade: str
    status: str          # C, I ou P
    origem: str          # propria, oficial, tecnica secundaria, terceiro, IA
    fonte: str
    verificar: str = ""  # o que falta para promover a C

    def linha(self) -> str:
        if self.valor is None:
            valor = "PENDENTE"
        else:
            # indices adimensionais pedem mais casas que valores em reais
            casas = 4 if not self.unidade else 2
            valor = fmt(self.valor, casas).rstrip("0").rstrip(",") if casas == 4 else fmt(self.valor)
        rotulo = f"{valor} {self.unidade}".rstrip()
        return (
            f"  [{self.status}] {self.nome}: {rotulo}\n"
            f"      origem: {self.origem} | fonte: {self.fonte}"
        )


# ---------------------------------------------------------------------------
# Indices da lei.
#
# ATENCAO: os valores abaixo foram lidos em compilador privado de legislacao,
# nao no Diario Oficial do Municipio. Por isso entram como status I, origem
# tecnica secundaria. Confirmar antes de qualquer uso que sustente decisao.
# ---------------------------------------------------------------------------

INDICE_VI: Dict[str, float] = {
    "adensavel": 0.10,
    "adensamento-basico": 0.15,
    "desaceleracao": 0.20,
    "ocupacao-sustentavel": 0.30,
    "patrimonio": 0.30,
}

VI_STATUS = "I"
VI_ORIGEM = "tecnica secundaria"
VI_FONTE = f"{LEI}, lido em compilador privado"
VI_VERIFICAR = (
    "confirmar cada indice no texto publicado no Diario Oficial do Municipio de Goiania"
)

# Percentuais do CUB R-16 admitidos pela lei para composicao do Vm.
# O enquadramento de cada grupo no percentual correspondente NAO foi confirmado
# e por isso e informado pelo usuario, nunca deduzido pelo script.
PERCENTUAIS_CUB_ADMITIDOS = (50.0, 40.0, 30.0)


@dataclass
class Resultado:
    voo: Optional[float]
    status: str
    insumos: List[Insumo] = field(default_factory=list)
    alertas: List[str] = field(default_factory=list)
    pendencias: List[str] = field(default_factory=list)


def calcular(
    qsc: float,
    area: str,
    cub_r16: float,
    cub_data: str,
    percentual_cub: float,
    vi_manual: Optional[float] = None,
) -> Resultado:
    """Monta a estimativa e a procedencia de cada insumo."""

    alertas: List[str] = []
    pendencias: List[str] = []

    if vi_manual is not None:
        vi = vi_manual
        vi_insumo = Insumo(
            nome="Vi, indice da area",
            valor=vi,
            unidade="",
            status="P",
            origem="propria",
            fonte="informado manualmente pelo usuario",
            verificar="registrar a lei, o artigo e o anexo que fixam este indice",
        )
        pendencias.append(
            "O indice Vi foi informado manualmente. Registre a norma que o fixa antes de usar o resultado."
        )
    else:
        chave = area.strip().lower()
        if chave not in INDICE_VI:
            raise ValueError(
                f"area '{area}' desconhecida. Use uma de: {', '.join(sorted(INDICE_VI))}, "
                f"ou informe --vi diretamente."
            )
        vi = INDICE_VI[chave]
        vi_insumo = Insumo(
            nome=f"Vi, indice da area ({chave})",
            valor=vi,
            unidade="",
            status=VI_STATUS,
            origem=VI_ORIGEM,
            fonte=VI_FONTE,
            verificar=VI_VERIFICAR,
        )
        pendencias.append(VI_VERIFICAR)

    if percentual_cub not in PERCENTUAIS_CUB_ADMITIDOS:
        alertas.append(
            f"O percentual {percentual_cub}% nao esta entre os admitidos "
            f"({', '.join(f'{p:g}%' for p in PERCENTUAIS_CUB_ADMITIDOS)}). "
            "Confirme o enquadramento do grupo na lei."
        )

    vm = cub_r16 * (percentual_cub / 100.0)

    cub_insumo = Insumo(
        nome="CUB R-16",
        valor=cub_r16,
        unidade="R$/m2",
        status="P",
        origem="tecnica secundaria",
        fonte=f"informado pelo usuario, referencia {cub_data}",
        verificar="confirmar o valor e o mes na publicacao do Sinduscon-GO",
    )
    pendencias.append(
        f"Confirmar o CUB R-16 de {cub_data} na publicacao do Sinduscon-GO. "
        "O CUB e mensal, e uma estimativa envelhece com ele."
    )

    vm_insumo = Insumo(
        nome=f"Vm, {percentual_cub:g}% do CUB R-16",
        valor=vm,
        unidade="R$/m2",
        status="I",
        origem="propria",
        fonte="calculado sobre o CUB informado",
        verificar="depende da confirmacao do CUB e do enquadramento do grupo",
    )
    pendencias.append(
        "Confirmar na lei qual percentual do CUB se aplica ao grupo do empreendimento. "
        "O script nao deduz o enquadramento."
    )

    qsc_insumo = Insumo(
        nome="Qsc, area construida adicional",
        valor=qsc,
        unidade="m2",
        status="P",
        origem="propria",
        fonte="informado pelo usuario",
        verificar=(
            "so e confirmavel apos a definicao do potencial construtivo basico "
            "na certidao de uso do solo emitida pelo municipio"
        ),
    )
    pendencias.append(
        "O Qsc depende do potencial construtivo basico do lote, que exige certidao "
        "de uso do solo emitida pela prefeitura."
    )

    voo = vm * vi * qsc

    voo_insumo = Insumo(
        nome="VOO, contrapartida estimada",
        valor=voo,
        unidade="R$",
        status="I",
        origem="propria",
        fonte=f"{FORMULA}, conforme {LEI}",
        verificar="promover a C exige todos os insumos acima confirmados em fonte oficial",
    )

    alertas.append(
        "Esta e uma estimativa de ordem de grandeza. Ela nao substitui o calculo "
        "oficial emitido pelo municipio, que e o unico valor exigivel."
    )

    return Resultado(
        voo=voo,
        status="I",
        insumos=[qsc_insumo, cub_insumo, vm_insumo, vi_insumo, voo_insumo],
        alertas=alertas,
        pendencias=pendencias,
    )


def relatorio(r: Resultado) -> str:
    larg = 74
    linhas: List[str] = []
    linhas.append("=" * larg)
    linhas.append("OUTORGA ONEROSA DO DIREITO DE CONSTRUIR | GOIANIA")
    linhas.append(f"{FORMULA}   ({LEI})")
    linhas.append("=" * larg)
    linhas.append("")
    linhas.append("INSUMOS E PROCEDENCIA")
    linhas.append("")
    for ins in r.insumos:
        linhas.append(ins.linha())
        if ins.verificar:
            linhas.append(f"      falta: {ins.verificar}")
        linhas.append("")

    linhas.append("-" * larg)
    linhas.append(f"CONTRAPARTIDA ESTIMADA: R$ {fmt(r.voo)}")
    linhas.append(f"STATUS DA ESTIMATIVA: {r.status}  (indicio, nao confirmado)")
    linhas.append("-" * larg)
    linhas.append("")

    linhas.append("PENDENCIAS PARA PROMOVER A ESTIMATIVA A CONFIRMADA")
    for i, p in enumerate(r.pendencias, 1):
        linhas.append(f"  P-{i:02d}  {p}")
    linhas.append("")

    linhas.append("ALERTAS")
    for a in r.alertas:
        linhas.append(f"  !  {a}")
    linhas.append("")
    linhas.append("=" * larg)
    linhas.append(
        "Nenhum valor acima esta confirmado. Uma estimativa com status I nao\n"
        "autoriza decisao de compra e nao entra em proposta comercial sem que\n"
        "as pendencias acima estejam resolvidas e registradas."
    )
    linhas.append("=" * larg)
    return "\n".join(linhas)


def main(argv: Optional[List[str]] = None) -> int:
    p = argparse.ArgumentParser(
        description="Estimativa de outorga onerosa do direito de construir em Goiania, com procedencia C/I/P.",
        epilog="Do Lote a Cidade, projeto Contexto Primeiro.",
    )
    p.add_argument("--qsc", type=float, required=True,
                   help="area construida adicional pretendida, em m2")
    p.add_argument("--area", default="adensavel",
                   help="area de aplicacao: " + ", ".join(sorted(INDICE_VI)))
    p.add_argument("--vi", type=float, default=None,
                   help="informa o indice Vi diretamente, ignorando a tabela interna")
    p.add_argument("--cub", type=float, required=True,
                   help="CUB R-16 em R$/m2, obtido no Sinduscon-GO")
    p.add_argument("--cub-data", default="[FONTE NECESSARIA]",
                   help="mes e ano de referencia do CUB informado, ex: 06/2026")
    p.add_argument("--percentual-cub", type=float, required=True,
                   help="percentual do CUB aplicavel ao grupo: 50, 40 ou 30")
    p.add_argument("--json", action="store_true",
                   help="saida em JSON, com a procedencia de cada insumo")

    a = p.parse_args(argv)

    if a.qsc <= 0:
        print("erro: --qsc precisa ser maior que zero.", file=sys.stderr)
        return 2
    if a.cub <= 0:
        print("erro: --cub precisa ser maior que zero.", file=sys.stderr)
        return 2

    try:
        r = calcular(
            qsc=a.qsc,
            area=a.area,
            cub_r16=a.cub,
            cub_data=a.cub_data,
            percentual_cub=a.percentual_cub,
            vi_manual=a.vi,
        )
    except ValueError as e:
        print(f"erro: {e}", file=sys.stderr)
        return 2

    if a.json:
        saida = asdict(r)
        saida["formula"] = FORMULA
        saida["lei"] = LEI
        print(json.dumps(saida, ensure_ascii=False, indent=2))
    else:
        print(relatorio(r))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
