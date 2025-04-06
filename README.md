# Quirk Zigbee para TS0601 (_TZE284_iwn0gpzz)

Este repositorio contiene un **quirk personalizado para Home Assistant + ZHA**, creado para el dispositivo **TS0601** con el identificador Tuya `_TZE284_iwn0gpzz`.

## Características detectadas

Este quirk permite exponer correctamente los siguientes sensores:

- Energía consumida total (`kWh`)
- Energía producida total (`kWh`)
- Potencia activa total (`W`)
- Frecuencia AC (`Hz`)
- Factor de potencia (`%`)
- Voltaje fase (`V`)
- Corriente fase (`A`)
- Potencia fase (`W`)

## Uso

1. Copia este archivo en tu directorio de `custom_zha_quirks` (si usas `zha-custom`).
2. Asegúrate de que Home Assistant lo detecte reiniciando el sistema o recargando ZHA.
3. El dispositivo debe ser identificado como compatible por su modelo (`TS0601`) y fabricante (`_TZE284_iwn0gpzz`).

## Notas

- Basado en el nuevo sistema de `TuyaQuirkBuilder` de ZHA.
- Se usaron divisores estándar para representar los valores correctamente en sus unidades físicas.

---