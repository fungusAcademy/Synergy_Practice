import unittest 
from worker import WORKER

class TestWorker(unittest.TestCase):
    def setUp(self):
        self.worker = WORKER("Иванов А.И.", "Профессор", 120000, 2010)
    
    def test_calculate_experience(self):
        self.assertEqual(self.worker.calculate_experience(2024), 14)
    
    def test_setters_getters(self):
        self.worker.set_salary(130000)
        self.assertEqual(self.worker.salary, 130000)
        
        self.worker.set_position("Декан")
        self.assertEqual(self.worker.position, "Декан")
    
    def test_initialization(self):
        self.assertEqual(self.worker.surname_initials, "Иванов А.И.")
        self.assertEqual(self.worker.start_year, 2010)

if __name__ == '__main__':
    unittest.main()