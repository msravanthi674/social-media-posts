# app.py

import streamlit as st # type: ignore
from src.generator import generate_post

# ------------------ Streamlit App ------------------ #

st.set_page_config(
    page_title="AI Social Media Post Generator",
    page_icon="✨",
    layout="centered"
)

st.title("✨ AI-Powered Social Media Post Generator")
st.write("Generate engaging posts from long-form content using **Mistral AI**.")

# Sidebar settings
st.sidebar.header("⚙️ Settings")

platforms = st.sidebar.multiselect(
    "Select Platforms",
    ["Twitter", "LinkedIn", "Instagram", "Facebook"],
    default=["Twitter", "LinkedIn"]
)

tone = st.sidebar.selectbox(
    "Select Tone",
    ["default", "professional", "casual", "funny", "inspirational"],
    index=0
)

length = st.sidebar.selectbox(
    "Select Post Length",
    ["short", "medium", "long"],
    index=1
)

temperature = st.sidebar.slider(
    "Creativity (Temperature)",
    0.1, 1.0, 0.7
)

# Input text
st.subheader("📄 Paste your blog/article text")
blog_text = st.text_area("Input", height=200, placeholder="Paste your article, blog, or long-form content here...")

# Generate posts
if st.button("🚀 Generate Posts"):
    if not blog_text.strip():
        st.warning("⚠️ Please enter some text before generating posts.")
    else:
        results = {}
        with st.spinner("Generating posts with Mistral AI..."):
            for platform in platforms:
                post = generate_post(
                    long_form_text=blog_text,
                    platform=platform,
                    tone=tone,
                    length=length,
                    temperature=temperature
                )
                results[platform] = post

        st.success("✅ Posts generated successfully!")

        # Display results
        for platform, post in results.items():
            st.subheader(f"📌 {platform}")
            st.write(post)

        # Prepare TXT output
        output_text = ""
        for platform, post in results.items():
            output_text += f"--- {platform} ---\n{post}\n\n"

        # Download button
        st.download_button(
            label="📥 Download Posts as TXT",
            data=output_text,
            file_name="social_posts.txt",
            mime="text/plain"
        )
