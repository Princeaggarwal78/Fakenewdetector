document.addEventListener("DOMContentLoaded", function () {
    document.querySelector("form").addEventListener("submit", function (event) {
        event.preventDefault();  

        let newsText = document.getElementById("news").value;  

        if (newsText.trim() === "") {
            alert("Please enter some news text.");
            return;
        }

 
        fetch("/predict", {
            method: "POST",
            body: new URLSearchParams({ "news": newsText }),
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        })
        .then(response => response.json())  // 🔥 JSON response parse kar raha hai
        .then(data => {
            let resultDiv = document.getElementById("page");

            // 🔥 🔥 🔥 FIX: Pehle se existing result ko hatao
            let existingOutput = document.getElementById("prediction-result");
            if (existingOutput) {
                existingOutput.remove();
            }

            // 🔥 Naya h2 element create karo
            let output = document.createElement("h2");
            output.id = "prediction-result";  // ID set kar diya taaki baar-baar repeat na ho
            output.innerText = "Prediction: " + data.prediction;
            output.style.color = data.prediction === "Fake News" ? "red" : "green"; // 🔥 Fake ke liye red, real ke liye green
            resultDiv.appendChild(output);
        })
        .catch(error => {
            alert("Error: " + error);
        });
    });
});
