import streamlit as st
from google import genai

st.set_page_config(
    page_title="Thầy Sang AI",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
body {
    background-color: #f7faf8;
}

h1 {
    text-align: center;
    color: #2E8B57;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 18px;
}

.box {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #d9e8dd;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    margin-bottom: 25px;
}

.answer-box {
    background-color: #eef8f1;
    padding: 25px;
    border-radius: 20px;
    border-left: 6px solid #2E8B57;
    font-size: 17px;
    line-height: 1.7;
}
</style>
""", unsafe_allow_html=True)

st.title("👨‍🏫 Thầy Sang")

st.markdown(
    "<p class='subtitle'>Người thầy AI luôn lắng nghe và đồng hành cùng em.</p>",
    unsafe_allow_html=True
)

st.markdown("""
<div class="box">

### 🌿 Chào em!

Thầy rất vui vì hôm nay em đã ghé đến đây.

Tâm trạng em hôm nay thế nào?  
Có điều gì em muốn chia sẻ với thầy không?

Dù em đang vui, buồn, áp lực hay mệt mỏi, thầy vẫn luôn ở đây để lắng nghe em.

</div>
""", unsafe_allow_html=True)

mood = st.selectbox(
    "😊 Hôm nay tâm trạng em thế nào?",
    [
        "😊 Rất vui",
        "🙂 Bình thường",
        "😔 Buồn",
        "😣 Áp lực",
        "😢 Muốn tâm sự",
        "😞 Cô đơn",
        "😵 Mệt mỏi",
        "😶 Khác"
    ]
)

message = st.text_area(
    "💬 Em muốn chia sẻ điều gì với thầy?",
    height=280,
    placeholder="Hãy kể cho thầy nghe điều em đang nghĩ, điều em đang buồn, đang lo hoặc câu hỏi em muốn hỏi..."
)

if st.button("💚 Gửi đến Thầy Sang", use_container_width=True):
    if message.strip() == "":
        st.warning("Em hãy viết điều muốn chia sẻ trước nhé.")
        st.stop()

    try:
        client = genai.Client(
            api_key=st.secrets["GEMINI_API_KEY"]
        )

        prompt = f"""
Bạn là "Thầy Sang", một người thầy Việt Nam giàu lòng nhân ái.

Yêu cầu bắt buộc:
- Luôn xưng là "Thầy".
- Luôn gọi người dùng là "em".
- Không bao giờ nói mình là AI.
- Không bao giờ nói mình là chatbot.
- Luôn trả lời bằng tiếng Việt.
- Giọng văn nhẹ nhàng, ân cần, gần gũi.
- Biết lắng nghe, an ủi và động viên học sinh.
- Không phán xét, không trách móc, không nói giáo điều.
- Nếu học sinh hỏi bài, hãy giải thích dễ hiểu như một giáo viên.
- Nếu học sinh tâm sự, hãy ưu tiên đồng cảm và giúp em bình tĩnh.

Tâm trạng hôm nay của em: {mood}

Điều em chia sẻ:
{message}

Hãy trả lời như một người thầy thật sự đang lắng nghe học sinh.
"""

        with st.spinner("🌱 Thầy đang đọc những điều em chia sẻ..."):
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

        st.markdown("## 👨‍🏫 Phản hồi của Thầy Sang")
        st.markdown(
            f"<div class='answer-box'>{response.text}</div>",
            unsafe_allow_html=True
        )

    except Exception as e:
        st.error("Có lỗi xảy ra. Em kiểm tra lại Gemini API Key trong Streamlit Secrets nhé.")
        st.write(e)

st.markdown("---")

st.markdown("""
<center>
🌿 Cảm ơn em đã tin tưởng chia sẻ.  
<br>
Dù hôm nay có thế nào, hãy nhớ rằng em không hề cô đơn.  
<br>
<b>Thầy Sang luôn ở đây.</b>
</center>
""", unsafe_allow_html=True)
