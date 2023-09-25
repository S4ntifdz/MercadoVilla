const carousel = document.querySelector('.carousel');
const leftArrow = document.querySelector('.left-arrow');
const rightArrow = document.querySelector('.right-arrow');

let slideIndex = 0;

leftArrow.addEventListener('click', () => {
  slideIndex = Math.max(slideIndex - 1, 0);
  updateSlidePosition();
});

rightArrow.addEventListener('click', () => {
  const slidesCount = carousel.children.length;
  slideIndex = Math.min(slideIndex + 1, slidesCount - 1);
  updateSlidePosition();
});

function updateSlidePosition() {
  const slideWidth = carousel.clientWidth;
  carousel.style.transform = `translateX(-${slideIndex * slideWidth}px)`;
}
