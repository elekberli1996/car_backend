document.getElementById("ad-form").addEventListener("submit", function (event) {
  const phoneInput = document.getElementById("phone");
  const phoneValue = phoneInput.value;

  // Telefon nömrəsi formatı üçün müntəzəm ifadə (regex)
  const phonePattern = /^\d{3}\d{3}\d{2}\d{2}$/;

  if (!phonePattern.test(phoneValue)) {
    alert(
      "Zəhmət olmasa, telefon nömrəsini düzgün formatda daxil edin (0001112233)."
    );
    event.preventDefault(); // Formun göndərilməsinin qarşısını alır
  }
});

// document.getElementById('additional-images').addEventListener('change', function(event) {
//     const files = event.target.files;
//     const previewContainer = document.createElement('div');
//     previewContainer.classList.add('preview-container');

//     Array.from(files).forEach(file => {
//         const reader = new FileReader();
//         reader.onload = function(e) {
//             const img = document.createElement('img');
//             img.src = e.target.result;
//             img.classList.add('preview-image');
//             previewContainer.appendChild(img);
//         };
//         reader.readAsDataURL(file);
//     });

//     document.body.appendChild(previewContainer);
// });

var url = "http://127.0.0.1:8000/api/cars/brands/";
document.getElementById("brand").addEventListener("change", function () {
  const brandId = this.value;
  console.log(brandId);

  const modelSelect = document.getElementById("model");

  modelSelect.innerHTML = '<option value="">Seçin</option>';

  if (brandId) {
    fetch(`${url}${brandId}/models/`, { method: "GET" })
      .then((response) => response.json())
      .then((models) => {
        console.log(models); // API'den gelen veriyi konsola yazdırın

        // Burada models'in bir dizi olduğundan emin olun
        if (Array.isArray(models)) {
          models.forEach((model) => {
            const option = document.createElement("option");
            option.value = model.id; // Modelin ID'sini değere ekleyin
            option.textContent = model.name; // Modelin adını metin olarak ekleyin
            modelSelect.appendChild(option);
          });
        } else {
          console.error("Beklenen formatta veri gelmedi.");
        }
      })
      .catch((error) => {
        console.error("Bir hata oluştu:", error);
      });
  }
});
