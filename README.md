# 📡 IoT Data Pipeline: HiveMQ → MySQL → Grafana

Proyecto para transmitir datos desde terminales IoT a un dashboard en Grafana, usando Python como intermediario.

## 🛠️ Tecnologías
- **HiveMQ** (Broker MQTT)
- **Python** (Script de procesamiento)
- **MySQL** (Base de datos)
- **Grafana** (Visualización)

## ⚡ Instalación
1. Clonar repositorio:
   ```bash
   git clone https://github.com/Pablo4604/HydroSense.git

2. Instalar dependencias:

   pip install -r scripts/requirements.txt

4. Ejecutar script:
   
   python scripts/mqtt_a_mysql.py

5. Configuración de Grafana
   
   Importar el dashboard desde /grafana/dashboard.json.

   Configurar MySQL como fuente de datos.


![flujo de datos](https://github.com/user-attachments/assets/dbd45cc9-c1a4-4644-b4ea-23bf4ee35f7e)


   
---
