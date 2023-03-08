import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme("DarkTeal10")

label1 = sg.Text("Select archive:")
input1 = sg.Input(key="archive_input")
choose_button1 = sg.FilesBrowse("Choose", key="archive_browse")

label2 = sg.Text("Select location:")
input2 = sg.Input(key="folder_input")
choose_button2 = sg.FolderBrowse("Choose", key="folder_browse")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="white")

exit_button = sg.Button("Exit", button_color="tomato")

col_1 = sg.Column([[label1], [label2]])
col_2 = sg.Column([[input1, choose_button1], [input2, choose_button2]])
layout = [[col_1, col_2], [extract_button, exit_button, output_label]]
window = sg.Window("Zip File Extractor", layout, use_custom_titlebar=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, "Exit"):  # If user closes window or clicks exit
        break
    if event == "archive_browse":
        window["archive_input"].update(value=values["archive_browse"])
    elif event == "folder_browse":
        window["folder_input"].update(value=values["folder_browse"])
    elif event == "Extract":
        archivepath = values["archive_input"]
        dest_dir = values["folder_input"]
        extract_archive(archivepath, dest_dir)
        window["output"].update(value="File extraction has now been completed")

window.close()
