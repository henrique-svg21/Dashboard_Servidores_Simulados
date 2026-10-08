import sqlite3
import time 
import random
from datetime import datetime

def init_db():
    conn = sqlite3.connect('telemetria.db', timeout=10)
    cursor = conn.cursor()

    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leituras_servidores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp DATETIME,
            server_id TEXT,
            temp_CPU REAL,
            uso_CPU INTEGER,
            uso_RAM INTEGER,
            latencia INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def simular_servidores():
    init_db()
    print("Simulador de servidores em execução. Pressione Ctrl + C para parar")

    servidores = {
        'Servidor_A': {'temp_CPU': 55.0, 'uso_RAM': 72, 'uso_CPU': 90, 'latencia': 32},
        'Servidor_B': {'temp_CPU': 58.5, 'uso_RAM': 89, 'uso_CPU': 78, 'latencia': 18},
        'Servidor_C': {'temp_CPU': 62.0, 'uso_RAM': 56, 'uso_CPU': 69, 'latencia': 23}
    }

    while True:
        try:
            conn = sqlite3.connect('telemetria.db', timeout=10)
            cursor = conn.cursor()
        
            for server_id, dados in servidores.items():
                temp_CPU = round(dados['temp_CPU'] + random.uniform(-0.4, 0.4), 2)
                uso_RAM = round(max(0, min(100, dados['uso_RAM'] + random.uniform(-0.8, 0.8))), 2)
                uso_CPU = round(dados['uso_CPU'] + random.uniform(-0.15, 0.15), 2)
                latencia = round(dados['latencia'] + random.uniform(-0.15, 0.15), 2)
                
                dados['temp_CPU'] = temp_CPU
                dados['uso_RAM'] = uso_RAM
                dados['uso_CPU'] = uso_CPU
                dados['latencia'] = latencia

                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Nome da tabela corrigido para leituras_servidores
                cursor.execute('''
                    INSERT INTO leituras_servidores (timestamp, server_id, temp_CPU, uso_RAM, uso_CPU, latencia)
                    VALUES (?,?,?,?,?,?)
                ''', (timestamp, server_id, temp_CPU, uso_RAM, uso_CPU, latencia))
        
            conn.commit()
            conn.close()

            print(f"[{datetime.now().strftime('%H:%M:%S')}] Novas leituras inseridas.")
            time.sleep(2)

        except sqlite3.OperationalError as e:
            if "locked" in str(e).lower() or "busy" in str(e).lower():
                print(f"Aviso de concorrência: {e}")
                time.sleep(1)
            else:
                raise e
        except KeyboardInterrupt:
            print("\nSimulação finalizada")
            break
    
if __name__ == "__main__":
    simular_servidores()