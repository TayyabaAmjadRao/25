import streamlit as st
import os
from PIL import Image
import pytesseract

# Ensure the 'covers' directory exists
covers_dir = "covers"
if not os.path.exists(covers_dir):
    os.makedirs(covers_dir)

# Set Tesseract OCR path (update this based on your system)
# Example for Windows: "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Streamlit UI
st.title("📚 Personal Library Manager")

# Upload Book Cover
st.subheader("Upload Book Cover")
cover_image = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])

if cover_image:
    # Open the image
    img = Image.open(cover_image)
    
    # Display the uploaded image
    st.image(img, caption="Uploaded Cover", use_column_width=True)
    
    # Save the image
    image_path = os.path.join(covers_dir, cover_image.name)
    img.save(image_path)
    st.success(f"Image saved as: {image_path}")

    # Extract text from image using OCR
    st.subheader("Extracted Text from Cover")
    extracted_text = pytesseract.image_to_string(img)
    st.text_area("OCR Output", extracted_text, height=150)

st.write("---")

# Book Details Section
st.subheader("📖 Enter Book Details")
book_title = st.text_input("Book Title")
author = st.text_input("Author")
publication_year = st.number_input("Publication Year", min_value=1500, max_value=2100, step=1)
isbn = st.text_input("ISBN")

# Save Book Info
if st.button("Save Book"):
    if book_title and author and publication_year and isbn:
        book_data = f"{book_title}, {author}, {publication_year}, {isbn}, {image_path if cover_image else 'No Cover'}\n"
        
        # Save book details
        with open("library_records.txt", "a") as file:
            file.write(book_data)

        st.success("📚 Book details saved successfully!")
    else:
        st.warning("⚠️ Please fill in all fields before saving!")

# Show saved books
st.subheader("📜 Library Records")
if os.path.exists("library_records.txt"):
    with open("library_records.txt", "r") as file:
        records = file.readlines()
        for record in records:
            st.write(record.strip())
else:
    st.write("No books added yet.")

