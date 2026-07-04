import streamlit as st
from google import genai

st.set_page_config(
    page_title="Thầy Sang AI",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f3fbf6 0%, #e3f4ea 45%, #d7ecdf 100%);
    color: #20352a;
}

.block-container {
    max-width: 900px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.hero {
    background: rgba(255, 255, 255, 0.88);
    border: 1px solid #d8eadf;
    border-radius: 28px;
    padding: 36px 32px;
    text-align: center;
    box-shadow: 0 14px 35px rgba(46, 139, 87, 0.14);
    margin-bottom: 26px;
}

.avatar {
    font-size: 64px;
    margin-bottom: 8px;
}

.hero h1 {
    color: #24734a;
    font-size: 46px;
    margin: 0;
    font-weight: 800;
}

.subtitle {
    color: #496556;
    font-size: 18px;
    margin-top: 10px;
    line-height: 1.6;
}

.greeting-card {
    background: #ffffff;
    border: 1px solid #d8eadf;
    border-radius: 24px;
    padding: 28px;
    box-shadow: 0 10px 26px rgba(46, 139, 87, 0.10);
    margin-bottom: 24px;
    line-height: 1.8;
    font-size: 17px;
}

.greeting-card h3 {
    color: #24734a;
    margin-top: 0;
}

label, .stSelectbox label, .stTextArea label {
    color: #20352a !important;
    font-weight: 700 !important;
    font-size: 16px !important;
}

div[data-baseweb="select"] > div {
    border-radius: 16px;
    border: 1px solid #cfe6d7;
    background-color: #ffffff;
}

textarea {
    border-radius: 18px !important;
    border: 1px solid #cfe6d7 !important;
    background-color: #ffffff !important;
    color: #20352a !important;
    font-size: 16px !important;
}

div.stButton > button {
    background: linear-gradient(135deg, #2e8b57, #3ba66c);
    color: white;
    border: none;
    border-radius: 18px;
    height: 56px;
    font-size: 18px;
    font-weight: 700;
    box-shadow: 0 10px 22px rgba(46, 139, 87, 0.22);
    transition: 0.2s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px);
    background: linear-gradient(135deg, #287a4d, #349761);
    color: white;
}

.answer-box {
    background: #ffffff;
    border-left: 8px solid #2e8b57;
    border-radius: 22px;
    padding: 26px;
    box-shadow: 0 12px 28px rgba(46, 139, 87, 0.12);
    color: #20352a;
    line-height: 1.8;
    font-size: 17px;
    white-space: pre-wrap;
}

.footer {
    text-align: center;
    color: #496556;
    line-height: 1.8;
    margin-top: 32px;
    padding: 20px;
}

hr {
    border: none;
    border-top: 1px solid #cfe6d7;
    margin: 32px 0;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="avatar">👨‍🏫</div>
    <h1>Thầy Sang</h1>
    <div class="subtitle">
        Người thầy AI luôn lắng nghe, đồng hành và giúp em nhẹ lòng hơn mỗi ngày.
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="greeting-card">
    <h3>🌿 Chào em!</h3>
    <p>Thầy rất vui vì hôm nay em đã ghé đến đây.</p>
    <p>Tâm trạng em hôm nay thế nào? Có điều gì em muốn chia sẻ với thầy không?</p>
    <p>Dù em đang vui, buồn, áp lực, mệt mỏi hay chỉ muốn có một người lắng nghe, thầy vẫn luôn ở đây với em.</p>
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
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

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
- Trả lời vừa đủ, không quá dài, lời văn tự nhiên như thầy đang trò chuyện trực tiếp.

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
<div class="footer">
    🌿 Cảm ơn em đã tin tưởng chia sẻ.<br>
    Dù hôm nay có thế nào, hãy nhớ rằng em không hề cô đơn.<br>
    <b>Thầy Sang luôn ở đây.</b>
</div>
""", unsafe_allow_html=True)
