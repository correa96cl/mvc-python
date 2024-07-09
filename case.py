class AlgumaCoisa:
    def __enter__(self):
        print("Entrei")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Sai")

with AlgumaCoisa() as something:
    print("estou no meio")