import matplotlib.pyplot as plt
import numpy as np # Necesitamos numpy para algunas operaciones matemáticas y de color

# Paso 1: Creamos una lista de pacientes (tu base de datos simulada)
pacientes = [
    {"nombre": "Ana Pérez", "presion_arterial": 125, "glucosa": 90},
    {"nombre": "Juan García", "presion_arterial": 155, "glucosa": 105}, # Alto riesgo
    {"nombre": "María López", "presion_arterial": 120, "glucosa": 120}, # Alto riesgo
    {"nombre": "Pedro Rodríguez", "presion_arterial": 135, "glucosa": 98},
    {"nombre": "Sofía Vargas", "presion_arterial": 160, "glucosa": 135}  # Alto riesgo
]

print("Analizando los datos de los pacientes y generando gráficos...\n")

for paciente in pacientes:
    nombre = paciente["nombre"]
    presion = paciente["presion_arterial"]
    glucosa = paciente["glucosa"]

    # Paso 2: Definimos los umbrales de riesgo
    RIESGO_PRESION = 140
    RIESGO_GLUCOSA = 110

    riesgo_glucosa = glucosa > RIESGO_GLUCOSA
    riesgo_presion = presion > RIESGO_PRESION

    # Paso 3: Decidimos el color de la alerta (rojo o verde) y el título
    color_glucosa = 'red' if riesgo_glucosa else 'green'
    color_presion = 'red' if riesgo_presion else 'green'
    
    titulo_paciente = f"Paciente: {nombre}"
    if riesgo_glucosa or riesgo_presion:
        titulo_paciente += " (¡RIESGO ALTO!)"
        borde_color = 'red'
    else:
        borde_color = 'green'

    # --- Generación del Gráfico ---
    
    # Creamos una "ventana" para nuestro gráfico
    fig, ax = plt.subplots(figsize=(6, 4), edgecolor=borde_color, linewidth=3) # Agregamos un borde
    
    # Datos para las barras
    etiquetas = ['Presión Arterial', 'Glucosa']
    valores = [presion, glucosa]
    colores_barras = [color_presion, color_glucosa]

    # Creamos las barras
    ax.bar(etiquetas, valores, color=colores_barras)
    
    # Añadimos los valores encima de cada barra
    for i, v in enumerate(valores):
        ax.text(i, v + 5, str(v), ha='center', va='bottom', fontsize=12, color=colores_barras[i])

    # Líneas de umbral de riesgo para que el médico vea la referencia
    ax.axhline(y=RIESGO_PRESION, color='red', linestyle='--', label=f'Riesgo Presión (> {RIESGO_PRESION})')
    ax.axhline(y=RIESGO_GLUCOSA, color='orange', linestyle='--', label=f'Riesgo Glucosa (> {RIESGO_GLUCOSA})')


    # Configuramos el título y etiquetas
    ax.set_title(titulo_paciente, fontsize=16, color=borde_color)
    ax.set_ylabel('Valores', fontsize=12)
    ax.legend()
    ax.set_ylim(0, max(presion, glucosa) + 30) # Ajustamos el límite Y para que los números no se salgan

    # Mostrar el gráfico (esto generará una imagen diferente para cada paciente)
    plt.tight_layout() # Ajusta el diseño para que no se superpongan elementos
    plt.show()

    # Opcional: Guardar el gráfico como una imagen (ej. PNG)
    # plt.savefig(f"reporte_paciente_{nombre.replace(' ', '_')}.png")
    # plt.close(fig) # Cierra la figura para liberar memoria si vas a generar muchas
    
    print("\n" + "="*70 + "\n") # Separador para los resultados en texto
