--Crear la tabla Transacciones

CREATE TABLE Transacciones (
ID INT IDENTITY(1,1) PRIMARY KEY,
NumeroCuenta VARCHAR(20) NOT NULL,
TipoTransaccion VARCHAR(10) CHECK
(TipoTransaccion IN ('Deposito', 'Retiro')),
Monto DECIMAL(10, 2) NOT NULL CHECK
(Monto > 0),
Fecha DATETIME DEFAULT GETDATE(),
FOREIGN KEY (NumeroCuenta) 
REFERENCES
CuentasBancarias(NumeroCuenta)
);