#!/usr/bin/env python3

from experta import *
import tkinter as tk
from tkinter import messagebox

class Alergia(Fact):
    """Información acerca de los síntomas de las alergias más comunes"""
    pass

class DiagnosticoAlergia(KnowledgeEngine):
    diagnósticos = set()

    # Reglas para diferentes tipos de alergias
    @Rule(AND(Alergia(nombre='sibilancias'),
              Alergia(nombre='dolor de pecho'),
              Alergia(nombre='disnea'),
              Alergia(nombre='fatiga')))
    def asma(self):
        self.diagnósticos.add('asma')

    @Rule(AND(Alergia(nombre='ronchas'),
              Alergia(nombre='dificultad respiratoria'),
              Alergia(nombre='picor intenso')))
    def urticaria(self):
        self.diagnósticos.add('urticaria')

    @Rule(AND(Alergia(nombre='estornudos'),
              Alergia(nombre='taponamiento nasal'),
              Alergia(nombre='lagrimeo')))
    def rinitis(self):
        self.diagnósticos.add('rinitis')

    @Rule(AND(Alergia(nombre='nauseas'),
              Alergia(nombre='vómito'),
              Alergia(nombre='dolor abdominal'),
              Alergia(nombre='dificultad respiratoria')))
    def alergia_alimentaria(self):
        self.diagnósticos.add('Alergia Alimentaria')

    @Rule(AND(Alergia(nombre='lagrimeo ocular'),
              Alergia(nombre='enrojecimiento ocular'),
              Alergia(nombre='picor'),
              Alergia(nombre='sensibilidad a la luz')))
    def conjuntivitis_alergica(self):
        self.diagnósticos.add('conjuntivitis alérgica')

    @Rule(AND(Alergia(nombre='pérdida de cabello'),
              Alergia(nombre='malestar estomacal'),
              Alergia(nombre='hinchazón de la cara')))
    def alergia_farmacos(self):
        self.diagnósticos.add('Alergia a fármacos')

    @Rule(AND(Alergia(nombre='inflamación local'),
              Alergia(nombre='dolor local'),
              Alergia(nombre='picazón')))
    def alergia_himenopteros(self):
        self.diagnósticos.add('Alergia a himenópteros')

    @Rule(AND(Alergia(nombre='descamación'),
              Alergia(nombre='ampolla'),
              Alergia(nombre='quemadura')))
    def dermatitis_contacto(self):
        self.diagnósticos.add('Dermatitis alérgica de contacto')

    @Rule(NOT(Fact(diagnostico=W())))
    def sin_informacion(self):
        print("No hay información disponible sobre el tipo de alergia según los síntomas ingresados")

def obtener_sintomas():
    # Solicitar al usuario que ingrese los síntomas separados por coma
    sintomas = input("Por favor, introduce tus síntomas separados por coma: ")
    return [sintoma.strip() for sintoma in sintomas.split(',')]

class InterfazSistemaExperto(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Sistema Experto de Alergias")
        self.geometry("400x300")

        # Etiqueta e entrada para los síntomas
        tk.Label(self, text="Ingresa tus síntomas separados por coma:").pack(pady=10)
        self.entry_sintomas = tk.Entry(self)
        self.entry_sintomas.pack(pady=10)

        # Botón para ejecutar el sistema experto
        btn_ejecutar = tk.Button(self, text="Obtener Diagnóstico", command=self.ejecutar_sistema_experto)
        btn_ejecutar.pack(pady=20)

    def ejecutar_sistema_experto(self):
        # Obtener los síntomas del usuario desde la entrada
        sintomas_input = self.entry_sintomas.get()

        # Verificar si se proporcionaron síntomas
        if not sintomas_input:
            messagebox.showinfo("Error", "Por favor, ingresa al menos un síntoma.")
            return

        # Convertir la entrada en una lista de síntomas
        sintomas_presentados = [sintoma.strip() for sintoma in sintomas_input.split(',')]

        # Inicializar el motor de reglas y limpiar diagnósticos previos
        engine = DiagnosticoAlergia()
        engine.reset()

        # Declarar los hechos (síntomas) en el motor de reglas
        for sintoma in sintomas_presentados:
            engine.declare(Alergia(nombre=sintoma))

        # Ejecutar el motor de reglas
        engine.run()

        # Mostrar los diagnósticos acumulados
        if engine.diagnósticos:
            mensaje = "Diagnósticos:\n" + "\n".join(f"- {diagnóstico}" for diagnóstico in engine.diagnósticos)
        else:
            mensaje = "No hay información disponible sobre el tipo de alergia según los síntomas ingresados"

        # Mostrar el resultado en un cuadro de mensaje
        messagebox.showinfo("Resultado del Diagnóstico", mensaje)

if __name__ == "__main__":
    # Crear y ejecutar la interfaz
    app = InterfazSistemaExperto()
    app.mainloop()
