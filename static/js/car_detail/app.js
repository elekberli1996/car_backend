const slides = document.querySelectorAll(".slide");
const thumbnails = document.querySelectorAll(".thumbnail");
const leftArrow = document.querySelector(".arrow.leftSlider");
const rightArrow = document.querySelector(".arrow.rightSlider");

let currentIndex = 0;
let autoSlideInterval;

function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle("active", i === index);
  });
  thumbnails.forEach((thumb, i) => {
    thumb.classList.toggle("active", i === index);
  });
  currentIndex = index;
}

function nextSlide() {
  const nextIndex = (currentIndex + 1) % slides.length;
  showSlide(nextIndex);
}

function prevSlide() {
  const prevIndex = (currentIndex - 1 + slides.length) % slides.length;
  showSlide(prevIndex);
}

thumbnails.forEach((thumbnail, index) => {
  thumbnail.addEventListener("click", () => {
    showSlide(index);
    resetAutoSlide();
  });
});

function startAutoSlide() {
  autoSlideInterval = setInterval(nextSlide, 5000);
}

function resetAutoSlide() {
  clearInterval(autoSlideInterval);
  startAutoSlide();
}

leftArrow.addEventListener("click", () => {
  prevSlide();
  resetAutoSlide();
});

rightArrow.addEventListener("click", () => {
  nextSlide();
  resetAutoSlide();
});

showSlide(currentIndex);
startAutoSlide();
document.getElementById("copy-icon").addEventListener("click", function () {
  const textToCopy = document.getElementById("vin-value").innerText;

  navigator.clipboard
    .writeText(textToCopy)
    .then(function () {
      alert("Mətn uğurla kopyalandı!");
    })
    .catch(function (err) {
      alert("Kopyalama alınmadı: " + err);
    });
});
