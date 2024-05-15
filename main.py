from processor import cli_processor
from handler import compose_handlers
from commands.handlers import get_handlers
from commands.types import Dependencies
from storage.address_book import AddressBook

def main():
    address_book = AddressBook()
    dependencies = Dependencies(address_book)

    handlers = get_handlers(dependencies)
    handler = compose_handlers(handlers)

    start = cli_processor(handler)
    start()

if __name__ == "__main__":
    main()