import pyfiglet

def generate_bradesco_ascii():
    ascii_art = pyfiglet.figlet_format("bradesco - Stratbox")
    print(ascii_art)

if __name__ == "__main__":
    generate_bradesco_ascii()