# 🏋️‍♂️ FitSheet

Log your workouts straight into Google Sheets because spreadsheets are the *real* fitness trackers.  
This Python script connects the [Nutritionix API](https://developer.nutritionix.com/) with the [Sheety API](https://sheety.co/) to record exercises, duration, and calories burned.  
No fitness app, no ads, just your terminal + a little bit of Python magic.  

---

## 🚀 Features
- Ask once: "What exercise did you do and for how long? (e.g., '30 min running')" → boom, logged.
- Auto-fetches calories + duration from Nutritionix.
- Saves the data neatly into your Google Sheet using Sheety.
- Uses `.env` variables so your secrets stay safe.

---

## 🛠 Setup

1. Clone the repo:
   ```bash
   git clone https://github.com/Unnathie/FitSheet.git
   cd FitSheet
   ```
2. Install dependencies:

   ```bash
   pip install requests python-dotenv
   ```

3. Copy `.env.example` to `.env` and fill in your credentials:

   ```bash
   ID=your_nutritionix_app_id
   KEY=your_nutritionix_app_key
   SHEET_ENDPOINT=your_sheety_endpoint
   USER_NAME=your_username
   PASSWORD=your_password
   ```

4. Run the script:

   ```bash
   python fitsheet.py
   ```

---

## 📊 Example Output

```
What exercise did you do and for how long? (e.g., '30 min running') running 2 hour
{"workout": {"date":"2025-08-26","time":"15:42:10","exercise":"running","duration":120,"calories":462}}
```
<img width="627" height="76" alt="image" src="https://github.com/user-attachments/assets/9455f118-f110-4de6-904a-526985a43b78" />

## 🤓 Why?

Because sometimes the simplest tools are the ones you’ll actually use.
Track your fitness progress in a Google Sheet  automate it later, brag about it forever.

---

## 🧾 License

MIT License. Free to fork, hack, and improve.
