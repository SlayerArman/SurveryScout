# Operation Scout

Operation Scout is a simple desktop application I built using Python and Tkinter. It displays basic information about the current computer and allows the information to be copied to the clipboard or exported as a text report.

## Download

If you don't want to install Python or the project dependencies, you can download the standalone Windows executable from the **Releases** page.

1. Go to the **Releases** section of this repository.
2. Download **OperationScout.exe** from the latest release.
3. Double-click the executable to start the application.

## Features

- View computer name
- View current user
- View operating system
- View Python version
- View processor information
- View CPU usage
- View installed memory
- View storage usage
- Refresh displayed information
- Copy system information to the clipboard
- Export a system report to a text file

## Requirements

- Python 3.14+
- psutil

Install the required package with:

```bash
pip install -r requirements.txt
```

## Running the Application

Run the application with:

```bash
python app.py
```

## Project Structure

```text
OperationScout/
│
├── app.py
├── README.md
├── requirements.txt
├── reports/
├── assets/
│   ├── icon.png
│   └── screenshot.png
└── scout/
    ├── report.py
    └── system.py
```

## Screenshot

![Operation Scout](assets/screenshot.png)

## Future Improvements

Some features I'd like to add in the future:

- Display additional system information
- Improve the user interface
- Support exporting reports in different formats
- Add more customization options

## Notes

This project was created as a practice project while learning Python, Tkinter, and working with system information using the `psutil` library.