import unittest
import json
import os
from src.core.main import SREGenAgent

class TestSREGenAgent(unittest.TestCase):
    def setUp(self):
        self.agent = SREGenAgent()

    def test_json_generation(self):
        # Mock de respuesta del modelo o prueba de estructura
        # Como es un agente IA, probamos si el archivo se genera
        self.agent.interact("Basic web server")
        self.assertTrue(os.path.exists("main.tf.json"))
        with open("main.tf.json", "r") as f:
            data = json.load(f)
            self.assertIn("provider", data)

if __name__ == "__main__":
    unittest.main()
