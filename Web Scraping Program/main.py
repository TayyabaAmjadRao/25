import streamlit as st
import requests
from bs4 import BeautifulSoup as bs

# Streamlit App Title
st.title("GitHub Profile Image Scraper")

# Input field for GitHub username
github_user = st.text_input("Enter GitHub Username:")

# Button to fetch profile image
if st.button("Get Profile Image"):
    if github_user:
        try:
            url = f'https://github.com/{github_user}'
            headers = {'User-Agent': 'Mozilla/5.0'}
            r = requests.get(url, headers=headers)

            if r.status_code == 200:
                soup = bs(r.content, 'html.parser')
                profile_img_tag = soup.find('img', {'alt': f'@{github_user}'})

                if profile_img_tag:
                    profile_image = profile_img_tag['src']
                    
                    # Convert the low-resolution URL to high-resolution
                    if profile_image.startswith("https://avatars.githubusercontent.com/"):
                        profile_image = profile_image.split("?")[0] + "?s=400"  # Fetching High-Res Image

                    st.image(profile_image, caption=f"{github_user}'s Profile Picture", use_container_width=True)
                else:
                    st.error("Profile image not found. Please check the username.")
            else:
                st.error("Invalid GitHub user or network error.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a GitHub username.")

# Footer
st.markdown("---")
st.markdown("Developed by **SABAHAT**")
