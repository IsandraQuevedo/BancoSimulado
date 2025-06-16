--Coreccion de transferencias para codigo de python 3

ALTER TABLE Transacciones
ADD CONSTRAINT CK_TipoTransaccion
CHECK (TipoTransaccion IN (
'Retiro',
'Deposito',
'Transferencia Entrada',
'Transferencia Salida'
));