
import streamlit as st
from gtts import gTTS
import base64
import tempfile

st.set_page_config(page_title="يلا نذاكر بذكاء!", page_icon="📘")
st.title("📘 يلا نذاكر بذكاء!")

st.markdown("ضع نص الدرس أو انسخ الكلام من فيديو يوتيوب:")
lesson_text = st.text_area("نص الدرس هنا:")

if st.button("ابدأ الدرس 📚"):
    if not lesson_text.strip():
        st.warning("من فضلك اكتب أو انسخ نص الدرس أولًا!")
    else:
        explain = f"الدرس بيتكلم عن: {lesson_text[:150]} ... وبطريقة مبسطة نفهم إن الفكرة الأساسية هي المعلومات المهمة اللي اتقالت في الدرس."
        st.subheader("🧠 الشرح")
        st.write(explain)

        tts = gTTS(text=explain, lang="ar")
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tts.save(f"{tfile.name}.mp3")
        audio_file = open(f"{tfile.name}.mp3", "rb").read()
        st.audio(audio_file, format="audio/mp3")

        summary = f"{lesson_text[:120]} ... (ده ملخص سريع للدرس)"
        st.subheader("📝 الملخص")
        st.write(summary)

        st.subheader("❓ الأسئلة")
        st.write("""1) إيه أهم حاجة اتقالت في الدرس؟  
2) صح ولا غلط: الدرس اتكلم عن حاجة مهمة؟  
3) اذكر معلومة استفدتها من الدرس؟  
4) لو كنت المدرس هتشرح الدرس ازاي؟  
**الإجابات:** حسب الدرس أو فهمك.""")

st.markdown("---")
st.markdown("✨ واجهة مصممة للأطفال مع ألوان جذابة وأزرار واضحة")
