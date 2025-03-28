# Configuración de la conexión a Azure Data Lake Storage
storage_account = "https://azdletluao.dfs.core.windows.net"
container = "uao"
file_path_EEUU = "etl/datos_EEUU/Breast_Cancer.csv"
file_path_colombia = "etl/datos_colombia/Cancer-de-mama-datos-abiertos.csv"
sas_token = "sp=racwdlmeop&st=2025-03-17T17:32:07Z&se=2026-01-01T01:32:07Z&spr=https&sv=2022-11-02&sr=c&sig=oW%2FVy%2Fe8ursHd%2FrkBli26wRGclIfhGsSg7IbgrahYz4%3D"

# Configuración de la conexión a Azure SQL Database
server = 'server-uao-etl.database.windows.net'
database = 'uao-etl'
username = 'useruao'
password = 'Passuao123'
driver = 'ODBC Driver 17 for SQL Server'