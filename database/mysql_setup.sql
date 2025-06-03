cat > database/mysql_setup.sql << 'EOF'
CREATE DATABASE IF NOT EXISTS iot_data;
USE iot_data;

CREATE TABLE IF NOT EXISTS sensor_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    timestamp DATETIME NOT NULL,
    value VARCHAR(255) NOT NULL
);

-- Opcional: Ejemplo de vista para Grafana
CREATE VIEW sensor_data_view AS
SELECT timestamp, value FROM sensor_data;
EOF