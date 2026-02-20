## Vamos nos conectar:
[Linkedin](https://www.linkedin.com/in/jeduardosleite/)
---

![image](imagem/title.png)


# Objetivo
  O objetivo dessa atividade é simular um cenário real de limpeza de dados, fazendo uma análise completa das variáveis e, posteriormente, importar para o Power BI.

---

# Problemas encontrados
  Encontrei alguns problemas durante a análise dos dados. Problemas na formatação da data e categoria dos produtos, valores nulos, tipos de dados incorretos e inconsistência no valor unitário.

---

# Solucionando os problemas
  Sempre pensando no plano de negócio, o meu raciocínio seguiu a premissa de não excluir quaisquer dados sem antes verificar detalhadamente cada informação.

- ## Valores nulos
  Duas colunas detinham valores nulos, uma quantitativa e outra qualitativa. O tratamento foi realizando seguindo a premissa de análise da importância da variável, causa e solução da falta do dado.
Para a ```qualitativa```, optei por acrescentar uma nova categoria, desta maneira as informações permaneceriam no banco de dados. 
Para a ```qualitativa```, usei a fórmula matemática de ```total / quantidade```, desta maneira o valor unitário seria fidedigno.
```python
df['valor_unitario'] = df['valor_unitario'].fillna(df['valor_total'] / df['quantidade'])
```
---

- ## String desformatadas
  Neste caso, usei as funções específicas do python para trabalhar com **strings**, sendo a função ```title``` utilizada para deixar a primeira letra maiúscula, mantendo o padrão do banco de dados.

---


- ## Alterando o tipo de dados
  Aqui tive alguns problemas que surgiram durante o processo.
  1) as colunas ```data_venda``` e ```valor_unitario``` estavam com erros nas strings. Para corrigir as datas, usei a função:
    ```python
    def corrigir_data(data_str): # Cria uma função
    try:                                                    # Tenta converter a string usando o formato padrão
        return datetime.strptime(data_str, "%Y-%m-%d")      # Se funcionar, retorna a data convertida
    except:                                                 # Se der erro, entra nesse bloco
        try:                                                # Bloco da correção automática
            dia, mes, ano = map(int, data_str.split("/"))   # Divide a string pelo /, converte cada parte para inteiro e atribuí às variáveis dia, mes, ano.
            ultimo_dia = calendar.monthrange(ano, mes)[1]   # Descobri o último dia do mês
            return datetime(ano, mes, ultimo_dia)           # Cria uma nova data corrigida
        except:                                             # Se TUDO falhar
            return pd.NaT                                   # Retorna valor ausente
    ```

   2) Para o valor_unitario, usei o mesmo método utilizado no tratamento do valor nulo, desta vez apliquei em todas as linhas. Poderia ter voltado no processo e aplicado essa lógica no tratamento dos dados nulos, porém, resolvi deixar essa anotação e seguir com a mesma linha de raciocínio que usei.

---

## Exportando o arquivo
Por fim, exportei o arquivo em ```xlsx```, para trabalhar no Power BI. A princípio, exportei em ```csv```, porém tive problemas com a formatação no Power BI.

---

# Ferramentas
```python
import pandas as pd
import calendar
import openpyxl
from datetime import datetime
```

---

# Aprendizado
Durante essa atividade, agreguei mais conhecimento sobre a lógica de limpeza dos dados, pratiquei funções (```iloc, fillna, def, etc...```) e resolvi problemas inéditos para mim, como o tratamento de strings.
