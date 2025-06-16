--Prueba de caso positivo: retiro valido y exitoso

INSERT INTO Transacciones (NumeroCuenta,
Fecha, Monto, TipoTransaccion)
VALUES ('0102123456789012', GETDATE(), 150.00,
'Retiro');