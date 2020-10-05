#first_metatrader_program

import MetaTrader5 as mt5

mt5.initialize()

SymbolsTotal = mt5.symbols_total()

if SymbolsTotal > 0 :
    print("Total de simbolos: ", SymbolsTotal)

else:
    print("Símbolos não encontrados")

mt5.shutdown()