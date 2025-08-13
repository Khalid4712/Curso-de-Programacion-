const pantalla = document.querySelector(".pantalla");
const botones = document.querySelectorAll(".btn");

botones.forEach(boton => {
    boton.addEventListener("click", () => {
        const botonApretado = boton.textContent;

        if(boton.id === "c") {
            pantalla.textContent = "0";
            return;
        }

        if (boton.id === "borrar") {
            if (pantalla.textContent.length === 1 || pantalla.textContent === "ERROR!") {
                pantalla.textContent = "0";
            } else {
                pantalla.textContent = pantalla.textContent.slice(0, -1);
            }
            return;
        }

        if (boton.id === "igual") {
            try {
                let expresion = pantalla.textContent;

                // Reemplazar ^ con ** para que eval() lo entienda
                expresion = expresion.replace(/\^/g, '**');

                let resultado;

                // Manejar las funciones trigonométricas
                if (expresion.includes("sin") || expresion.includes("cos") || expresion.includes("tan")) {
                    // Convertir grados a radianes
                    let valor = parseFloat(expresion.match(/\d+/));
                    if (expresion.includes("sin")) {
                        resultado = Math.sin(valor * Math.PI / 180);
                    } else if (expresion.includes("cos")) {
                        resultado = Math.cos(valor * Math.PI / 180);
                    } else if (expresion.includes("tan")) {
                        resultado = Math.tan(valor * Math.PI / 180);
                    }
                } else if (expresion.includes("√")) {
                    let valor = parseFloat(expresion.replace("√", ""));
                    resultado = Math.sqrt(valor);
                } else if (expresion.includes("%")) {
                    let partes = expresion.split("%");
                    resultado = (eval(partes[0]) / 100) * eval(partes[1] || 1);
                } else {
                    resultado = eval(expresion);
                }

                // Aquí se aplica la reducción de decimales
                // toFixed(5) reduce los decimales a 5. Puedes cambiar el número.
                pantalla.textContent = resultado.toFixed(5); 

            } catch {
                pantalla.textContent = "ERROR!";
            }
            return;
        }

        if(pantalla.textContent === "0" || pantalla.textContent === "ERROR!") {
            pantalla.textContent = botonApretado;
        } else {
            pantalla.textContent += botonApretado;
        }
    })
})