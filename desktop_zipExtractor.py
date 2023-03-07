import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("DarkTeal10")

label1 = sg.Text("Select archive:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="archive")

label2 = sg.Text("Select location:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

exit_button = sg.Button("Exit", button_color="tomato")

col_1 = sg.Column([[label1], [label2]])
col_2 = sg.Column([[input1], [input2]])
col_3 = sg.Column([[choose_button1], [choose_button2]])

layout = [[col_1, col_2, col_3], [extract_button, exit_button]]
window = sg.Window("Zip File Extractor", layout, use_custom_titlebar=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):  # If user closes window or clicks exit
        break
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extract_archive(archivepath, dest_dir)
    window["output"].update(value="File extraction has now been completed")

window.close()
