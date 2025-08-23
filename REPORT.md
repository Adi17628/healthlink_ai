## 1. Team Information
- *Project Title:* HealthLink AI – Bringing Health Guidance to Every Corner of India
- *Team Members:*
  1. (shahirshaik)
  2. [adityaannamdevula] 
  3. [mokshagyna] 
  4. [Subhash017] 
  5. [Bukkebharathnaik123] 

---

## 2. Application Overview

### Why We Built This
In many parts of India, especially in rural and low-bandwidth areas, quick and reliable health guidance is hard to access. Most AI health assistants require fast internet, are only in English, or feel complicated to use.  

We wanted to change that.  

Our mission was simple: *create a lightweight, multilingual, AI-powered health assistant that works even when internet is slow. And so, **HealthLink AI* was born.

### What It Does
HealthLink AI lets anyone:
- Ask about symptoms and get *first-aid steps, **home remedies, and **doctor warning signs*.
- Enter a medicine name and get *simple explanations, **uses, and **safety tips*.
- Upload a medical image (like a rash or wound) and get *AI-powered analysis*.

It’s designed to be *fast, clear, and friendly* — like talking to a caring community health worker, but on your phone.

---

## 3. AI Integration

We integrated *Google Gemini gemini-2.5-flash* to power both text and image understanding.  

The AI:
- Detects if a query is about *symptoms* or *medicine*.
- Responds in *150–200 words*, using bullet points, emojis, and simple language.
- Always ends with a *safety disclaimer* so users remember to consult a doctor.

For images, the AI can describe possible conditions, explain what to watch out for, and suggest safe next steps.

---

## 4. How We Built It (Technical Flow)

- *Front-End:* Streamlit for speed and ease of deployment.
- *Design:* Custom CSS for a clean, mobile-friendly UI.
- *Core Tabs:*
  - 💬 Text Query
  - 📸 Image Analysis
- *Caching:* We used @st.cache_resource so the AI client is always ready without delays.
- *Image Handling:* Compressed before sending to the AI to save bandwidth.
- *Offline-First Approach:*  
  - Minimal assets
  - Optimized loading
  - No heavy scripts

---

## 5. Week 2 – Testing with Real People

We didn’t want to just guess if it works — we wanted real feedback.  

So we reached out to:
- Student groups

We asked them to try both *text* and *image analysis*.  

*What they loved:*
- “Feels like I’m talking to a real helper”
- Easy to understand
- Image feature is exciting

*What they wanted improved:*
- More local language support
- Faster image uploads

We listened.  
We compressed images, improved speed, and made the disclaimers even clearer.

---

## 6. Our 4-Week Journey

### Week 1 – Building the MVP
We had *7 days*. That meant no fluff — just the essential features:
- Text query handling for symptoms & medicines
- Image upload & analysis
- Custom AI prompt
- Deployed to Hugging Face Spaces

We ended the week with a working MVP and a sense of “Wow, we actually pulled it off.”

---

### Week 2 – Testing & Iterating
We tested with 5 people.  

---

### Weeks 3–4 – Growing Our Users
Our goal wasn’t just to make the app — it was to *get it into people’s hands*.  

We targeted:
- Students
- Local WhatsApp groups

*Our message:*  
"Health help that fits in your pocket – even with slow internet."


---

## 7. The Road Ahead

We’re just getting started.  

*Next Goals:*
- Support 10+ Indian languages
- Add voice-based queries
- Use fully open-source AI models
- Build a volunteer translator community

*Sustainability Plan:*
- Keep it open-source
- Partner with NGOs for rural outreach
- Explore integration with government health programs

---

## 8. Links
- *Live App:* [https://huggingface.co/spaces/Adi222111/healthlink_ai]

---

*Final Note:*  
HealthLink AI is more than just an app — it’s a small step toward making health guidance accessible for everyone, everywhere.