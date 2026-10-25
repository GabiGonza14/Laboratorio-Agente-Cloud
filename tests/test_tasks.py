import unittest

from tasks import agregar_tarea, completar_tarea, pendientes


class TestTasks(unittest.TestCase):
    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "general")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_con_categoria_valida(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Practicar", "Backend")
        self.assertEqual(tarea["categoria"], "Backend")

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Practicar", "   ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria_sin_mayusculas(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Backend")
        agregar_tarea(tareas, "Leer", "frontend")
        agregar_tarea(tareas, "Deploy", "BACKEND")
        completar_tarea(tareas, 3)

        resultado = pendientes(tareas, "backend")
        self.assertEqual(len(resultado), 1)
        self.assertEqual(resultado[0]["titulo"], "Practicar")


if __name__ == "__main__":
    unittest.main()
