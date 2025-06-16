--Trigger activo para actualizar automaticamente el saldo despues de transacciones

CREATE TRIGGER ActualizarSaldo
ON Transacciones
AFTER INSERT
AS
BEGIN
SET NOCOUNT ON;

IF EXISTS (
SELECT 1
FROM inserted i
JOIN CuentasBancarias cb ON
i.NumeroCuenta = cb.NumeroCuenta
WHERE i.TipoTransaccion =
'Retiro'
AND cb.Saldo < i.Monto
)
BEGIN
RAISERROR ('Fondo insuficientes para realizar el retiro.', 16, 1);
ROLLBACK TRANSACTION;
RETURN;
END

UPDATE cb
SET cb.Saldo =
CASE
WHEN i.TipoTransaccion =
'Deposito' THEN cb.Saldo + i.Monto
WHEN i.TipoTransaccion =
'Retiro' THEN cb.Saldo - i.Monto
END
FROM CuentasBancarias cb
INNER JOIN inserted i ON
cb.NumeroCuenta = i.NumeroCuenta;
END;