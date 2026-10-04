from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
<!DOCTYPE html>
<html lang="my">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#111111">
    <title>Myanmar Recap AI</title>

    <style>
        body {
            margin: 0;
            padding: 20px;
            background: #111;
            color: white;
            font-family: Arial, sans-serif;
        }

        .box {
            max-width: 600px;
            margin: auto;
            padding: 25px;
            background: #1c1c1c;
            border-radius: 18px;
        }

        h1 {
            text-align: center;
        }

        p {
            color: #bbb;
            text-align: center;
        }

        input {
            width: 100%;
            margin-top: 20px;
            padding: 14px;
            box-sizing: border-box;
            border-radius: 10px;
            background: #292929;
            color: white;
            border: 1px solid #444;
        }

        button {
            width: 100%;
            margin-top: 15px;
            padding: 15px;
            border: 0;
            border-radius: 10px;
            background: #4f8cff;
            color: white;
            font-size: 17px;
        }

        #status {
            margin-top: 20px;
            text-align: center;
            color: #aaa;
        }
    </style>
</head>

<body>

<div class="box">
    <h1>🇲🇲 Myanmar Recap AI</h1>

    <p>
        Chinese Video → Myanmar Voice Recap
    </p>

    <input type="file" accept="video/*">

    <button onclick="startRecap()">
        🎬 Recap စတင်မယ်
    </button>

    <div id="status">
        Video ရွေးပြီး Recap စတင်ပါ။
    </div>
</div>

<script>
function startRecap() {
    document.getElementById("status").innerText =
        "⏳ Video ကို လုပ်ဆောင်ရန် ပြင်ဆင်နေပါတယ်...";
}
</script>

</body>
</html>
"""