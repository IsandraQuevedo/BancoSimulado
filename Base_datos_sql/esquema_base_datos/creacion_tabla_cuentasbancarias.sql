--Crear la tabla CuentasBancarias

CREATE TABLE CuentasBancarias (
NumeroCuenta VARCHAR(20) PRIMARY KEY,
ID_Cliente INT,
TipoCuenta VARCHAR(50),
Saldo DECIMAL(18,2),
FechaApertura DATE DEFAULT
GETDATE(),

FOREIGN KEY (ID_Cliente) REFERENCES
Clientes(ID)
);