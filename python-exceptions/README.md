# Python - Exceptions

Este proyecto trata sobre el manejo de **excepciones en Python**, una de las características más poderosas del lenguaje. Aprenderás a detectar errores, cómo capturarlos adecuadamente, cómo lanzar excepciones personalizadas y cómo limpiar recursos tras una falla.

## 📌 General

### ✅ Why Python programming is awesome

Python es un lenguaje de programación altamente legible, intuitivo y versátil. Su manejo de errores es uno de los aspectos que lo hace tan poderoso, ya que permite escribir código más seguro, controlado y a prueba de fallos. Gracias a su sistema de excepciones, podemos anticiparnos a los errores y actuar en consecuencia sin que el programa termine abruptamente.

---

### ⚠️ What’s the difference between errors and exceptions

- **Errors** (errores): Son fallos graves que normalmente no pueden ser gestionados por el programa, como errores de sintaxis o problemas del intérprete (por ejemplo, `SyntaxError` o `IndentationError`). Estos ocurren antes o durante la ejecución y normalmente detienen el programa.

- **Exceptions** (excepciones): Son eventos que ocurren durante la ejecución del programa y que pueden ser **manejados por el programador** para evitar que el programa se detenga. Ejemplos: `ZeroDivisionError`, `ValueError`, `TypeError`, etc.

---

### 🧱 What are exceptions and how to use them

Una **excepción** es un objeto especial que indica la ocurrencia de un error durante la ejecución. Python provee una estructura para **"intentar" código y capturar errores** con la sintaxis `try...except`.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("¡No se puede dividir por cero!")

