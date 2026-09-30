import streamlit as st
import time

from rag_pipeline import build_chain


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Shruti Telecom",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CSS — DARK SCI-FI HOLOGRAPHIC UI
# ============================================================

st.markdown("""
<style>

/* =========================================================
   GLOBAL APP BACKGROUND
========================================================= */

.stApp {

    background:
        radial-gradient(
            circle at 88% 12%,
            rgba(0, 210, 255, .13),
            transparent 23%
        ),
        radial-gradient(
            circle at 12% 80%,
            rgba(75, 55, 220, .15),
            transparent 28%
        ),
        linear-gradient(
            135deg,
            #020817,
            #031326 45%,
            #06182b 100%
        );

    color: #dbeafe;

    overflow-x: hidden;
}




/* =========================================================
   REMOVE WHITE STREAMLIT AREAS
========================================================= */

header[data-testid="stHeader"] {

    background: transparent !important;

}


[data-testid="stAppViewContainer"] {

    background: transparent !important;

}


[data-testid="stHeader"] {

    background: transparent !important;

}


[data-testid="stBottomBlockContainer"] {

    background: transparent !important;

}


.stBottomBlockContainer {

    background: transparent !important;

}


/* =========================================================
   MAIN CONTAINER
========================================================= */

.block-container {

    background: transparent !important;

    animation:
        pageEnter .7s ease-out;

}


@keyframes pageEnter {

    from {

        opacity: 0;

        transform:
            translateY(15px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


/* =========================================================
   HOLOGRAPHIC BUBBLE 1
========================================================= */

.stApp::before {

    content: "";

    position: fixed;

    width: 390px;
    height: 390px;

    right: 7%;
    top: 25%;

    border-radius: 50%;

    pointer-events: none;

    z-index: 0;

    background:

        radial-gradient(
            circle at 28% 25%,
            rgba(0, 220, 255, .32),
            rgba(36, 99, 235, .22) 35%,
            rgba(124, 58, 237, .17) 60%,
            transparent 76%
        );

    border:
        1px solid rgba(0, 204, 255, .38);

    box-shadow:

        inset 0 0 60px
        rgba(0, 220, 255, .12),

        inset -25px -25px 60px
        rgba(79, 70, 229, .20),

        0 0 80px
        rgba(0, 191, 255, .12);

    animation:
        holoBubbleOne 9s ease-in-out infinite;

}


@keyframes holoBubbleOne {

    0%,100% {

        transform:
            translate3d(0,0,0)
            scale(1);

    }

    25% {

        transform:
            translate3d(-55px,35px,0)
            scale(1.08);

    }

    50% {

        transform:
            translate3d(-20px,100px,0)
            scale(.94);

    }

    75% {

        transform:
            translate3d(55px,55px,0)
            scale(1.06);

    }

}


/* =========================================================
   HOLOGRAPHIC BUBBLE 2
========================================================= */

.stApp::after {

    content: "";

    position: fixed;

    width: 260px;
    height: 260px;

    left: 12%;
    bottom: 5%;

    border-radius: 50%;

    pointer-events: none;

    z-index: 0;

    background:

        radial-gradient(
            circle at 30% 25%,
            rgba(0, 225, 255, .27),
            rgba(59, 130, 246, .18) 38%,
            rgba(124, 58, 237, .18) 65%,
            transparent 78%
        );

    border:
        1px solid rgba(0, 204, 255, .32);

    box-shadow:

        inset 0 0 50px
        rgba(0, 200, 255, .12),

        0 0 70px
        rgba(59, 130, 246, .12);

    animation:
        holoBubbleTwo 10s ease-in-out infinite;

}


@keyframes holoBubbleTwo {

    0%,100% {

        transform:
            translate3d(0,0,0)
            scale(1);

    }

    25% {

        transform:
            translate3d(70px,-40px,0)
            scale(1.12);

    }

    50% {

        transform:
            translate3d(30px,-100px,0)
            scale(.92);

    }

    75% {

        transform:
            translate3d(-65px,-55px,0)
            scale(1.08);

    }

}


/* =========================================================
   EXTRA RIGHT UPPER BUBBLE
========================================================= */

.main::after {

    content: "";

    position: fixed;

    width: 190px;
    height: 190px;

    right: 20%;
    top: 7%;

    border-radius: 50%;

    pointer-events: none;

    z-index: 0;

    background:

        radial-gradient(
            circle at 30% 25%,
            rgba(34, 211, 238, .30),
            rgba(59, 130, 246, .20) 38%,
            rgba(139, 92, 246, .15) 65%,
            transparent 78%
        );

    border:
        1px solid rgba(34, 211, 238, .30);

    box-shadow:

        inset 0 0 40px
        rgba(255,255,255,.05),

        0 0 55px
        rgba(0, 200, 255, .14);

    animation:
        upperBubbleMove 8s ease-in-out infinite;

}


@keyframes upperBubbleMove {

    0%,100% {

        transform:
            translate3d(0,0,0)
            scale(1);

        opacity: .72;

    }

    25% {

        transform:
            translate3d(-55px,30px,0)
            scale(1.12);

        opacity: .9;

    }

    50% {

        transform:
            translate3d(-20px,75px,0)
            scale(.92);

        opacity: .68;

    }

    75% {

        transform:
            translate3d(50px,35px,0)
            scale(1.08);

        opacity: .85;

    }

}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:

        radial-gradient(
            circle at 25% 15%,
            rgba(0, 200, 255, .12),
            transparent 28%
        ),

        linear-gradient(
            180deg,
            #03182b,
            #020d21 65%,
            #09082d
        ) !important;

    border-right:
        1px solid rgba(0, 200, 255, .22);

}


section[data-testid="stSidebar"] * {

    color: #dbeafe;

}


section[data-testid="stSidebar"] hr {

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(0, 210, 255, .28),
            transparent
        );

}


/* =========================================================
   BRAND
========================================================= */

.brand-title {

    font-size: 30px;

    font-weight: 700;

    letter-spacing: -1px;

    color: #e0f2fe;

}


.brand-title span {

    color: #22d3ee;

}


/* =========================================================
   SIGNAL ICON
========================================================= */

.signal-icon {

    font-size: 55px;

    display: inline-block;

    text-shadow:

        0 0 8px
        rgba(34,211,238,.55),

        0 0 22px
        rgba(59,130,246,.45),

        0 0 40px
        rgba(139,92,246,.30);

    animation:
        signalFloat 3s ease-in-out infinite;

}


@keyframes signalFloat {

    0%,100% {

        transform:
            translateY(0)
            rotate(0deg);

    }

    50% {

        transform:
            translateY(-8px)
            rotate(3deg);

    }

}


/* =========================================================
   SIDEBAR BUTTON
========================================================= */

section[data-testid="stSidebar"] .stButton button {

    background:
        rgba(5, 25, 50, .7);

    border:
        1px solid rgba(34,211,238,.22);

    border-radius: 12px;

}


section[data-testid="stSidebar"] .stButton button:hover {

    border-color:
        rgba(34,211,238,.60);

    box-shadow:
        0 0 22px
        rgba(34,211,238,.16);

}


/* =========================================================
   ONLINE STATUS
========================================================= */

.online-box {

    display: inline-flex;

    align-items: center;

    gap: 9px;

    padding: 9px 17px;

    border-radius: 30px;

    background:
        rgba(0, 220, 255, .07);

    border:
        1px solid rgba(0, 220, 255, .30);

    color: #67e8f9 !important;

    font-weight: 600;

}


.online-dot {

    width: 9px;

    height: 9px;

    border-radius: 50%;

    background: #22d3ee;

    box-shadow:
        0 0 12px
        rgba(34,211,238,.8);

    animation:
        pulse 1.7s infinite;

}


@keyframes pulse {

    0% {

        box-shadow:
            0 0 0 0
            rgba(34,211,238,.6);

    }

    70% {

        box-shadow:
            0 0 0 10px
            rgba(34,211,238,0);

    }

    100% {

        box-shadow:
            0 0 0 0
            rgba(34,211,238,0);

    }

}


/* =========================================================
   HERO
========================================================= */

.hero-label {

    font-size: 13px;

    letter-spacing: 7px;

    font-weight: 700;

    color: #67e8f9;

}


.hero-title {

    font-size:
        clamp(42px, 5vw, 72px);

    font-weight: 700;

    line-height: 1;

    letter-spacing: -3px;

    background:

        linear-gradient(
            90deg,
            #60a5fa,
            #22d3ee,
            #818cf8,
            #60a5fa
        );

    background-size: 300% auto;

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;

    animation:
        gradientMove 6s linear infinite;

}


@keyframes gradientMove {

    0% {

        background-position:
            0% center;

    }

    100% {

        background-position:
            300% center;

    }

}


.hero-description {

    font-size: 18px;

    color: #93c5fd;

    max-width: 700px;

}


.float-card {

    font-size: 55px;

    text-align: center;

    padding-top: 20px;

    animation:
        floating 4s ease-in-out infinite;

    filter:
        drop-shadow(
            0 0 15px
            rgba(34,211,238,.35)
        );

}


@keyframes floating {

    0%,100% {

        transform:
            translateY(0);

    }

    50% {

        transform:
            translateY(-10px);

    }

}


/* =========================================================
   HEADINGS
========================================================= */

h1, h2, h3, h4 {

    color: #dbeafe !important;

}


.stSubheader {

    color: #dbeafe !important;

}


/* =========================================================
   CHAT MESSAGE CONTAINER
   REMOVE BIG BOX/BUBBLE
========================================================= */

[data-testid="stChatMessage"] {

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    animation:
        messageIn .35s ease;

    margin-bottom: 18px;

}


@keyframes messageIn {

    from {

        opacity: 0;

        transform:
            translateY(10px);

    }

    to {

        opacity: 1;

        transform:
            translateY(0);

    }

}


/* =========================================================
   CHAT CONTENT — NO RECTANGULAR BOX
========================================================= */

[data-testid="stChatMessageContent"] {

    background: transparent !important;

    border: none !important;

    box-shadow: none !important;

    border-radius: 0 !important;

    color: #dbeafe !important;

    font-size: 18px !important;

    font-weight: 400 !important;

    line-height: 1.65 !important;

    padding: 8px 4px !important;

}


/* Remove pseudo shine */

[data-testid="stChatMessageContent"]::after {

    display: none !important;

}


/* =========================================================
   CHAT TEXT
========================================================= */

[data-testid="stChatMessageContent"] p {

    color: #dbeafe !important;

    font-size: 18px !important;

    font-weight: 400 !important;

    line-height: 1.65 !important;

}


[data-testid="stChatMessageContent"] strong {

    font-weight: 400 !important;

}


[data-testid="stChatMessageContent"] li {

    color: #dbeafe !important;

    font-size: 18px !important;

    font-weight: 400 !important;

}


/* =========================================================
   USER MESSAGE
========================================================= */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) [data-testid="stChatMessageContent"] {

    color: #e0f2fe !important;

}


[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-user"]
) [data-testid="stChatMessageContent"] p {

    color: #e0f2fe !important;

    font-size: 18px !important;

    font-weight: 400 !important;

}


/* =========================================================
   ASSISTANT MESSAGE
========================================================= */

[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) [data-testid="stChatMessageContent"] {

    color: #dbeafe !important;

}


[data-testid="stChatMessage"]:has(
    [data-testid="chatAvatarIcon-assistant"]
) [data-testid="stChatMessageContent"] p {

    color: #dbeafe !important;

    font-size: 18px !important;

    font-weight: 400 !important;

}


/* =========================================================
   AVATAR
========================================================= */

[data-testid="stChatMessageAvatar"] {

    background:
        rgba(5, 25, 50, .75) !important;

    border:
        1px solid rgba(34,211,238,.25);

    border-radius: 8px !important;

}


/* =========================================================
   CHAT INPUT OUTER AREA
========================================================= */

[data-testid="stChatInput"] {

    background:
        rgba(3, 20, 38, .96) !important;

    border:
        1px solid rgba(34,211,238,.45) !important;

    border-radius: 12px !important;

    padding: 6px !important;

    box-shadow:

        0 0 25px
        rgba(34,211,238,.08),

        inset 0 0 15px
        rgba(0,150,255,.05);

    transition:
        all .3s ease;

}


/* =========================================================
   CHAT INPUT HOVER
========================================================= */

[data-testid="stChatInput"]:hover {

    border-color:
        rgba(34,211,238,.85) !important;

    transform:
        translateY(-3px)
        scale(1.005);

    box-shadow:

        0 0 30px
        rgba(34,211,238,.16),

        0 8px 30px
        rgba(0,0,0,.25);

}


/* =========================================================
   CHAT INPUT FOCUS
========================================================= */

[data-testid="stChatInput"]:focus-within {

    border-color:
        #22d3ee !important;

    transform:
        translateY(-4px)
        scale(1.008);

    box-shadow:

        0 0 35px
        rgba(34,211,238,.22),

        inset 0 0 20px
        rgba(34,211,238,.05);

}


/* =========================================================
   CHAT INPUT TEXTAREA
========================================================= */

[data-testid="stChatInput"] textarea {

    background:
        transparent !important;

    color:
        #111827 !important;

    -webkit-text-fill-color:
        #111827 !important;

    caret-color:
        #111827 !important;

    font-size:
        16px !important;

    font-weight:
        400 !important;

    border:
        none !important;

    outline:
        none !important;

    padding:
        13px 14px !important;

}


/* =========================================================
   INPUT PLACEHOLDER
========================================================= */

[data-testid="stChatInput"] textarea::placeholder {

    color:
        #64748b !important;

    opacity:
        1 !important;

    font-size:
        16px !important;

    font-weight:
        400 !important;

}


/* =========================================================
   SEND BUTTON
========================================================= */

[data-testid="stChatInput"] button {

    background:
        linear-gradient(
            135deg,
            #0891b2,
            #2563eb
        ) !important;

    color:
        white !important;

    border:
        1px solid
        rgba(103,232,249,.45) !important;

    border-radius:
        9px !important;

    transition:
        all .25s ease;

}


[data-testid="stChatInput"] button:hover {

    transform:
        scale(1.08);

    box-shadow:

        0 0 18px
        rgba(34,211,238,.45);

}


/* =========================================================
   REMOVE WHITE BOTTOM BACKGROUND (SEAMLESS)
========================================================= */

[data-testid="stBottom"],
[data-testid="stBottom"] > div,
[data-testid="stBottom"] > div > div,
[data-testid="stBottomBlockContainer"],
[data-testid="stBottomBlockContainer"] > div,
.stBottom,
.stBottom > div,
.stChatFloatingInputContainer {

    background: transparent !important;
    background-color: transparent !important;
    box-shadow: none !important;
    border: none !important;

}

[data-testid="stBottom"]::before,
[data-testid="stBottom"]::after,
.stChatFloatingInputContainer::before,
.stChatFloatingInputContainer::after {

    display: none !important;

}


/* =========================================================
   DIVIDER
========================================================= */

hr {

    border:
        none !important;

    height:
        1px !important;

    background:

        linear-gradient(
            90deg,
            transparent,
            rgba(34,211,238,.30),
            transparent
        ) !important;

}


/* =========================================================
   CAPTION
========================================================= */

.stCaption,
[data-testid="stCaptionContainer"] {

    color:
        #7dd3fc !important;

}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

    .hero-title {

        font-size:
            42px;

    }

    .hero-description {

        font-size:
            16px;

    }

    [data-testid="stChatMessageContent"] p {

        font-size:
            16px !important;

    }

    .main::after {

        width:
            120px;

        height:
            120px;

    }

}

</style>
""", unsafe_allow_html=True)


# ============================================================
# SESSION STATE
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================================
# LOAD RAG
# ============================================================

@st.cache_resource
def get_chain():

    return build_chain()


chain = get_chain()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        '<div class="signal-icon">📡</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="brand-title">
            Shruti <span>Telecom</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Your Queries. Our Network."
    )

    st.divider()

    st.markdown(
        "### 💬 Ask a Question"
    )

    st.write(
        "Ask anything related to your telecom services."
    )

    st.divider()

    st.markdown(
        """
        <div class="online-box">
            <span class="online-dot"></span>
            RAG Powered
        </div>
        """,
        unsafe_allow_html=True
    )

    st.caption(
        "Accurate • Up-to-date • Reliable"
    )


# ============================================================
# HERO
# ============================================================

left, right = st.columns([4, 1])


with left:

    st.markdown(
        '<div class="hero-label">WELCOME TO</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="hero-title">Shruti Telecom</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-description">
            Instant answers to your telecom-related queries,
            powered by RAG.
        </div>
        """,
        unsafe_allow_html=True
    )


with right:

    st.markdown(
        """
        <div class="float-card">
            📡
        </div>
        """,
        unsafe_allow_html=True
    )


st.divider()


# ============================================================
# CHAT HEADER
# ============================================================

st.subheader(
    "📡 Telecom RAG Assistant"
)

st.caption(
    "Ask your telecom-related question."
)


# ============================================================
# CHAT HISTORY
# ============================================================

for message in st.session_state.messages:

    with st.chat_message(
        message["role"],
        avatar=(
            "👤"
            if message["role"] == "user"
            else "📡"
        )
    ):

        st.write(
            message["content"]
        )


# ============================================================
# CHAT INPUT
# ============================================================

question = st.chat_input(
    "Ask anything about telecom..."
)


# ============================================================
# PROCESS QUESTION
# ============================================================

if question:

    # ========================================================
    # USER MESSAGE
    # ========================================================

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message(
        "user",
        avatar="👤"
    ):

        st.write(question)


    # ========================================================
    # ASSISTANT MESSAGE
    # ========================================================

    with st.chat_message(
        "assistant",
        avatar="📡"
    ):

        with st.spinner(
            "📡 Connecting to telecom knowledge..."
        ):

            try:

                # rag_pipeline.py ka chain
                # direct string question expect karta hai

                result = chain.invoke(question)

                # StrOutputParser ke baad
                # result normally string hota hai

                answer = str(result)


                # =================================================
                # TYPING EFFECT
                # =================================================

                placeholder = st.empty()

                current_text = ""

                for word in answer.split():

                    current_text += word + " "

                    placeholder.write(
                        current_text
                    )

                    time.sleep(0.018)


                # =================================================
                # SAVE ANSWER
                # =================================================

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )


            except Exception as e:

                answer = (
                    "Sorry, I couldn't process "
                    "your question.\n\n"
                    f"Error: {str(e)}"
                )

                st.error(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )