import pandas as pd

def save_to_csv(data, filename):

    data = pd.DataFrame(data)
    output_filename = f"{filename}.csv"
    data.to_csv(output_filename, index=False)
    print(f"Data saved to {output_filename}")