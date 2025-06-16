--Prueba de caso negativo: retiro con fondos insuficientes

INSERT INTO Transacciones (NumeroCuenta,
Fecha, Monto, TipoTransaccion)
VALUES ('0102123456789012', GETDATE(), 3480.00,
'Retiro');