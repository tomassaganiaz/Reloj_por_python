from reloj.builder import RelojBuilder

class ConsolaReloj:
    def __init__(self):
        self.relojes = []

    def crear_reloj(self):
        try:
            h = int(input("Hora (0-23): "))
            m = int(input("Minuto (0-59): "))
            s = int(input("Segundo (0-59): "))
        except ValueError:
            print("Por favor, ingresá números enteros válidos.")
            return
        
        # Validar los valores (podrías usar funciones del módulo utils.py si lo tienes)
        if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
            print("Valores de hora, minuto o segundo fuera de rango.")
            return
        
        reloj = RelojBuilder().con_hora(h).con_minutos(m).con_segundos(s).construir()
        self.relojes.append(reloj)
        print("Reloj creado:", reloj.mostrar())

    def mostrar_relojes(self):
        if not self.relojes:
            print("No hay relojes creados.")
            return
        for i, r in enumerate(self.relojes):
            print(f"[{i}] {r.mostrar()}")

    def adelantar_minuto(self):
        if not self.relojes:
            print("No hay relojes para adelantar.")
            return
        self.mostrar_relojes()
        try:
            idx = int(input("¿Qué reloj querés adelantar? "))
            if idx < 0 or idx >= len(self.relojes):
                print("Índice inválido.")
                return
        except ValueError:
            print("Ingresá un número válido.")
            return
        self.relojes[idx].adelantar_minuto()
        print("Nuevo valor:", self.relojes[idx].mostrar())

    def actualizar_hora(self):
        if not self.relojes:
            print("No hay relojes para modificar.")
            return
        self.mostrar_relojes()
        try:
            idx = int(input("¿Qué reloj querés modificar? "))
            if idx < 0 or idx >= len(self.relojes):
                print("Índice inválido.")
                return
            h = int(input("Nueva hora (0-23): "))
            m = int(input("Nuevo minuto (0-59): "))
            s = int(input("Nuevo segundo (0-59): "))
        except ValueError:
            print("Ingresá números enteros válidos.")
            return
        if not (0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59):
            print("Valores fuera de rango.")
            return
        self.relojes[idx].actualizar_hora(h, m, s)
        print("Hora actualizada:", self.relojes[idx].mostrar())

    def comparar_relojes(self):
        if len(self.relojes) < 2:
            print("Necesitás al menos dos relojes para comparar.")
            return
        self.mostrar_relojes()
        try:
            a = int(input("Reloj A: "))
            b = int(input("Reloj B: "))
            if any(idx < 0 or idx >= len(self.relojes) for idx in (a,b)):
                print("Índices inválidos.")
                return
        except ValueError:
            print("Ingresá números válidos.")
            return
        iguales = self.relojes[a].es_igual(self.relojes[b])
        print("Son iguales." if iguales else "Son distintos.")

    def iniciar(self):
        while True:
            print("\n--- MENÚ ---")
            print("1. Crear reloj")
            print("2. Mostrar relojes")
            print("3. Adelantar un minuto")
            print("4. Modificar hora")
            print("5. Comparar relojes")
            print("6. Salir")

            opcion = input("Elegí una opción: ")

            if opcion == "1":
                self.crear_reloj()
            elif opcion == "2":
                self.mostrar_relojes()
            elif opcion == "3":
                self.adelantar_minuto()
            elif opcion == "4":
                self.actualizar_hora()
            elif opcion == "5":
                self.comparar_relojes()
            elif opcion == "6":
                print("¡Chau!")
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__":
    app = ConsolaReloj()
    app.iniciar()
