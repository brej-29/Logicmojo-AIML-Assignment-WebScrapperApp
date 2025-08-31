from scraper import (
    scrape_imdb_top_movies,
    scrape_former_presidents,
)
from utils import save_to_csv

def main():
    while True:
        print("Welcome to the Web Scraper!")
        print("Choose a scraping target:")
        print("1. IMDb Top Movies")
        print("2. Former Presidents of India")

        choice = input("Enter the number of your choice: ")

        if choice == '1':
            data = scrape_imdb_top_movies()
        elif choice == '2':
            data = scrape_former_presidents()
        else:
            print("Invalid choice. Exiting.")
            return

        if not data.empty:
            print("\nScraping completed. Here are the results:")
            print(data)

            save_choice = input("\nDo you want to save the results to a CSV file? (yes/no): ")
            if save_choice.lower() == 'yes':
                filename = input("Enter the filename (without extension): ")
                save_to_csv(data, filename)
            else:
                print("Data not saved.")
        else:
            print("\nScraping failed or no data was found. Please check for error messages above.")

        if input("\nDo you want to scrape again? (yes/no): ").lower() != 'yes':
            print("Exiting the scraper. Goodbye!")
            break

if __name__ == "__main__":
    main()