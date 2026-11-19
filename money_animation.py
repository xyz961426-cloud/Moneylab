import streamlit as st
import streamlit.components.v1 as components

def money_transfer(amount=20000, label="Money transferred",
                   sender="Customer", receiver="Bank"):

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    * {{ box-sizing:border-box; }}
    body {{
        margin:0;
        font-family:Arial,sans-serif;
        background:transparent;
    }}
    .box {{
        background:linear-gradient(135deg,#0f172a,#1e293b);
        padding:20px;
        border-radius:20px;
        color:white;
        text-align:center;
        border:1px solid #334155;
    }}
    .people {{
        display:flex;
        justify-content:space-around;
        align-items:center;
        font-size:45px;
    }}
    .person {{
        font-size:14px;
        color:#cbd5e1;
        margin-top:5px;
    }}
    .coin {{
        display:inline-block;
        animation:fly 2s ease-in-out infinite alternate;
    }}
    .arrow {{
        font-size:28px;
        color:#4ade80;
    }}
    .amount {{
        background:linear-gradient(135deg,#064e3b,#065f46);
        padding:18px;
        border-radius:15px;
        margin-top:15px;
        animation:pulse 2s infinite;
    }}
    .value {{
        font-size:30px;
        font-weight:bold;
        color:#86efac;
    }}
    @keyframes fly {{
        from {{transform:translateX(-25px) scale(.8);}}
        to {{transform:translateX(25px) scale(1.1);}}
    }}
    @keyframes pulse {{
        0%,100% {{box-shadow:0 0 5px #22c55e;}}
        50% {{box-shadow:0 0 18px #22c55e;}}
    }}
    </style>
    </head>
    <body>
    <div class="box">
        <div style="font-size:18px;font-weight:bold;margin-bottom:20px;">
            {label}
        </div>
        <div class="people">
            <div>
                <div>👤</div>
                <div class="person">{sender}</div>
            </div>
            <div>
                <div class="coin">🪙</div>
                <div class="arrow">➜</div>
            </div>
            <div>
                <div>🏦</div>
                <div class="person">{receiver}</div>
            </div>
        </div>
        <div class="amount">
            <div class="value">₹{amount:,}</div>
            <div>Money transferred</div>
        </div>
    </div>
    </body>
    </html>
    """

    components.html(html, height=245, scrolling=False)
