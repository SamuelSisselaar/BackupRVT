# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:21:26 2023

@author: ssi
"""
import os
import shutil
import fnmatch
import streamlit as st

# Display Streamlit UI for input
st.markdown("### Input source folder and move files")

source_folder = st.text_input("Source folder path")
if not source_folder:
    st.warning("Please enter the source folder path.")
    st.stop()

destination_folder = os.path.join(source_folder, "Backup")

# Automatically create the Backup folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

# Loop through files and subfolders in the source folder
for root, dirs, files in os.walk(source_folder):
    for file in files:
        if any(fnmatch.fnmatch(file, pattern) for pattern in ["*00[0-9][0-9].rvt", "*00[0-9][0-9].rfa", "*00[0-9][0-9].rte"]):
            old_path = os.path.join(root, file)
            new_path = os.path.join(destination_folder, file)
            shutil.move(old_path, new_path)

st.success("Files moved successfully.")

