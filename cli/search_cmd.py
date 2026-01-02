import sys
from core.search import semantic_search


def main():
    query = sys.argv[1]
    results = semantic_search(query)

    for r in results:
        print(r)


if __name__ == "__main__":
    main()
