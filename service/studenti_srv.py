from domain.entitati import studenti
from repository.studenti_repo import OperatiiStudenti, OperatiiStudentiFile
from domain.validatori import StudentValidator
from utils.functions import string_generator, number_string_generator
import random
from random import randint

class StudentService:

    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add_student(self, id, nume, grup):
        """
            Functia incearca sa introduca studentul in memorie
        """
        student = studenti(id, nume, grup)
        self.__validator.valideaza_studentul(student)
        self.__repo.adaugare_student(student)
        return student
    
    def delete_student(self, id):
        """
            Functia incearca sa stearga studentul
        """
        self.__repo.stergere_student(id)

    def modify_student(self, id, nume_nou, grup_nou):
        """
            Modifica studentul mentionat
        """
        student = studenti(id, nume_nou, grup_nou)
        self.__validator.valideaza_studentul(student)
        self.__repo.modificare_student(id, nume_nou, grup_nou)
        return student
    
    def search_id(self, id):
        """
            Verificam daca exista student cu id-ul cautat 
        """
        student = self.__repo.cautare_student(id)
        return student
    
    def get_studenti(self):
        """
            Returnam toti studentii din repo
        """
        return self.__repo.returnare_studenti()
    
    def add_random_studenti(self, nr):
        """
            Adaugam studenti random in repo
        """
        for index in range(nr):
            student = studenti(random.randint(1, 100000), string_generator(11), number_string_generator(10))
            self.__validator.valideaza_studentul(student)
            self.__repo.adaugare_student(student)