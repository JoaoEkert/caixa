from teste import test_authentication
from teste import test_data_entry
from teste import test_performance
from teste import test_usability

def run_all_tests():
    test_authentication.teste_autenticacao()
    test_data_entry.teste_entrada_dados()
    test_performance.teste_desempenho()
    test_usability.teste_usabilidade()

if __name__ == "__main__":
    run_all_tests()