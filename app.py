import streamlit as st
from google import genai

st.set_page_config(
    page_title="Thầy Sang AI",
    page_icon="🌿",
    layout="centered"
)

st.markdown("""
<style>
h1{
    text-align:center;
    color:#2E8B57;
}

.subtitle{
    text-align:center;
    color:#666;
    font-size:18px;
}

.box{
    background:#F7FAF8;
    padding:25px;
    border-radius:20px;
    border:1px solid #d9e8dd;
}
</style>
""", unsafe_allow_html=True)

st.title("👨‍🏫 Thầy Sang")

st.markdown(
    "<p class='subtitle'>Người thầy AI luôn lắng nghe và đồng hành cùng em.</p>",
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='box'>

### 🌿 Chào em!

Thầy rất vui vì hôm nay em đã ghé đến đây.

Có thể hôm nay em đang vui...

Có thể em đang mệt mỏi...

Hay đơn giản chỉ muốn có một người lắng nghe.

Đừng ngại nhé.

💚 Thầy luôn sẵn sàng lắng nghe em.

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
    height=250,
    placeholder="Hãy kể cho thầy nghe..."
)

if st.button("💚 Gửi đến Thầy Sang", use_container_width=True):

    if message.strip() == "":
        st.warning("Em hãy nhập điều muốn chia sẻ nhé.")
        st.stop()

    client = genai.Client(
        api_key=st.secrets["GEMINI_API_KEY"]
    )

    prompt = f"""
Bạn là Thầy Sang.

Luôn xưng Thầy.
Luôn gọi người dùng là em.

Không bao giờ nói mình là AI.

Hãy trả lời nhẹ nhàng, ân cần, động viên.

Tâm trạng của em:
{mood}

Điều em chia sẻ:

{message}
"""

    with st.spinner("🌱 Thầy đang đọc những điều em chia sẻ..."):

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

    st.markdown("## 👨‍🏫 Thầy Sang")

    st.success(response.text)
