#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LGPD PII Scanner Toolkit - Motor de Identificação e Validação de Dados Sensíveis
Python 3 stdlib puro - Validação matemática de CPF (Mod 11) e Mascaramento
"""

import sys
import re
from typing import List, Dict, Any, Tuple

class LGPDScannerEngine:
    @staticmethod
    def validar_cpf(cpf: str) -> bool:
        """Valida matematicamente se um CPF é real segundo o algoritmo de Módulo 11."""
        numeros = [int(c) for c in cpf if c.isdigit()]
        if len(numeros) != 11:
            return False
        # Rejeita CPFs com todos os dígitos iguais (ex: 111.111.111-11)
        if len(set(numeros)) == 1:
            return False
            
        # 1º dígito verificador
        soma = sum(numeros[i] * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        d1 = 0 if resto == 10 else resto
        if d1 != numeros[9]:
            return False
            
        # 2º dígito verificador
        soma = sum(numeros[i] * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        d2 = 0 if resto == 10 else resto
        return d2 == numeros[10]

    @staticmethod
    def mascarar_cpf(cpf: str) -> str:
        """Mascara o CPF para exibição segura em relatórios (***.***.123-**)."""
        digitos = "".join([c for c in cpf if c.isdigit()])
        if len(digitos) == 11:
            return f"***.***.{digitos[6:9]}-**"
        return "***"

    @classmethod
    def escanear_texto(cls, texto: str) -> List[Dict[str, Any]]:
        """Varre um texto em busca de CPFs e classifica se são válidos."""
        padrao_cpf = r"\b\d{3}\.?\d{3}\.?\d{3}-?\d{2}\b"
        candidatos = re.findall(padrao_cpf, texto)
        achados = []
        
        for cand in candidatos:
            valido = cls.validar_cpf(cand)
            achados.append({
                "original_mascarado": cls.mascarar_cpf(cand),
                "tipo": "CPF",
                "valido_mod11": valido,
                "artigo_lgpd": "Art. 5º, II (Dado Pessoal)",
                "severidade": "ALTA" if valido else "FALSO_POSITIVO"
            })
            
        return achados

def main():
    print("=" * 65)
    print("⚖️  TECHDIM LGPD PII SCANNER - AUDITORIA DEMO")
    print("=" * 65)
    
    texto_amostra = """
    Relatório de colaboradores:
    João Silva, CPF: 529.982.247-25 (Valido).
    Dado inválido de teste: 111.111.111-11 (Invalido).
    Contrato assinado em São Paulo.
    """
    
    resultados = LGPDScannerEngine.escanear_texto(texto_amostra)
    for r in resultados:
        icone = "🚨" if r["valido_mod11"] else "⚪"
        print(f"{icone} Tipo: {r['tipo']:<5} | Dado: {r['original_mascarado']:<15} | Status: {r['severidade']:<15} | Base: {r['artigo_lgpd']}")
        
    print("-" * 65)
    print("✓ Varredura LGPD executada com sucesso. Dados mascarados preservados.")

if __name__ == "__main__":
    main()
