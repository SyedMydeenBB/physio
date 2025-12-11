// Mobile Navigation Toggle
document.addEventListener('DOMContentLoaded', function() {
    // Add mobile menu toggle functionality
    const mobileMenuBtn = document.createElement('button');
    mobileMenuBtn.className = 'mobile-menu-btn';
    mobileMenuBtn.innerHTML = '<i class="fas fa-bars"></i>';
    
    const header = document.querySelector('.header .container');
    header.prepend(mobileMenuBtn);
    
    mobileMenuBtn.addEventListener('click', function() {
        document.querySelector('.navbar').classList.toggle('show');
    });
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Contact form submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            e.preventDefault();
            // Add your form submission logic here
            alert('Thank you for your message! We will contact you soon.');
            this.reset();
        });
    }
    
    // Appointment booking modal
    const bookBtns = document.querySelectorAll('.book-btn, .btn-secondary');
    bookBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            e.preventDefault();
            showBookingModal();
        });
    });
    
    function showBookingModal() {
        const modalHTML = `
            <div class="modal">
                <div class="modal-content">
                    <span class="close-modal">&times;</span>
                    <h2>Book an Appointment</h2>
                    <form id="bookingForm">
                        <input type="text" placeholder="Your Name" required>
                        <input type="tel" placeholder="Phone Number" required>
                        <input type="email" placeholder="Email Address">
                        <select required>
                            <option value="">Select Service</option>
                            <option value="back-pain">Back Pain Physiotherapy</option>
                            <option value="neck-pain">Neck Pain Physiotherapy</option>
                            <option value="shoulder-pain">Shoulder Pain Physiotherapy</option>
                            <option value="knee-pain">Knee Pain Physiotherapy</option>
                            <option value="home-visit">Home Visit Physiotherapy</option>
                        </select>
                        <input type="date" required>
                        <input type="time" required>
                        <textarea placeholder="Additional Notes"></textarea>
                        <button type="submit">Book Now</button>
                    </form>
                </div>
            </div>
        `;
        
        document.body.insertAdjacentHTML('beforeend', modalHTML);
        
        const modal = document.querySelector('.modal');
        const closeBtn = document.querySelector('.close-modal');
        
        modal.style.display = 'block';
        
        closeBtn.onclick = function() {
            modal.remove();
        };
        
        window.onclick = function(event) {
            if (event.target === modal) {
                modal.remove();
            }
        };
        
        document.getElementById('bookingForm').addEventListener('submit', function(e) {
            e.preventDefault();
            alert('Appointment booked successfully! We will confirm via phone.');
            modal.remove();
        });
    }
});