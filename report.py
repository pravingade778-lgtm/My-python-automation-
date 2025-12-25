# ==========================================
# Project: Automated Business Intelligence Tool
# Developer: Pravin
# GitHub: https://github.com/तुझं-युजरनेम
# ==========================================

import datetime
import os

def run_project():
    print("--- PRAVIN'S AUTOMATION ENGINE STARTING ---")
    
    # User inputs for dynamic reporting
    client = input("Enter Client Name: ")
    task = input("Enter Task Description: ")
    
    # Logic to create HTML content
    html_data = f"""
    <html>
    <body style="font-family: Arial; padding: 40px; background: #f4f4f4;">
        <div style="background: white; padding: 20px; border-radius: 10px; border-top: 5px solid blue;">
            <h1>Automated Project Report</h1>
            <p><b>Analyst:</b> Pravin</p>
            <p><b>Client:</b> {client}</p>
            <p><b>Task:</b> {task}</p>
            <p><b>Date:</b> {datetime.date.today()}</p>
            <hr>
            <p style="color: green;">✔ Status: Processed Successfully</p>
        </div>
    </body>
    </html>
    """
    
    # Save file
    file_name = "Professional_Report.html"
    with open(file_name, "w") as f:
        f.write(html_data)
        
    print(f"REPORT GENERATED: {file_name}")

if __name__ == "__main__":
    run_project()
