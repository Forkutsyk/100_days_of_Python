import requests
import os
from dotenv import load_dotenv
from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import Calendar
from datetime import datetime, timedelta
import json
import logging

# Current progress:
# AT least it is now showing the today's amount of pages on the statistic window in the main menu ...
# TODO 1: fix "error" on the AVG and TOTAL on the main screen in the statistic menu it is cuz i'm geting XML answer :1
# TODO 2: fix the buttons on the ADD, UPDATE, DELETE window // probably should use grid ;1

# Set up logging
logging.basicConfig(filename='habit_tracker.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables from parent directory
load_dotenv(dotenv_path='../.env')
TOKEN = os.getenv("PIXELA_TOKEN")
USERNAME = os.getenv("PIXELA_USERNAME")
GRAPH_ID = os.getenv("GRAPH_ID")

if not all([TOKEN, USERNAME, GRAPH_ID]):
    raise ValueError("Missing environment variables. Please check your ../.env file.")


class HabitTracker:
    def __init__(self):
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.graph_endpoint = f"{self.pixela_endpoint}/{USERNAME}/graphs"
        self.pixel_endpoint = f"{self.pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

        self.headers = {
            "X-USER-TOKEN": TOKEN
        }

        self.root = Tk()
        self.root.title("Habit Tracker")
        self.root.geometry("400x250")
        self.define_gui()

    def define_gui(self):
        self.root.configure(bg='#f0f0f0')

        main_frame = Frame(self.root, padx=20, pady=20, bg='#f0f0f0')
        main_frame.pack(fill=BOTH, expand=True)

        stats_frame = Frame(main_frame, relief=RIDGE, borderwidth=2, bg='white')
        stats_frame.pack(fill=X, pady=(0, 20))

        self.total_pages = StringVar(value="0")
        self.avg_pages = StringVar(value="0.0")
        self.today_pages = StringVar(value="0")

        for i, (text, var) in enumerate([("TOTAL", self.total_pages),
                                         ("AVG", self.avg_pages),
                                         ("TODAY", self.today_pages)]):
            Frame(stats_frame, width=120, height=60, bg='white').grid(row=0, column=i, padx=2, pady=2)
            Label(stats_frame, text=text, font=('Arial', 12, 'bold'), bg='white').grid(row=0, column=i)
            Label(stats_frame, textvariable=var, font=('Arial', 14), bg='white').grid(row=1, column=i)

        buttons_frame = Frame(main_frame, bg='#f0f0f0')
        buttons_frame.pack(fill=X)

        button_style = {'font': ('Arial', 12), 'width': 10, 'bg': '#4CAF50', 'fg': 'white',
                        'activebackground': '#45a049'}

        Button(buttons_frame, text="ADD", command=self.open_add_window, **button_style).pack(side=LEFT, padx=5)
        Button(buttons_frame, text="UPDATE", command=self.open_update_window, **button_style).pack(side=LEFT, padx=5)
        Button(buttons_frame, text="DELETE", command=self.open_delete_window, **button_style).pack(side=LEFT, padx=5)

        self.update_statistics()

    def update_statistics(self):
        try:
            logging.info("Updating statistics...")

            # Fetch total pages
            response = self.make_request("GET", f"{self.graph_endpoint}/{GRAPH_ID}")
            response_text = response.text
            logging.debug(f"API Response: {response_text}")

            try:
                graph_data = response.json()
                self.total_pages.set(graph_data.get('totalQuantity', '0'))
                logging.info(f"Total pages set to: {self.total_pages.get()}")
            except json.JSONDecodeError:
                logging.error(f"Failed to parse JSON from API response: {response_text}")
                self.total_pages.set("Error")

            # Calculate average pages
            today = datetime.now().date()
            start_date = (today - timedelta(days=30)).strftime("%Y%m%d")
            end_date = today.strftime("%Y%m%d")
            response = self.make_request("GET", f"{self.pixel_endpoint}?from={start_date}&to={end_date}")
            response_text = response.text
            logging.debug(f"API Response: {response_text}")

            try:
                pixels_data = response.json()
                pixels = pixels_data.get('pixels', [])
                if pixels:
                    avg = sum(int(pixel['quantity']) for pixel in pixels) / len(pixels)
                    self.avg_pages.set(f"{avg:.1f}")
                else:
                    self.avg_pages.set("0.0")
                logging.info(f"Average pages set to: {self.avg_pages.get()}")
            except json.JSONDecodeError:
                logging.error(f"Failed to parse JSON from API response: {response_text}")
                self.avg_pages.set("Error")

            # Fetch today's pages
            today_date = today.strftime("%Y%m%d")
            response = self.make_request("GET", f"{self.pixel_endpoint}/{today_date}")
            response_text = response.text
            logging.debug(f"API Response: {response_text}")

            try:
                if response.status_code == 200:
                    today_data = response.json()
                    self.today_pages.set(today_data.get('quantity', '0'))
                elif response.status_code == 404:
                    self.today_pages.set("0")
                else:
                    response.raise_for_status()
                logging.info(f"Today's pages set to: {self.today_pages.get()}")
            except json.JSONDecodeError:
                logging.error(f"Failed to parse JSON from API response: {response_text}")
                self.today_pages.set("Error")

        except requests.exceptions.RequestException as e:
            error_message = f"Failed to update statistics: {str(e)}"
            logging.error(error_message, exc_info=True)
            messagebox.showerror("Error", error_message)
        except Exception as e:
            error_message = f"An unexpected error occurred: {str(e)}"
            logging.error(error_message, exc_info=True)
            messagebox.showerror("Error", error_message)

    def make_request(self, method, url, json=None):
        try:
            response = requests.request(method, url, headers=self.headers, json=json)
            response.raise_for_status()
            return response
        except requests.RequestException as e:
            logging.error(f"Request failed: {str(e)}", exc_info=True)
            raise

    def open_add_window(self):
        add_window = Toplevel(self.root)
        add_window.title("Add New Pixel")
        add_window.geometry("300x300")
        add_window.configure(bg='#f0f0f0')

        frame = Frame(add_window, padx=20, pady=20, bg='#f0f0f0')
        frame.pack(fill=BOTH, expand=True)

        cal = Calendar(frame, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=10)

        pages_frame = Frame(frame, bg='#f0f0f0')
        pages_frame.pack(fill=X, pady=10)
        Label(pages_frame, text="Pages:", bg='#f0f0f0', font=('Arial', 12)).pack(side=LEFT)
        pages_entry = Entry(pages_frame, width=5, font=('Arial', 12))
        pages_entry.pack(side=LEFT, padx=5)

        Button(frame, text="ADD", command=lambda: self.add_pixel(cal.get_date(), pages_entry.get(), add_window),
               bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)

    def open_update_window(self):
        update_window = Toplevel(self.root)
        update_window.title("Update Pixel")
        update_window.geometry("300x300")
        update_window.configure(bg='#f0f0f0')

        frame = Frame(update_window, padx=20, pady=20, bg='#f0f0f0')
        frame.pack(fill=BOTH, expand=True)

        cal = Calendar(frame, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=10)

        pages_frame = Frame(frame, bg='#f0f0f0')
        pages_frame.pack(fill=X, pady=10)
        Label(pages_frame, text="Pages:", bg='#f0f0f0', font=('Arial', 12)).pack(side=LEFT)
        pages_entry = Entry(pages_frame, width=5, font=('Arial', 12))
        pages_entry.pack(side=LEFT, padx=5)

        Button(frame, text="UPDATE",
               command=lambda: self.update_pixel(cal.get_date(), pages_entry.get(), update_window),
               bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)

    def open_delete_window(self):
        delete_window = Toplevel(self.root)
        delete_window.title("Delete Pixel")
        delete_window.geometry("300x250")
        delete_window.configure(bg='#f0f0f0')

        frame = Frame(delete_window, padx=20, pady=20, bg='#f0f0f0')
        frame.pack(fill=BOTH, expand=True)

        cal = Calendar(frame, selectmode='day', date_pattern='yyyy-mm-dd')
        cal.pack(pady=10)

        Button(frame, text="DELETE", command=lambda: self.delete_pixel(cal.get_date(), delete_window),
               bg='#4CAF50', fg='white', font=('Arial', 12)).pack(pady=10)

    def add_pixel(self, date, quantity, window):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            pixel_data = {
                "date": date_obj.strftime("%Y%m%d"),
                "quantity": quantity,
            }

            # Check if pixel already exists for today
            response = self.make_request("GET", f"{self.pixel_endpoint}/{pixel_data['date']}")
            if response.status_code == 200:
                messagebox.showinfo("Info", "You've already read some pages today. Please use the update function.")
            else:
                self.make_request("POST", self.pixel_endpoint, json=pixel_data)
                messagebox.showinfo("Success", "Pixel added successfully!")
                window.destroy()
                self.update_statistics()
        except Exception as e:
            error_message = f"Failed to add pixel: {str(e)}"
            logging.error(error_message, exc_info=True)
            messagebox.showerror("Error", error_message)

    def update_pixel(self, date, quantity, window):
        try:
            date_obj = datetime.strptime(date, "%Y-%m-%d")
            pixel_data = {
                "quantity": quantity,
            }
            update_endpoint = f"{self.pixel_endpoint}/{date_obj.strftime('%Y%m%d')}"

            # Check if pixel exists for the given date
            response = self.make_request("GET", update_endpoint)
            if response.status_code == 404:
                messagebox.showinfo("Info", f"You haven't read any pages on {date}. Please use the add function.")
            else:
                self.make_request("PUT", update_endpoint, json=pixel_data)
                messagebox.showinfo("Success", "Pixel updated successfully!")
                window.destroy()
                self.update_statistics()
        except Exception as e:
            error_message = f"Failed to update pixel: {str(e)}"
            logging.error(error_message, exc_info=True)
            messagebox.showerror("Error", error_message)

    def delete_pixel(self, date, window):
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        delete_date = date_obj.strftime("%Y%m%d")
        if messagebox.askyesno("Confirm", f"Do you want to delete the pixel for {date}?"):
            try:
                delete_endpoint = f"{self.pixel_endpoint}/{delete_date}"

                # Check if pixel exists for the given date
                response = self.make_request("GET", delete_endpoint)
                if response.status_code == 404:
                    messagebox.showinfo("Info", f"There is no pixel to delete for {date}.")
                else:
                    self.make_request("DELETE", delete_endpoint)
                    messagebox.showinfo("Success", "Pixel deleted successfully!")
                    window.destroy()
                    self.update_statistics()
            except Exception as e:
                error_message = f"Failed to delete pixel: {str(e)}"
                logging.error(error_message, exc_info=True)
                messagebox.showerror("Error", error_message)

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = HabitTracker()
    app.run()