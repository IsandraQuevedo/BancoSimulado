--Version anterior del trigger (guardado como respaldo)

CREATE TRIGGER ActualizarSaldo
ON Transacciones
AFTER INSERT
AS
BEGIN
SET NOCOUNT ON;

UPDATE cb
SET cb.Saldo = 
CASE
WHEN t.TipoTransaccion =
'Deposito' THEN cb.Saldo + t.Monto
WHEN t.TipoTransaccion = 
'Retiro' THEN cb.Saldo - t.Monto
END 
FROM CuentasBancarias cb
INNER JOIN	inserted t ON
cb.NumeroCuenta = t.NumeroCuenta;
END;