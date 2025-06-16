--Agregar saldo a cuenta

ALTER TABLE CuentasBancarias
ADD Saldo DECIMAL(10, 2) DEFAULT 0; 