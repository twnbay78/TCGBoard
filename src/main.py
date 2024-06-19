import tkinter as tk
from threading import Thread
from datetime import datetime, timedelta
from tcgplayer_connector import TcgPlayerData, MarketplaceSearchConnector

class MtgDashboardWindow:
    def __init__(self, root, refresh_frequency=60000):
        self.root = root
        self.root.title("Personal MTG Dashboard")
        
        # Create a label to display data
        self.data_label = tk.Label(root, text="Initializing...", font=("Helvetica", 16))
        self.data_label.pack(padx=20, pady=20)

        # Set window icon 
        root.iconbitmap("../resources/mtg_icon.ico")
        
        # Make the window resizable
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        
        # Start the background thread to refresh data
        self.global_last_refresh_time = None
        self.refresh_frequency = refresh_frequency # Refresh every 60000 milliseconds (1 minute)
        self.refresh_data()

    def fetch_data(self):
        # Simulate data fetching logic
        # Replace this with actual business logic to pull data
        marketplace_search_connector = MarketplaceSearchConnector()
        mh3_market_price = marketplace_search_connector.get_lowest_price_with_shipping_by_url_name("Modern Horizons 3 Collector Booster Display")
        mh3_lowest_price_with_shipping = marketplace_search_connector.get_market_price_by_url_name("Modern Horizons 3 Collector Booster Display")
        self.global_last_refresh_time = datetime.now()
        next_refresh = self.global_last_refresh_time + timedelta(milliseconds=self.refresh_frequency)
        time_str = "%Y-%m-%d %H:%M"
        output_data = (
            f"Last refresh: {str(self.global_last_refresh_time.strftime(time_str))}\n"
            f"Next Refresh: {next_refresh.strftime(time_str)}\n"
            "-----\n"
            "Modern Horizons 3 Collector Booster Display\n"
            f"Market Price: ${str(mh3_market_price)}\n"
            f"Lowest TCGPlayer Price: ${str(mh3_lowest_price_with_shipping)}\n"
        )

        return output_data

    def refresh_data(self):
        # Fetch new data
        new_data = self.fetch_data()
        
        # Update the label with new data
        self.data_label.config(text=new_data)
        
        # Schedule the next data refresh
        self.root.after(self.refresh_frequency, self.refresh_data)  # Refresh every 60000 milliseconds (1 minute)

def run_app():
    root = tk.Tk()
    app = MtgDashboardWindow(root)
    root.mainloop()

# Run the app
if __name__ == "__main__":
    run_app()
