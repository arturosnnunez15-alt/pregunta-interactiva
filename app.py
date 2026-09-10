import os
from flask import Flask, render_template_string

app = Flask(__name__)

HTML_CODE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pregunta de investigación ✨</title>
    <style>
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #ffe6eb;
            font-family: 'Arial', sans-serif;
            overflow: hidden;
            text-align: center;
        }
        h1 { color: #d63384; font-size: 1.8rem; margin-bottom: 30px; padding: 0 20px; }
        .btn-container { position: relative; width: 300px; height: 150px; }
        button {
            padding: 12px 25px;
            font-size: 1.2rem;
            font-weight: bold;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            position: absolute;
            transition: all 0.15s ease;
        }
        #btn-si { background-color: #28a745; color: white; left: 20px; }
        #btn-no { background-color: #dc3545; color: white; right: 20px; }
        
        .heart {
            position: fixed;
            font-size: 2rem;
            animation: float 3s linear infinite;
            opacity: 0;
        }
        @keyframes float {
            0% { transform: translateY(100vh) scale(0.5); opacity: 1; }
            100% { transform: translateY(-10vh) scale(1.2); opacity: 0; }
        }
    </style>
</head>
<body>

    <div id="main-card">
        <h1>¿Estás pensando en mí? 😉</h1>
        <div class="btn-container">
            <button id="btn-si" onclick="aceptar()">SÍ</button>
            <button id="btn-no" onmouseover="moverBoton()" onclick="moverBoton()" ontouchstart="moverBoton()">NO</button>
        </div>
    </div>

    <script>
        function moverBoton() {
            const btnNo = document.getElementById('btn-no');
            const x = Math.random() * (window.innerWidth - 120);
            const y = Math.random() * (window.innerHeight - 60);
            btnNo.style.position = 'fixed';
            btnNo.style.left = x + 'px';
            btnNo.style.top = y + 'px';
        }

        function aceptar() {
            document.getElementById('main-card').innerHTML = "<h1>¡Sabía que la respuesta era esa! ❤️✨</h1>";
            lanzarCorazones();
            
            setTimeout(() => {
                // Abre WhatsApp con el mensaje listo para enviarte
                window.location.href = "https://wa.me/595962125194?text=%C2%A1Confieso%20que%20s%C3%AD%20estoy%20pensando%20en%20vos!%20%F0%9F%92%96";
            }, 2200);
        }

        function lanzarCorazones() {
            for (let i = 0; i < 35; i++) {
                setTimeout(() => {
                    const heart = document.createElement('div');
                    heart.classList.add('heart');
                    heart.innerHTML = '❤️';
                    heart.style.left = Math.random() * 100 + 'vw';
                    heart.style.animationDuration = (Math.random() * 2 + 2) + 's';
                    document.body.appendChild(heart);
                }, i * 80);
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_CODE)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
