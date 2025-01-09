document.getElementById('ad-form').addEventListener('submit', function(event) {
    const phoneInput = document.getElementById('phone');
    const phoneValue = phoneInput.value;

    // Telefon nömrəsi formatı üçün müntəzəm ifadə (regex)
    const phonePattern = /^\d{3}\d{3}\d{2}\d{2}$/;

    if (!phonePattern.test(phoneValue)) {
        alert('Zəhmət olmasa, telefon nömrəsini düzgün formatda daxil edin (0001112233).');
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
