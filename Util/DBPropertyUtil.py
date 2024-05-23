class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name=r"DESKTOP-QFPQL5Q\MSSQLSERVER01"
        database_name="case study"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str