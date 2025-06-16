--Prueba para hacer un deposito valido

INSERT INTO Transacciones (NumeroCuenta,
Fecha, Monto,
TipoTransaccion)
VALUES ('0102123456789012', GETDATE(), 300.00,
'Deposito');