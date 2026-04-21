import unittest
from src.utils.optimizer import optimize_terraform_json
import os
import json

class TestOptimizer(unittest.TestCase):
    def test_migration_to_arm(self):
        sample = {"resource": {"aws_instance": {"app": {"instance_type": "t3.medium"}}}}
        with open("test_main.json", "w") as f:
            json.dump(sample, f)
        optimize_terraform_json("test_main.json")
        with open("test_main.json", "r") as f:
            data = json.load(f)
        self.assertEqual(data["resource"]["aws_instance"]["app"]["instance_type"], "t4g.medium")
        os.remove("test_main.json")

if __name__ == "__main__":
    unittest.main()
