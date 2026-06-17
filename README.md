# 🧪 Proyecto Final - Automatización QA

## 📌 Descripción
Este proyecto tiene como objetivo automatizar pruebas funcionales sobre el sitio SauceDemo y pruebas de API sobre ReqRes, utilizando Selenium con Python y el patrón Page Object Model.

Se validan flujos completos como:

- Login de usuario (válido, inválido, parametrizado con CSV)
- Navegación e inventario de productos
- Gestión del carrito de compras (data-driven con JSON)
- Flujo completo de checkout
- Pruebas de API REST (GET, POST, DELETE)
- Escenarios BDD con Behave

El propósito es aplicar los conocimientos adquiridos durante el curso, enfocándose en buenas prácticas de automatización QA.

---

## 🌐 Sitios Utilizados

- https://www.saucedemo.com
- https://reqres.in

---

## 🚀 Tecnologías Utilizadas
- Python 3.11+
- Selenium WebDriver
- Pytest
- Requests
- Behave (BDD)
- pytest-html
- Git & GitHub

---

## 📂 Estructura del Proyecto

```text
proyecto-final-automation-testing-jessica-puricelli/
├── data/
│   ├── users.csv
│   └── products.json
├── features/
│   ├── login.feature
│   ├── environment.py
│   └── steps/
│       └── login_steps.py
├── page/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_login_csv.py
│   ├── test_inventory.py
│   ├── test_cart.py
│   ├── test_cart_json.py
│   ├── test_checkout.py
│   └── test_api.py
├── utils/
│   ├── logger.py
│   └── data_reader.py
├── conftest.py
├── pytest.ini
└── requirements.txt
```

Las carpetas `reports/`, `screenshots/` y `logs/` se generan automáticamente al ejecutar los tests.

---

## Instalación de Dependencias

1. Clonar el repositorio:
```bash
git clone https://github.com/Jess-Vp/proyecto-final-automation-testing-jessica-puricelli.git
cd proyecto-final-automation-testing-jessica-puricelli
```

2. Crear tu entorno virtual:
```bash
python -m venv venv
```

3. Activar entorno virtual:
```bash
# Mac / Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

4. Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución de Pruebas

Ejecutar todos los tests:
```bash
pytest
```

Solo tests de API (no requieren Chrome):
```bash
pytest tests/test_api.py
```

Solo tests de UI:
```bash
pytest tests/test_login.py tests/test_inventory.py tests/test_cart.py tests/test_checkout.py
```

Tests BDD con Behave:
```bash
behave
```

Ejecutar un test específico:
```bash
pytest tests/NOMBRE_DEL_FILE.py
```

El reporte HTML se genera automáticamente en `reports/report.html`.

---

## 🧪 Casos de Prueba Implementados

### Login
- Login exitoso con credenciales válidas
- Login con password inválido
- Login con usuario inválido
- Login parametrizado con datos desde `users.csv`

### Inventario
- Validación del título de la página
- Verificación de productos visibles
- Validación de nombre y precio del primer producto
- Verificación de elementos de UI (menú y filtro)
- Validación de opciones del filtro (Name A-Z, Z-A, Price low-high, high-low)

### Carrito
- Agregar producto al carrito y validar contador
- Verificar que el producto en carrito coincide con el seleccionado
- Data-driven: agregar múltiples productos desde `products.json` y validar carrito

### Checkout
- Flujo completo: agregar producto → carrito → checkout → confirmación
- Validación de error al continuar sin datos personales

### API REST (reqres.in)
- Login válido
- Login sin password
- Login sin email
- Crear usuario
- Eliminar usuario
- Obtener usuario y validar tiempo de respuesta

### BDD (Behave)
- Login exitoso
- Login con credenciales inválidas
- Login con campos vacíos
