import pandas as pd
import glob
import matplotlib.pyplot as plt

# Coletar dados de vendedores e vendas
arquivos = glob.glob("*.xlsx")
df_geral = pd.concat([pd.read_excel(f) for f in arquivos], ignore_index=True)

# Filtrar quem bateu a meta
meta = 50000
top_vendedores = df_geral[df_geral['Vendas'] > meta].sort_values(by='Vendas', ascending=True)

# Exportar o Relatório 
top_vendedores.to_excel('relatorio_elite.xlsx', index=False)
print(f"Relatório Excel gerado com {len(top_vendedores)} vendedores.")

# visualização do gráfico
plt.figure(figsize=(8, 4))
plt.barh(top_vendedores['Vendedor'], top_vendedores['Vendas'], color='gold', height=0.4)

plt.axvline(meta, color='red', linestyle='--', label=f'Meta R$ {meta}')
plt.title('Vendedores Excelentes (Acima de R$ 50k)')
plt.xlabel('Valor Vendido (R$)')
plt.ylabel('Vendedor')
plt.legend()
plt.tight_layout()
plt.ylim(-1, 1)
# Salvar o gráfico como imagem
plt.savefig('grafico_vendas.png')
plt.show()
