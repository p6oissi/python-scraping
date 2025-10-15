from src.utils import run_periodically

if __name__ == '__main__':
    keyword = input("Enter the keyword: ")
    run_periodically(keyword, interval=100)