-- ver todas las cuentas

SELECT * FROM CuentasBancarias;

--ver cuentas con nombres de clientes

SELECT C.Nombre, C.Cedula, CB.NumeroCuenta, CB.TipoCuenta, CB.Saldo
FROM Clientes C
JOIN CuentasBancarias CB ON C.ID =
CB.ID_Cliente;