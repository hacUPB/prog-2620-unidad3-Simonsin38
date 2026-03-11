# **Reto Unidad 3** 🏆
# ✈️ Reto de Programación: Sistema de Monitoreo de Combustible y Seguridad en Ruta (SMCS)

<aside>
⚠️

**¡Importante!**
No se permite el uso de código no visto en clase.

</aside>

## 🌍 El Contexto (Idea General)

En la aviación comercial, la gestión del combustible es un factor crítico de seguridad y eficiencia. Un avión no solo debe llevar combustible para llegar a su destino, sino también reservas legales para emergencias, desvíos por clima y tiempos de espera. Las condiciones de ruta, como el viento en contra o a favor, alteran dinámicamente el consumo.

## ❓ Pregunta Esencial

*¿Cómo podemos utilizar la lógica computacional para predecir el consumo de combustible de una aeronave en tiempo real y tomar decisiones de desvío automático que garanticen la seguridad del vuelo?*

## 🎯 El Desafío

Eres el ingeniero aeronáutico encargado de programar el **SMCS**, un sistema básico a bordo de un bimotor comercial. El avión tiene una ruta programada que consta de **un número de tramos (waypoints)**. Tu programa debe simular el vuelo, calculando el combustible restante después de cada tramo y tomando decisiones críticas si las reservas se ven comprometidas.

**Reglas del Sistema:**

1. **Capacidad Inicial:** El avión despega con un valor de combustible en el tanque en kilogramos.
2. **Consumo Base:** investiga cuál podría ser un consumo estándar en kilogramos por kilómetro.
3. **Efecto del Viento:**
    - Si hay viento en contra (Headwind), el consumo aumenta en “digamos” un 20%. Este valor, lo debes investigar tú y lo debes justificar. No puede ser el mismo de los otros grupos.
    - Si hay viento a favor (Tailwind), el consumo se reduce en `otro valor` que investigarás también.
    - Si el viento es cruzado o nulo, el consumo es el base.
4. **Reserva Legal:** El avión **nunca** puede bajar de un valor de combustible (este será el límite que tú debes definir). Si al proyectar el siguiente tramo el combustible caerá por debajo de este límite, el sistema debe emitir una alerta crítica, abortar la ruta y aterrizar en el aeropuerto alterno más cercano.