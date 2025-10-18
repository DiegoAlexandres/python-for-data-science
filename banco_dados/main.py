#%%
import pandas as pd
import psycopg
from db_postgresql import get_db_connection

#%%
def buscar_transacoes_do_banco():
    
    query_sql = "SELECT * FROM transactions;"

    try:
        with get_db_connection() as conn:
            
            df = pd.read_sql_query(query_sql, conn)
            
            print("✅ Dados da tabela 'transactions' carregados com sucesso!")
            return df

    except psycopg.Error as e:
        print(f"❌ Erro ao consultar o banco de dados: {e}")
        return None


#%%
df_transacoes = buscar_transacoes_do_banco()

#%%
df = pd.DataFrame(df_transacoes)
df.head()