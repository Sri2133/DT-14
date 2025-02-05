// Add interactivity to the CTA button
const ctaButton = document.querySelector('.cta-button');

ctaButton.addEventListener('click', () => {
  alert('Welcome to Stock Market Sentiment Analysis!');
});

// Add hover effects to feature cards
const featureCards = document.querySelectorAll('.feature-card');

featureCards.forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.3)';
  });

  card.addEventListener('mouseleave', () => {
    card.style.boxShadow = 'none';
  });
});