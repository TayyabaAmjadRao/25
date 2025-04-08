import os
import shutil  # Import shutil to handle zip operations
import streamlit as st
from pathlib import Path

# Streamlit App Title
st.title("Bulk Image Renamer with Drag & Drop")

# File uploader (Drag & Drop)
uploaded_files = st.file_uploader("Drag and drop images here", type=["jpg", "jpeg", "png"], accept_multiple_files=True)

# Button to rename and save files
if st.button("Rename Images"):
    if uploaded_files:
        renamed_files = []
        output_folder = "renamed_images"

        # Ensure output folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for i, uploaded_file in enumerate(uploaded_files):
            ext = Path(uploaded_file.name).suffix  # Get original file extension
            new_filename = f"image{i}{ext}"  # Rename format

            save_path = os.path.join(output_folder, new_filename)
            with open(save_path, "wb") as f:
                f.write(uploaded_file.read())  # Save the file

            renamed_files.append((uploaded_file.name, new_filename))

        st.success(f"Renamed {len(uploaded_files)} images successfully!")

        # Display renamed files in a table
        st.table(renamed_files)

        # Provide a link to download renamed images
        zip_path = shutil.make_archive("renamed_images", "zip", output_folder)
        with open(zip_path, "rb") as f:
            st.download_button("Download Renamed Images", f, file_name="renamed_images.zip", mime="application/zip")

    else:
        st.warning("Please upload image files first.")

# Footer
st.markdown("---")
st.markdown("Developed by TayyabaRao**")
