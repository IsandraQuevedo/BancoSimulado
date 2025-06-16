import pyodbc
from decimal import Decimal, InvalidOperation
from datetime import datetime

# Conexión a SQL Server
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-QVTKL1N\SQLEXPRESS;DATABASE=BancoSimulado;Trusted_Connection=yes;")
cursor = conn.cursor()

 # Límites
LIMITE_RETIROS_DIARIOS = 5
MAX_RETIRO_BS = Decimal("800000.00")
MAX_TRANSFERENCIA_BS_DIA = Decimal("100000.00")

# Montos con punto o coma
def convertir_monto(input_str):
    try:
        return Decimal(input_str.replace(',', '.'))
    except InvalidOperation:
        return None

# Verificar si la cuenta existe 
def cuenta_existe(numero_cuenta_str): 
    try:
        cursor.execute("SELECT 1 FROM CuentasBancarias WHERE NumeroCuenta = ?", numero_cuenta_str)
        return cursor.fetchone() is not None
    except Exception as e:
        print(f"Error técnico al verificar la existencia de la cuenta: {e}")
        return False

# Consultar saldo 
def consultar_saldo(numero_cuenta_str): 
    try:
        cursor.execute("SELECT Saldo FROM CuentasBancarias WHERE NumeroCuenta = ?", numero_cuenta_str)
        resultado = cursor.fetchone()
        return resultado[0] if resultado else None
    except Exception as e:
        print(f"Error técnico al consultar el saldo: {e}")
        return None
    
# Ver historial 
def ver_historial(numero_cuenta_str): 
    cursor.execute("SELECT Fecha, TipoTransaccion, Monto FROM Transacciones WHERE NumeroCuenta = ? ORDER BY Fecha DESC", numero_cuenta_str)
    transacciones = cursor.fetchall()
    if not transacciones:
        print("No hay transacciones registradas.")
    else:
        print("\n--- HISTORIAL DE TRANSACCIONES ---")
        for t in transacciones:
            fecha = t[0].strftime('%d/%m/%Y %H:%M')
            print(f"{fecha} - {t[1]}: Bs {t[2]:,.2f}")

# Contar retiros 
def contar_retiros_hoy(numero_cuenta_str): 
    cursor.execute("""
        SELECT COUNT(*) FROM Transacciones
        WHERE NumeroCuenta = ? AND TipoTransaccion = 'Retiro'
        AND CONVERT(date, Fecha) = CONVERT(date, GETDATE())
    """, numero_cuenta_str)
    return cursor.fetchone()[0]

# Sumar transferencias 
def total_transferencias_hoy(numero_cuenta_str): 
    cursor.execute("""
        SELECT ISNULL(SUM(Monto), 0) FROM Transacciones
        WHERE NumeroCuenta = ? AND TipoTransaccion = 'Transferencia Salida'
        AND CONVERT(date, Fecha) = CONVERT(date, GETDATE())
    """, numero_cuenta_str)
    return cursor.fetchone()[0]

# Retiro 
def realizar_retiro(numero_cuenta_str, monto): 
    saldo = consultar_saldo(numero_cuenta_str) 
    if saldo is None:
        print("Error: la cuenta no existe o saldo no disponible. Verifique el número de cuenta.")
        return
    if monto > saldo:
        print("Saldo insuficiente.")
        return
    if monto > MAX_RETIRO_BS:
        print(f"El monto máximo por retiro es Bs {MAX_RETIRO_BS:,.2f}")
        return
    if contar_retiros_hoy(numero_cuenta_str) >= LIMITE_RETIROS_DIARIOS:
        print("Límite diario de retiros alcanzado.")
        return
    confirm = input(f"Confirmar retiro de Bs {monto:,.2f}? (s/n): ").lower()
    if confirm != 's':
        print("Operación cancelada.")
        return
    cursor.execute("UPDATE CuentasBancarias SET Saldo = Saldo - ? WHERE NumeroCuenta = ?", monto, numero_cuenta_str) 
    cursor.execute("INSERT INTO Transacciones (NumeroCuenta, TipoTransaccion, Monto, Fecha) VALUES (?, 'Retiro', ?, GETDATE())", numero_cuenta_str, monto) 
    conn.commit()
    print("Retiro realizado con éxito.")

# Transferencia 
def realizar_transferencia(origen_cuenta_str, destino_cuenta_str, monto): 
    if not cuenta_existe(destino_cuenta_str): 
        print("La cuenta destino no existe.")
        return
    saldo = consultar_saldo(origen_cuenta_str) 
    if saldo is None:
        print("Error al consultar el saldo de la cuenta origen. Verifique el número de cuenta.")
        return
    if monto > saldo:
        print("Saldo insuficiente.")
        return
    if total_transferencias_hoy(origen_cuenta_str) + monto > MAX_TRANSFERENCIA_BS_DIA:
        print(f"Supera el límite diario de Bs {MAX_TRANSFERENCIA_BS_DIA:,.2f} en transferencias.")
        return
    confirm = input(f"Confirmar transferencia de Bs {monto:,.2f} a la cuenta {destino_cuenta_str}? (s/n): ").lower()
    if confirm != 's':
        print("Operación cancelada.")
        return
    cursor.execute("UPDATE CuentasBancarias SET Saldo = Saldo - ? WHERE NumeroCuenta = ?", monto, origen_cuenta_str) 
    cursor.execute("UPDATE CuentasBancarias SET Saldo = Saldo + ? WHERE NumeroCuenta = ?", monto, destino_cuenta_str) 
    cursor.execute("INSERT INTO Transacciones (NumeroCuenta, TipoTransaccion, Monto, Fecha) VALUES (?, 'Transferencia Salida', ?, GETDATE())", origen_cuenta_str, monto) 
    cursor.execute("INSERT INTO Transacciones (NumeroCuenta, TipoTransaccion, Monto, Fecha) VALUES (?, 'Transferencia Entrada', ?, GETDATE())", destino_cuenta_str, monto) 
    conn.commit()
    print("Transferencia completada con éxito.")

# Menú principal
def main():
    print("Bienvenido querido usuario al cajero automático de BancoSimulado")
    
    while True: 
        numero_cuenta_ingresado = input("Ingrese su número de cuenta: ") 
        
        
        if not numero_cuenta_ingresado.isdigit():
            print("Por favor, ingrese un número de cuenta válido (solo dígitos).")
            continue
            
        if not cuenta_existe(numero_cuenta_ingresado): 
            print("La cuenta ingresada no existe.")
            continue 
        else:
            break 

    while True:
        print("\nSeleccione su operación:")
        print("1. Saldo disponible")
        print("2. Retiro")
        print("3. Transferencia")
        print("4. Ver historial")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            saldo = consultar_saldo(numero_cuenta_ingresado) 
            if saldo is not None:
                print(f"Su saldo disponible es Bs {saldo:,.2f}")
            else:
                print("Error al consultar el saldo. Por favor, intente de nuevo.") 
        elif opcion == "2":
            monto = convertir_monto(input("Ingrese el monto a retirar: "))
            if monto is None:
                print("Monto inválido.")
                continue
            realizar_retiro(numero_cuenta_ingresado, monto) 
        elif opcion == "3":
            destino_cuenta_ingresado = input("Ingrese el número de cuenta destino: ") 
            
            
            if not destino_cuenta_ingresado.isdigit():
                print("Por favor, ingrese un número de cuenta destino válido (solo dígitos).")
                continue

            monto = convertir_monto(input("Ingrese el monto a transferir: "))
            if monto is None:
                print("Monto inválido.")
                continue
            realizar_transferencia(numero_cuenta_ingresado, destino_cuenta_ingresado, monto) 
        elif opcion == "4":
            ver_historial(numero_cuenta_ingresado) 
        elif opcion == "5":
            print("Gracias por usar BancoSimulado. ¡Hasta luego!")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()
