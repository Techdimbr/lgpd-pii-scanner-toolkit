#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes unitários para o motor do LGPD PII Scanner Toolkit.
"""

import unittest
import sys
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

from lgpd_scanner import LGPDScannerEngine

class TestLGPDScannerEngine(unittest.TestCase):
    def test_cpf_valido_e_invalido(self):
        # CPF matematicamente válido conhecido para testes: 52998224725
        self.assertTrue(LGPDScannerEngine.validar_cpf("529.982.247-25"))
        # CPF repetido falso
        self.assertFalse(LGPDScannerEngine.validar_cpf("111.111.111-11"))
        # CPF com dígito errado
        self.assertFalse(LGPDScannerEngine.validar_cpf("529.982.247-00"))

    def test_mascaramento_cpf(self):
        mascarado = LGPDScannerEngine.mascarar_cpf("529.982.247-25")
        self.assertEqual(mascarado, "***.***.247-**")

    def test_escanear_texto(self):
        texto = "Cliente A CPF 529.982.247-25 e outro 000.000.000-00."
        achados = LGPDScannerEngine.escanear_texto(texto)
        self.assertEqual(len(achados), 2)
        self.assertTrue(achados[0]["valido_mod11"])
        self.assertFalse(achados[1]["valido_mod11"])

if __name__ == "__main__":
    unittest.main()
