build:
	pyinstaller --onefile --noconsole --icon=app.ico main.py --add-data "resources/*:resources"