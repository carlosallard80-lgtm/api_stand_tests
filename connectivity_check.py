import requests
import configuration

print("=== DIAGNÓSTICO DE CONECTIVIDAD ===")

# Test 1: Servidor base
print("\n1. Probando servidor base...")
try:
    response = requests.get(configuration.URL_SERVICE)
    print(f"   Status: {response.status_code}")
    print(f"   URL: {configuration.URL_SERVICE}")
except Exception as e:
    print(f"   Error: {e}")

# Test 2: Endpoint de documentación
print("\n2. Probando endpoint de documentación...")
try:
    doc_response = requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)
    print(f"   Status: {doc_response.status_code}")
    print(f"   URL: {configuration.URL_SERVICE + configuration.DOC_PATH}")
except Exception as e:
    print(f"   Error: {e}")

# Test 3: Endpoint de usuarios (con datos mínimos)
print("\n3. Probando endpoint de usuarios...")
try:
    test_response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json={"test": "connectivity"},
        headers={"Content-Type": "application/json"}
    )
    print(f"   Status: {test_response.status_code}")
    print(f"   URL: {configuration.URL_SERVICE + configuration.CREATE_USER_PATH}")
except Exception as e:
    print(f"   Error: {e}")

print("\n=== FIN DEL DIAGNÓSTICO ===")