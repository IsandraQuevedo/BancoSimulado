# BancoSimulado
Proyecto personal usando SQL, Python y Power BI

*BancoSimulado* es un sistema de cajero automático en consola hecho en Python, conectado a una base de datos en SQL Server, con visualización de transacciones en Power BI. Este proyecto simula operaciones reales como consultas de saldo, depósitos, retiros, transferencias y muestra los movimientos del cliente mediante gráficos.

## 🛠️ Tecnologías utilizadas

- Python (con pyodbc para conexión a SQL Server)
- SQL Server (base de datos, triggers y validaciones)
- Power BI (visualización de transacciones)
- SQL Server Management Studio

## 🎯 Funcionalidades principales

- Consultar saldo disponible
- Realizar depósitos y retiros (con confirmación y validaciones)
- Transferencias entre cuentas (con límites diarios)
- Validación de saldo insuficiente y cuentas inexistentes
- Historial de transacciones completo
- Dashboard en Power BI por cliente y tipo de movimiento

## ✨ Demostración

Observa el sistema en acción:
En esta demostración, se observa el flujo completo del cajero automático. Tras ingresar una de las cuentas configuradas en SQL Server, el sistema presenta un menú interactivo. Se ilustran funcionalidades clave como:

* **Consulta de saldo:** Verificación instantánea del dinero disponible.
* **Retiros:** Demostración de extracciones de efectivo, incluyendo el límite máximo diario.
* **Gestión de errores:** Prueba de una transacción con un monto superior al saldo disponible, mostrando la validación de seguridad.
* **Historial de transacciones:** Visualización detallada de todos los movimientos de la cuenta.
![Captura de pantalla del sistema]()
Accede al siguiente link de Youtube para ver la demostración 👉 (https://www.youtube.com/watch?v=yRlqixxkXmk)

## 📝 Requisitos

Para ejecutar este proyecto, necesitarás:
- Python 3.x 
- SQL Server 
- SQL Server Management Studio 
- El módulo `pyodbc` de Python (se instalará con `pip install pyodbc`)
- Power BI Desktop (para ver el dashboard)

## ⚙️ Cómo ejecutar el proyecto

1. Instala Python 3 y SQL Server.
2. Ejecuta los scripts .sql en el orden correcto usando SQL Server Management Studio.
3. Abre el archivo Python:
  ```bash
python cajero_automatico.py
 ```
4. Abre el archivo .pbix en Power BI para ver los gráficos.

## ✍️ Autora

Isandra Quevedo
Estudiante de informática con interés en desarrollo de software, análisis de datos,automatización y paginas web
📧 quevedoisandra@gmail.com

## 📄 Licencia

Este proyecto es educativo.
