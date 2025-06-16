--Crear tabla Clientes

CREATE TABLE Clientes (
ID INT PRIMARY KEY IDENTITY(1,1),
Nombre NVARCHAR(100),
Cedula VARCHAR(20),
Correo VARCHAR(100),
Telefono VARCHAR(15),
FechaRegristro DATE DEFAULT GETDATE()
);